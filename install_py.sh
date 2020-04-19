#!/bin/bash

# Author      : BALAJI POTHULA <balaji.pothula@techie.com>,
# Date        : 18 December 2019,
# Description : UNIX Help.

# updating local repositories.
sudo apt -y update

# installing supporting softwares
sudo apt -y install build-essential \
                    zlib1g-dev      \
                    libncurses5-dev \
                    libgdbm-dev     \
                    libnss3-dev     \
                    libssl-dev      \
                    libreadline-dev \
                    libffi-dev      \
                    wget

# downloading python source.
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz

# extracting compressed files.
tar -xf Python-3.7.5.tgz

# changing into python dir.
cd python-3.7.5

# testing system and optimizing python.
./configure --enable-optimizations

# installing a second instance of python.
sudo make altinstall

# verifying python version.
python3 --version
