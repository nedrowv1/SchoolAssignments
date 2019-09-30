"""number conversion functions; dec -> bin; bin -> dec"""

def convert_bin_to_dec(binary):
    """convert a given base 2 to base 10 float"""
    decimal = 0
    decimal_dec = 0

    #convert binary input into iterable, sortable format
    binary_list = list(str(binary))
    deci_index = binary_list.index(".")  # find float

    #to convert a binary whole number into decimal, multiply the current
    #decimal, then add the binary bit
    for bit_ in binary_list[:deci_index]:
        decimal = (decimal * 2) + float(bit_)

    #to convert a fractional binary, add the current bit to the calculated
    #decimal, and divide by 2
    for bit_ in binary_list[:deci_index:-1]:
        decimal_dec = (float(bit_) + float(decimal_dec)) / 2

    decimal_float = decimal + decimal_dec
    return float(decimal_float)


def convert_dec_to_bin(decimal):
    """convert a given float in base 10 to base 2"""
    decimal_string = ""
    binary_string = ""

    decimal_part = decimal % 1
    quotient = int(decimal)

    #to convert a whole base 10 number into binary, divide by 2 until the
     #whole number portion is 0 and reverse order of remainders
    while quotient >= 1:
        binary_string += str(int(quotient) % 2)
        quotient = quotient / 2
    binary_string = binary_string[::-1]

    #fractional conversion into binary is opposite whole number conversion.
    #multiply the fractional pay by 2, until the fraction part equals 0
    while decimal_part % 1 != 0:
        decimal_string += str(int(decimal_part * 2))
        decimal_part = (decimal_part * 2) % 1

    binary_string = binary_string + "." + decimal_string  # add them together

    return float(binary_string)
