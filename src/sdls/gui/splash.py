# -*- coding: utf-8 -*-
import time
import wx._core

from sdls.util.resources import get_path_for_image


class SplashScreen(wx.SplashScreen):

    def __init__(self, callback):
        self.callback = callback

        bitmap = wx.Image(get_path_for_image("splash.png"), wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        super(SplashScreen, self).__init__(bitmap, wx.SPLASH_CENTRE_ON_SCREEN, 0, None)
        # TODO: fix in wx.SplashScreen class
        time.sleep(0.03)
        wx.CallAfter(self.do_callback)

    def do_callback(self):
        self.callback()
        if self:
            self.Destroy()
