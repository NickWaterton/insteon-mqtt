#===========================================================================
#
# Tests for: insteont_mqtt/message/InpExtended.py
#
#===========================================================================
import insteon_mqtt.message as Msg
import pytest

#===========================================================================
class Test_InpExtended:
    #-----------------------------------------------------------------------
    def test_basic(self):
        b = bytes([0x02, 0x51,
                   0x3e, 0xe2, 0xc4, 0x23, 0x9b, 0x65,
                   0x41, 0x11, 0x01,
                   0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,
                   0x0a, 0x0b, 0x0c, 0x0d, 0x0e])
        obj = Msg.InpExtended.from_bytes(b)

        # TODO: check obj

        str(obj)

    #-----------------------------------------------------------------------


#===========================================================================