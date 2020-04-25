# python packages is to build from source

CLFAGS='-g0 -Wl -I/usr/include:/usr/local/include -L/usr/lib:/usr/local/lib' pip install numpy --global-option=build_ext
