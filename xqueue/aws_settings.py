from __future__ import absolute_import
import logging

from .production import *

logging.error("aws_settings is deprecated, please use xqueue.production instead")
