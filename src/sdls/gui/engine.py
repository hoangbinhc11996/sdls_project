# -*- coding: utf-8 -*-
from sdls.engine.driver.driver import Driver
from sdls.engine.scan.SDLs_scan import SDLsScan
from sdls.engine.scan.current_video import CurrentVideo
from sdls.engine.calibration.pattern import Pattern
from sdls.engine.calibration.calibration_data import CalibrationData
from sdls.engine.calibration.camera_intrinsics import CameraIntrinsics
from sdls.engine.calibration.autocheck import Autocheck
from sdls.engine.calibration.laser_triangulation import LaserTriangulation
from sdls.engine.calibration.platform_extrinsics import PlatformExtrinsics
from sdls.engine.calibration.combo_calibration import ComboCalibration
from sdls.engine.algorithms.image_capture import ImageCapture
from sdls.engine.algorithms.image_detection import ImageDetection
from sdls.engine.algorithms.laser_segmentation import LaserSegmentation
from sdls.engine.algorithms.point_cloud_generation import PointCloudGeneration
from sdls.engine.algorithms.point_cloud_roi import PointCloudROI


# Instances of engine modules

driver = Driver()
SDLs_scan = SDLsScan()
current_video = CurrentVideo()
pattern = Pattern()
calibration_data = CalibrationData()
camera_intrinsics = CameraIntrinsics()
scanner_autocheck = Autocheck()
laser_triangulation = LaserTriangulation()
platform_extrinsics = PlatformExtrinsics()
combo_calibration = ComboCalibration()
image_capture = ImageCapture()
image_detection = ImageDetection()
laser_segmentation = LaserSegmentation()
point_cloud_generation = PointCloudGeneration()
point_cloud_roi = PointCloudROI()
