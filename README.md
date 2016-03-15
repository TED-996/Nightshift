Nightshift
===

Nightshift is a small tool that changes your wallpaper according to the time of day. You give it a daytime and a nightime wallpaper, and Nightshift creates blends of the two to show around sunrise and sunset, and runs in the background, checking the time and changing the wallpaper according to the sunset and sunrise. 

See it in action: [Screenshots](http://imgur.com/a/Ju9ik)

Download the latest release to try Nightshift too! Don't forget to set it up (either from the installer, the Start menu or by running nightshift_setup.exe -not the installer- after installing Nightshift) so that it knows what wallpapers you want and your sunrise/sunset times.

## Building Nightshift from source

If you want to see what you're running or you want to improve Nightshift, you need Python 2.7 and the following libraries: `py2exe` (to get an executable file), `astral`, `pytz` and `tzlocal` (to get the sunrise/sunset times in your timezone) and `pillow` (to create the blended wallpapers).

1. Press Download ZIP to download the source code, then extract it somewhere useful.
2. Run `setup.py py2exe` in the folder where you extracted the zip file
3. The runnable files are in the `dist` folder.

Now, add nightshift.exe to your startup programs, set it up (with nightshift_setup.exe) and enjoy!

## License:

The MIT License (MIT)
Copyright (c) 2016 TED96

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.