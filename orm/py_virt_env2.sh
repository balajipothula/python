#!/bin/bash

# Author      : BALAJI POTHULA <balaji.pothula@techie.com>,
# Date        : 22 November 2020,
# Description : Install multiple Python versions.

# update packages.
sudo apt -y update

# upgrading gcc.
sudo apt -y upgrade gcc

# install python virtualenv and dependencies. 
sudo apt -y install curl            \
                    gcc             \
                    git-core        \
                    libbz2-dev      \
                    libreadline-dev \
                    libsqlite3-dev  \
                    libssl-dev      \
                    make            \
                    zlib1g-dev

# grabing latest pyenv and pyenv-virtualenv source from github.
git clone https://github.com/pyenv/pyenv.git             $HOME/.pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git   $HOME/.pyenv/plugins/pyenv-virtualenv
