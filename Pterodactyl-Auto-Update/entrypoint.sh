#!/bin/sh

cd /home/container

## Checking Java and Python Version
python --version
java -version


# Downloading updater.py (Current Version 3.0)

wget  https://github.com/Feuersteinium/mountain/releases/download/PAD-1.0/updater.py -Oupdater.py


# RUN!
python3 updater.py ; ${STARTUP}



