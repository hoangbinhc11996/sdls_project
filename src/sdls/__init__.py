# -*- coding: utf-8 -*-

__author__ = 'Hoang Chu <hoangbinhc11996@gmail.com>'
__version__ = '1.3'
__datetime__ = '12-12-2018'
__commit__ = ''


def Singleton(class_):
    class class_w(class_):
        _instance = None

        def __new__(class_, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w, class_).__new__(class_, *args, **kwargs)
                class_w._instance.__initialized = False
            return class_w._instance

        def __init__(class_, *args, **kwargs):
            if class_w._instance.__initialized:
                return
            super(class_w, class_).__init__(*args, **kwargs)
            class_w._instance.__initialized = True

    class_w.__name__ = class_.__name__
    return class_w
