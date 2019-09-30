#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:39:16 2018

@author: Nedrow, Vanessa
"""


# dictionaries and case/switch could be alternatives
def choose_hex(hex_num):
    """ hexadecimal character converter"""

    if hex_num == 10:
        hex_num = "A"
    elif hex_num == 11:
        hex_num = "B"
    elif hex_num == 12:
        hex_num = "C"
    elif hex_num == 13:
        hex_num = "D"
    elif hex_num == 14:
        hex_num = "E"
    elif hex_num == 15:
        hex_num = "F"
    elif hex_num == "A":
        hex_num = 10
    elif hex_num == "B":
        hex_num = 11
    elif hex_num == "C":
        hex_num = 12
    elif hex_num == "D":
        hex_num = 13
    elif hex_num == "E":
        hex_num = 14
    elif hex_num == "F":
        hex_num = 15
    else:
        hex_num = hex_num
    return hex_num


def convert_hex_to_dec(hexidecimal):
    """convert a given float in base 16 to base 10
    in progress"""

    decimal_dec = 0
    decimal = 0
    powerstep = 0
    hex_left = []
    hex_right = []
    hex_list = list(hexidecimal)
    lenhex = len(hex_list)

    # find the break between integer and decimal
    try:
        deci_index = hex_list.index(".")
    except ValueError:
        deci_index = len(hex_list)

    # append items before the decimal
    for hex_ in hex_list[0:deci_index]:
            hex_left.append(int(choose_hex(hex_)))  # this indentation is weird

    # append items after the decimal
    for hex_ in hex_list[deci_index + 1:lenhex]:
        hex_right.append(int(choose_hex(hex_)))

    # convert integer portion
    for cnt in range(len(hex_left), -1, -1):
        if cnt != len(hex_left):
            decimal = (hex_left[cnt] * (16 ** powerstep)) + float(decimal)
            powerstep += 1
    # convert decimal portion
    factor = -1
    for cnt in range(len(hex_right)):
        decimal_dec = (hex_right[cnt] * (16 ** factor)) + float(decimal_dec)
        factor -= 1

    # add them together
    decimal_float = decimal + decimal_dec
    return float(decimal_float)


def convert_dec_to_hex(quotient):
    """convert a given float in base 10 to base 16
    in progress"""
    hexidecimal = []
    hex_dec = []
    hex_string = ""
    fraction = False

    # find the decimal portion
    try:
        deci_part = quotient % 1
    except ValueError:
        deci_part = 0

    quotient = float(int(quotient))

    # convert decimal portion
    while deci_part % 1 != 0:
        hex_dec.append(int(deci_part * 16))
        deci_part = (deci_part * 16) % 1
        fraction = True
    # convert integer portion
    while quotient >= 1:
        hexidecimal.insert(0, int(quotient) % 16)
        quotient = quotient / 16

    # add them together and return string
    for hex_ in hexidecimal:
        hex_string += str(choose_hex(hex_))
    if fraction:
        hex_string += "."
        for hex_ in hex_dec:
            hex_string += str(choose_hex(hex_))
    return hex_string
# it wants a blank line at the end of the file
