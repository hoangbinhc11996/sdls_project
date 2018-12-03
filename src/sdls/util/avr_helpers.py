# -*- coding: utf-8 -*-

import os
import resources
from subprocess import Popen, PIPE, STDOUT

import logging
logger = logging.getLogger(__name__)

from sdls.util import system as sys


class AvrError(Exception):
    pass


class AvrDude(object):

    def __init__(self, protocol="arduino", microcontroller="atmega328p",
                 baud_rate="19200", port=None):
        self.protocol = protocol
        self.microcontroller = microcontroller
        self.baud_rate = baud_rate

        if sys.is_windows():
            self.avrdude = os.path.abspath(resources.get_path_for_tools("avrdude.exe"))
        elif sys.is_darwin():
            self.avrdude = os.path.abspath(resources.get_path_for_tools("avrdude"))
        else:
            try:
                Popen(["avrdude"], stdout=PIPE, stderr=STDOUT)
                self.avrdude = "avrdude"
            except:
                self.avrdude = None

        if self.avrdude is None:
            raise AvrError('avrdude not installed')

        self.avrconf = os.path.abspath(resources.get_path_for_tools("avrdude.conf"))
        self.port = port

    def _run_command(self, flags=[], callback=None):
        config = dict(avrdude=self.avrdude, avrconf=self.avrconf)
        cmd = ['%(avrdude)s'] + flags
        cmd = [v % config for v in cmd]
        logger.info(' ' + ' '.join(cmd))
        p = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=sys.is_windows())
        out = ''
        while True:
            char = p.stdout.read(1)
            if not char:
                break
            out += char
            if char == '#':
                if callback is not None:
                    callback()
        return out

    def flash(self, hex_path=None, clear_eeprom=False, callback=None):
        if hex_path is None:
            hex_path = resources.get_path_for_firmware("sdls-fw.hex")
        if clear_eeprom:
            hex_path = resources.get_path_for_firmware("eeprom_clear.hex")
        flags = ['-C', '%(avrconf)s', '-c', self.protocol, '-p', self.microcontroller,
                 '-P', '%s' % self.port, '-b', str(self.baud_rate), '-D', '-U',
                 'flash:w:%s' % os.path.basename(hex_path)]
        try:
            cwd = os.getcwd()
            os.chdir(os.path.dirname(os.path.abspath(hex_path)))
            out = self._run_command(flags, callback)
            logger.info(' Upload completed')
        finally:
            os.chdir(cwd)
        return out
