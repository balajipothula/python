#!/bin/bash

# Author      : BALAJI POTHULA <balaji.pothula@techie.com>,
# Date        : 15 September 2019,
# Description : UNIX Help.

# update packages.
sudo apt -y update

# upgrading gcc.
sudo apt -y upgrade gcc

# install python virtualenv and dependencies. 
sudo apt -y install libpq-dev         \
                    python-dev        \
                    python3-dev       \
                    python-virtualenv \
                    unzip             \
                    virtualenv        \
                    zip

# create emp virtual environment.
virtualenv --python=/usr/bin/python3 $HOME/emp

# activate emp virtual environment.
source $HOME/emp/bin/activate

# update pip package.
python3 -m pip install --upgrade pip

# install python packages.
pip install psycopg2 SQLAlchemy
pip install psycopg2 SQLAlchemy -t .

# change directory to emp virtual environment,
# zip python packages
cd $HOME/emp/lib/python3.5/site-packages && \
zip -qq -r $HOME/emp.zip .               && \
chmod 777  $HOME/emp.zip                 && \
cd
