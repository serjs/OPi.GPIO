# -*- coding: utf-8 -*-
# Copyright (c) 2018 Sergey Bogatyrets
# See LICENSE.md for details.

import functools
from copy import deepcopy
from OPi.constants import BOARD, BCM, SUNXI, CUSTOM


class _sunXi(object):

    def __getitem__(self, value):

        offset = ord(value[1]) - 65
        pin = int(value[2:])

        assert value[0] == "P"
        assert 0 <= offset <= 25
        assert 0 <= pin <= 31

        return (offset * 32) + pin


_pin_map = {
    # Physical pin to actual GPIO pin
    BOARD: {
        3: 12,
        5: 11,
        7: 6,
        8: 13,
        10: 14,
        11: 1,
        12: 110,
        13: 0,
        15: 3,
        16: 68,
        18: 71,
        19: 64,
        21: 65,
        22: 2,
        23: 66,
        24: 67,
        26: 21,
        27: 19,
        28: 18,
        29: 7,
        31: 8,
        32: 200,
        33: 9,
        35: 10,
        36: 201,
        37: 20,
        38: 198,
        40: 199
    },

    # BCM pin to actual GPIO pin
    BCM: {
        2: 12,
        3: 11,
        4: 6,
        6: 1,
        7: 0,
        8: 3,
        10: 64,
        11: 65,
        12: 66,
        14: 19,
        15: 7,
        18: 10,
        19: 20,
        24: 13,
        25: 14,
        26: 110,
        28: 68,
        29: 71,
        31: 2,
        32: 67,
        33: 21,
        34: 18,
        36: 200,
        38: 201,
        39: 198,
        40: 199
    },

    SUNXI: _sunXi(),

    # User defined, initialized as empty
    CUSTOM: {}
}


def set_custom_pin_mappings(mappings):
    _pin_map[CUSTOM] = deepcopy(mappings)


def get_gpio_pin(mode, channel):
    assert mode in [BOARD, BCM, SUNXI, CUSTOM]
    return _pin_map[mode][channel]


bcm = functools.partial(get_gpio_pin, BCM)
board = functools.partial(get_gpio_pin, BOARD)
sunxi = functools.partial(get_gpio_pin, SUNXI)
custom = functools.partial(get_gpio_pin, CUSTOM)
