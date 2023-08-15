#!/bin/sh

cd /home/container

## Checking Java and Python Version
python --version
java -version


# Downloading updater.py (Current Version 3.0)
wget  https://github.com/Feuersteinium/mountain/releases/download/PAD-1.0/updater.py -Oupdater.py



# Check for config

if [ $(ls -l | grep "updater.toml" | wc -l)  -eq 1 ]
then
    echo "updater.toml does exist. Won't do anything."
else
    wget https://raw.githubusercontent.com/Feuersteinium/mountain/master/Pterodactyl-Auto-Update/updater.toml -Oupdater.toml
fi


echo "Ready for startup..."

# RUN!
python3 updater.py ; ${STARTUP}



