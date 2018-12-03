# -*- coding: utf-8 -*-

import json
import urllib2
import webbrowser

from sdls import __version__, __datetime__, __commit__
from sdls.util import system as sys


class Version:
    def __init__(self, version):
        self.number = ''
        self.prenumber = ''
        for p in ['a', 'b', 'rc']:
            data = version.split(p)
            if len(data) == 2:
                self.number = data[0]
                self.prenumber = p + data[1]
        if self.prenumber == '':
            self.number = version
            self.prenumber = 'z'


current_version = Version(__version__)
current_datetime = __datetime__
current_commit = __commit__

latest_version = ''
latest_datetime = ''
latest_commit = ''

URL_API_RELEASES = 'https://api.github.com/repos/bqlabs/sdls/releases/latest'
URL_DOWNLOAD = 'https://github.com/bqlabs/sdls/releases/download/'


def download_lastest_data():
    global latest_version, latest_commit, latest_datetime
    try:
        f = urllib2.urlopen(URL_API_RELEASES, timeout=1)
        content = json.loads(f.read())
        tag_name = content['tag_name']
        f = urllib2.urlopen(URL_DOWNLOAD + tag_name + '/version', timeout=1)
        content = json.loads(f.read())
        latest_version = Version(content['version'])
        latest_datetime = content['datetime']
        latest_commit = content['commit']
    except:
        pass


def check_for_updates():
    return latest_version is not '' and \
        latest_version.number >= current_version.number and \
        latest_version.prenumber >= current_version.prenumber and \
        current_datetime is not '' and \
        latest_datetime > current_datetime


def _get_executable_url(version):
    url = None
    if sys.is_linux():
        import platform
        url = 'https://launchpad.net/~bqlabs/+archive/ubuntu/sdls/+files/'
        url += 'sdls_'
        url += version + '-'
        url += platform.linux_distribution()[2] + '1_'
        if platform.architecture()[0] == '64bit':
            url += 'amd64.deb'
        elif platform.architecture()[0] == '32bit':
            url += 'i386.deb'
        del platform
    elif sys.is_windows():
        url = URL_DOWNLOAD
        url += latest_version
        url += '/sdls_'
        url += version + '.exe'
    elif sys.is_darwin():
        url = URL_DOWNLOAD
        url += latest_version
        url += '/sdls_'
        url += version + '.dmg'
    return url


def download_latest_version():
    url = _get_executable_url(latest_version)
    if url is not None:
        webbrowser.open(url)
