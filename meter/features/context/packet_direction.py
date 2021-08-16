#!/usr/bin/env python

from enum import Enum, auto


class PacketDirection(Enum):
    """ Packet Direction creates constants for the direction of the packets.
    
    There are two given directions that the packets can Feature along
    the line. PacketDirection is an enumeration with the values
    forward (1) and reverse (2).
    """
    FORWARD = auto()
    REVERSE = auto()

    # FORWARD = 1
    # REVERSE = 2
    # def __init__(self,FORWARD,REVERSE):
    #     self.FORWARD = FORWARD
    #     self.REVERSE = REVERSE




