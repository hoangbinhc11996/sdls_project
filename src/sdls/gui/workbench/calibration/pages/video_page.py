# -*- coding: utf-8 -*-
import wx._core

from sdls.util import resources

from sdls.gui.engine import image_capture, image_detection, scanner_autocheck, laser_triangulation, \
    platform_extrinsics
from sdls.gui.workbench.calibration.pages.page import Page
from sdls.gui.util.image_view import ImageView
from sdls.gui.util.video_view import VideoView


class VideoPage(Page):

    def __init__(self, parent, title='Video page', start_callback=None, cancel_callback=None):
        Page.__init__(self, parent,
                      title=title,
                      desc=_("Put the pattern on the platform as shown in the "
                             "picture and press \"Start\""),
                      left=_("Cancel"),
                      right=_("Start"),
                      button_left_callback=cancel_callback,
                      button_right_callback=start_callback,
                      view_progress=True)

        # Elements
        image_view = ImageView(self.panel, quality=wx.IMAGE_QUALITY_HIGH)
        image_view.set_image(wx.Image(resources.get_path_for_image("pattern-position.png")))
        self.video_view = VideoView(self.panel, self.get_image)

        # Layout
        self.panel_box.Add(image_view, 3, wx.ALL | wx.EXPAND, 3)
        self.panel_box.Add(self.video_view, 2, wx.ALL | wx.EXPAND, 3)
        self.Layout()

    def initialize(self):
        self.gauge.SetValue(0)
        self.right_button.Enable()

    def play(self):
        self.video_view.play()
        self.GetParent().Layout()
        self.Layout()

    def stop(self):
        self.initialize()
        self.video_view.stop()

    def reset(self):
        self.video_view.reset()

    def get_image(self):
        if scanner_autocheck.image is not None:
            image = scanner_autocheck.image
        elif laser_triangulation.image is not None:
            image = laser_triangulation.image
        elif platform_extrinsics.image is not None:
            image = platform_extrinsics.image
        else:
            image = image_capture.capture_pattern()
            image = image_detection.detect_pattern(image)
        return image
