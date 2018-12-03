# -*- coding: utf-8 -*-

import wx._core
import platform
s = platform.system()
del platform


def is_linux():
    return s == 'Linux'


def is_darwin():
    return s == 'Darwin'


def is_windows():
    return s == 'Windows'


def is_wx28():
    return wx.__version__.startswith('2.8')


def is_wx30():
    return wx.__version__.startswith('3.0')
