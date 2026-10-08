import ctypes as c
import json, os, subprocess as sp, time
from pathlib import Path
root=Path('/tmp/kitty-resize-check')
kitty='/home/warloc/git/kitty/kitty/launcher/kitty'
conf=root/'test.conf'
conf.write_text('allow_remote_control socket-only\nenabled_layouts splits\nshell /bin/bash --noprofile --norc\ninitial_window_width 100c\ninitial_window_height 25c\n')
env=dict(os.environ,DISPLAY=':95',LIBGL_ALWAYS_SOFTWARE='1')
xvfb=sp.Popen(['Xvfb',':95','-screen','0','1400x800x24'],stdout=sp.DEVNULL,stderr=sp.DEVNULL)
proc=None
def rc(*args):
    return sp.check_output([kitty,'@','--to','unix:'+str(root/'socket'),*args],env=env,text=True,stderr=sp.DEVNULL)
def state():return json.loads(rc('ls'))
def panes():return state()[0]['tabs'][0]['windows']
def wait(fn):
    for _ in range(100):
        time.sleep(.1)
        try:
            value=fn()
            if value:return value
        except (sp.CalledProcessError,KeyError,IndexError):pass
    raise RuntimeError('Timed out')
try:
    time.sleep(.3)
    log=(root/'kitty.log').open('w')
    proc=sp.Popen([kitty,'--config',str(conf),'--listen-on','unix:'+str(root/'socket')],env=env,stdout=log,stderr=log)
    wait(state)
    target=int(rc('launch','--type=window'))
    wait(lambda:len(panes())==2)
    before=next(w for w in panes() if w['id']==target)
    x=c.CDLL('libX11.so.6');xt=c.CDLL('libXtst.so.6')
    x.XOpenDisplay.argtypes=[c.c_char_p];x.XOpenDisplay.restype=c.c_void_p
    x.XSetInputFocus.argtypes=[c.c_void_p,c.c_ulong,c.c_int,c.c_ulong]
    x.XKeysymToKeycode.argtypes=[c.c_void_p,c.c_ulong];x.XKeysymToKeycode.restype=c.c_uint
    x.XFlush.argtypes=[c.c_void_p]
    xt.XTestFakeKeyEvent.argtypes=[c.c_void_p,c.c_uint,c.c_int,c.c_ulong]
    display=x.XOpenDisplay(b':95')
    x.XSetInputFocus(display,state()[0]['platform_window_id'],1,0);x.XFlush(display)
    def key(sym,down):xt.XTestFakeKeyEvent(display,x.XKeysymToKeycode(display,sym),down,0)
    key(0xffe3,1);key(0xffe1,1);key(ord('r'),1)
    key(ord('r'),0);key(0xffe1,0);key(0xffe3,0);x.XFlush(display)
    overlay=wait(lambda:next((w for w in panes() if w['id']>target),None))
    overlay_id=overlay['id']
    wait(lambda:'Resize this window' in rc('get-text','--match',f'id:{overlay_id}'))
    rc('send-text','--match',f'id:{overlay_id}','w')
    changed=wait(lambda:next((w for w in panes() if w['id']==target and w['columns']>before['columns']),None))
    rc('send-key','--match',f'id:{overlay_id}','esc')
    wait(lambda:len(panes())==2)
    result={'result':'PASS','shortcut':'Ctrl+Shift+R via XTest','columns_before':before['columns'],'columns_after':changed['columns'],'escape_closed_overlay':True}
    (root/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
finally:
    if proc:
        proc.terminate();proc.wait(timeout=5)
    xvfb.terminate();xvfb.wait(timeout=5)
