# -*- coding: utf-8 -*-

import os

from sdls.util.mesh_loaders import ply
from sdls.util.mesh_loaders import stl

import logging
logger = logging.getLogger(__name__)


def load_supported_extensions():
    """ return a list of supported file extensions for loading. """
    return ['.ply', '.stl']


def save_supported_extensions():
    """ return a list of supported file extensions for saving. """
    return ['.ply']


def load_mesh(filename):
    """
    loadMesh loads one model from a file.
    """
    ext = os.path.splitext(filename)[1].lower()
    if ext == '.ply':
        return ply.load_scene(filename)
    if ext == '.stl':
        return stl.load_scene(filename)
    logger.error('Error: Unknown model extension: %s' % (ext))
    return None


def save_mesh(filename, _object):
    """
    Save a object into the file given by the filename.
    Use the filename extension to find out the file format.
    """
    ext = os.path.splitext(filename)[1].lower()
    if ext == '.ply':
        ply.save_scene(filename, _object)
        return
    logger.error('Error: Unknown model extension: %s' % (ext))
