import logging

from ..devicebase import DeviceBase
from ..packet import Packet

_LOGGER = logging.getLogger(__name__)

class Device(DeviceBase):
    '''Delta 3 Plus'''
    SN_PREFIX = b'P351'

    @staticmethod
    def check(sn):
        return sn.startswith(Device.SN_PREFIX)
