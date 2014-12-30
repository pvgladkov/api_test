__author__ = 'pgladkov'


import sys
import os
from ConfigParser import ConfigParser


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances or ('modify' in kwargs and kwargs['modify']):
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.config = ConfigParser()
        file_name = os.path.join('../config', 'config.cfg')
        try:
            self.config.readfp(open(file_name))
        except (IOError, OSError):
            sys.exit("File " + file_name + " not found")


    @property
    def url(self):
        return self.config.get('main', 'host')