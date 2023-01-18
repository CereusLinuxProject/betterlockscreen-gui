# Betterlockscreen Configuration tool
A GUI configuration tool to change Betterlockscreen background and modify dim/blur. 
This project was forked from <a href="https://github.com/arcolinux/arcolinux-betterlockscreen">ArcoLinux Betterlockscreen</a>.

## New Features
- You can modify blur for your lockscreen background.
- GUI takes dim & blur values from <code>~/.config/betterlockscreenrc</code> (if it doesn't exist, the <code>get_values.sh</code> will create it).
- A file-manager custom action was added to change background more easily.
- A custom script for <a href="https://github.com/CereusLinuxProject/resolution-hooks">resolution-hooks</a>, which will update the lockscreen background whenever the screen resolution changes or a screen is added/removed.

## Installation
For XBPS distributions, <code>betterlockscreen-gui</code> is available in <a href="https://sourceforge.net/projects/cereus-linux/files/repos/cereus-extra/">cereus-extra</a> repository. If using Cereus Linux LXQt it is already included in ISO. To install it manually, run:

    # xbps-install -S betterlockscreen-gui
