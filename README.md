# toontown-launcher
 A recreation of the Disney's Toontown Online game launcher.

The launcher uses Python 3.8, but I believe any version of 3 will do.

Requirements:
- `Pillow`


If you are looking for where the images are, they are encoded in base64.
The reason for this is because of a compiler issue I've had in the past.
However if someone can make it work, feel free to convert it back to files!

To convert, currently the tool has to be edited.
It is however a very simple base64 encoder so a new tool can be made to replace it if you'd like.

Current features include:
- Splash screen (it has no GUI yet)
- Main GUI with buttons (Only the close buttons work atm)

What needs work or added:
- Rounded window with a Taskbar Icon
- - Maybe a Windows API? Mac OS and Linux from what I've read support this via Tkinter out of the box.)

- Graphic Options GUI [not implemented]
- - Will probably just detect whether or not you have a `settings.json` or `preferences.json` and let you edit them in a similar fashion to how Disney had it. Maybe add more options?

- Updater [not implemented]
- - `patcher.ver` is outdated and clunky, so an example of what I think it better is below:
```
    {
    files : {
        name: "Toontown.exe",
        size: 012345,
        hash: 0deadbeef0,
        },{
        name: "libpandagl.dll",
        size: 012345,
        hash: 0deadbeef0,
        }
    }
```

This code is free to modify and redistribute as you please.
I started this, but haven't had that much time to do some touch up.
