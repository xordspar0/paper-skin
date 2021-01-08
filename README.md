paper-skin
==========

A simple Python script for making Minecraft player skins into printable paper crafts

You can obtain your current skin file my logging into your account at
minecraft.net, going to the skin section of your profile, right clicking your
current skin image, and saving it as a file.

Usage
=====

First, install the dependencies as detailed below. Then, simply type the following in the command line, replacing SKIN_FILE with your skin file and OUTPUT_FILE with the name of the file to create:

    paper-skin.py SKIN_FILE OUTPUT_FILE

Installing Dependencies
=======================

paper-skin uses Python 3 and Pillow.

Linux
-----

Install Python 3 and Pillow from your distro's repository.

For example:

    sudo apt-get install python3 python-pil

Alternatively, paper-skin is in the [AUR](https://aur.archlinux.org/packages/paper-skin).

Windows
-------

Download and install the latest release of [Python 3.x](https://www.python.org/downloads/).

Download and install [pip](http://www.pip-installer.org/en/latest/installing.html).

Run the following command to install Pillow:

    pip install --use-wheel Pillow
