# Kitty SDL sources

Resume.design models the owner-selected T002 manual-save design. NativeSessionCodec
maps to kitty/session.py and Kitty's existing serializers/loader; SavedSessionCatalog
and ResumePicker map to kitty/resume.py. The earlier observer/Codex/geometry draft
is superseded. No automatic snapshotting is modeled or implemented.

Validate and format with the installed SDL CLI:

```sh
/home/warloc/.local/lib/sdp/sdl check SDP/SDL/Kitty/Resume.design
/home/warloc/.local/lib/sdp/sdl format SDP/SDL/Kitty/Resume.design
/home/warloc/.local/lib/sdp/sdl viewpoints SDP/SDL/Kitty/Resume.design --format navigator --project kitty --output /tmp/kitty-resume-viewpoints
```

See [design](../../04--Design/KittyResume/Study.md) and
[verification](../../Verification/KittyResume.md).
