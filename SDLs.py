#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Check dependencies
try:
    import os
    import wx
    import sys
    import cv2
    import OpenGL
    import serial
    import numpy
    import scipy
    import matplotlib
except ImportError as e:
    print(e.message)
    exit(1)

# Try first the sources
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from sdls.util import resources

resdir = os.path.join(os.path.dirname(__file__), "res")
if not os.path.exists(resdir):
    resdir = "/usr/share/sdls"

resources.set_base_path(resdir)


def main():
    from sdls.gui import app
    app.SDLsApp().MainLoop()

if __name__ == '__main__':
    main()
