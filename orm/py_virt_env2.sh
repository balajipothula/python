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

# 
echo 'export PYENV_ROOT="$HOME/.pyenv"'    | tee -a "$HOME/.bashrc" "$HOME/.profile" > /dev/null
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' | tee -a "$HOME/.bashrc" "$HOME/.profile" > /dev/null

echo 'if command -v pyenv 1>/dev/null 2>&1; then eval "$(pyenv init -)"; fi' | tee -a "$HOME/.bashrc" "$HOME/.profile" > /dev/null

exec "$SHELL"

python -m pip install --upgrade pip setuptools wheel
