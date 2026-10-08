import json, os, subprocess as sp, time
from pathlib import Path
root = Path('/tmp/kitty-resume-check')
kitty = '/home/warloc/git/kitty/kitty/launcher/kitty'
for name in ('one', 'two space', 'three', 'state'):
    (root/name).mkdir(exist_ok=True)
conf=root/'test.conf'
conf.write_text('allow_remote_control socket-only\nshell /bin/bash --noprofile --norc\nenabled_layouts splits,tall\ninitial_window_width 100c\ninitial_window_height 25c\n')
fake=root/'fake-codex.py'
fake.write_text('import sys, time\nprint(sys.argv, flush=True)\ntime.sleep(300)\n')
env=dict(os.environ, DISPLAY=':94', LIBGL_ALWAYS_SOFTWARE='1', XDG_STATE_HOME=str(root/'state'))
xvfb=sp.Popen(['Xvfb', ':94', '-screen', '0', '1400x800x24'], stdout=sp.DEVNULL,stderr=sp.DEVNULL)
processes=[]
def rc(sock,*args):
    return sp.check_output([kitty,'@','--to','unix:'+str(root/sock),*args],env=env,text=True,stderr=sp.DEVNULL)
def wait(sock, predicate=lambda x: True):
    for _ in range(100):
        time.sleep(.1)
        try:
            value=json.loads(rc(sock,'ls'))
            if predicate(value): return value
        except (sp.CalledProcessError, json.JSONDecodeError): pass
    raise RuntimeError('Timed out '+sock)
def start(sock,*args):
    log=(root/(sock+'.log')).open('w')
    processes.append(sp.Popen([kitty,'--config',str(conf),'--listen-on','unix:'+str(root/sock),*args],env=env,stdout=log,stderr=log))
    return wait(sock)
def panes(state):
    return [w for osw in state for t in osw['tabs'] for w in t['windows']]
try:
    time.sleep(.3)
    a=start('original','--directory',str(root/'one'))
    rc('original','set-tab-title','First')
    rc('original','goto-layout','splits')
    rc('original','launch','--type=window','--cwd',str(root/'two space'),'--title','second-shell')
    rc('original','launch','--type=tab','--tab-title','Second','--cwd',str(root/'three'))
    time.sleep(1)
    rc('original','send-text','--match','id:3',f'python3 {fake} resume example-explicit-id\r')
    before=wait('original',lambda s:any('python3' in ' '.join(p.get('cmdline',[])) for w in panes(s) for p in w['foreground_processes']))
    saved=root/'snapshot.kitty-session'
    rc('original','action','save_as_session','--save-only','--use-foreground-process','--relocatable',str(saved))
    time.sleep(.3)
    assert str(saved) in json.loads((root/'state/kitty/saved-sessions.json').read_text())
    assert 'example-explicit-id' in saved.read_text(), saved.read_text()
    after=start('restored','--session',str(saved))
    after=wait('restored',lambda s:len(panes(s))==3 and any('example-explicit-id' in ' '.join(p.get('cmdline',[])) for w in panes(s) for p in w['foreground_processes']))
    def normalize(s):
        return [(t['title'],t['layout'],[(w['cwd'],w['is_focused']) for w in t['windows']]) for o in s for t in o['tabs']]
    assert normalize(before)==normalize(after),(normalize(before),normalize(after))
    (root/'before.json').write_text(json.dumps(before,indent=2))
    (root/'after.json').write_text(json.dumps(after,indent=2))
    print(json.dumps({'result':'PASS','tabs':2,'panes':3,'cwd_and_layout':normalize(after),'foreground_resume_argv':True,'catalog_registered':True}))
finally:
    for proc in processes:
        proc.terminate()
        try: proc.wait(timeout=5)
        except sp.TimeoutExpired: proc.kill(); proc.wait()
    xvfb.terminate(); xvfb.wait(timeout=5)
