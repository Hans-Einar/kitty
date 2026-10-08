import fcntl,json,os,pty,select,struct,subprocess as sp,termios,time
from pathlib import Path
root=Path('/tmp/kitty-resume-check')
kitty='/home/warloc/git/kitty/kitty/launcher/kitty'
env=dict(os.environ,TERM='xterm-256color',XDG_STATE_HOME=str(root/'state'))
for action in ('cancel','select','invalid'):
    result=root/(action+'-argv.json')
    result.unlink(missing_ok=True)
    code=f"import json,os; from kitty.resume import main; os.execv=lambda exe,args,json=json: open({str(result)!r},'w').write(json.dumps(args)); main(['--config','NONE'])"
    if action=='invalid':
        bad=root/'bad.kitty-session'; bad.write_text('garbage_command\n')
        (root/'state/kitty/saved-sessions.json').write_text(json.dumps([str(bad)]))
    master,slave=pty.openpty()
    fcntl.ioctl(slave,termios.TIOCSWINSZ,struct.pack('HHHH',25,100,0,0))
    proc=sp.Popen([kitty,'+runpy',code],stdin=slave,stdout=slave,stderr=slave,env=env,start_new_session=True)
    os.close(slave)
    output=b''
    deadline=time.monotonic()+10
    while b'Search:' not in output and time.monotonic()<deadline:
        if select.select([master],[],[],.1)[0]: output+=os.read(master,65536)
    assert b'Search:' in output,output
    os.write(master,b'\x1b' if action=='cancel' else b'\r')
    if action=='invalid':
        while b'Cannot open session' not in output and time.monotonic()<deadline:
            if select.select([master],[],[],.1)[0]: output+=os.read(master,65536)
        assert b'Cannot open session' in output,output
        os.write(master,b'\x1b')
    while proc.poll() is None and time.monotonic()<deadline:
        if select.select([master],[],[],.1)[0]:
            try: output+=os.read(master,65536)
            except OSError: break
    assert proc.wait(timeout=5)==0,repr(output)
    os.close(master)
    if action=='select':
        args=json.loads(result.read_text()); assert args[-2:]==['--session',str(root/'snapshot.kitty-session')],args
    else: assert not result.exists()
    (root/(action+'-pty.bin')).write_bytes(output)
    print(action+': PASS')
(root/'state/kitty/saved-sessions.json').write_text(json.dumps([str(root/'snapshot.kitty-session')]))
