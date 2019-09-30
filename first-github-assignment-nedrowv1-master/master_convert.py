"""function switcher.  dec->bin; bin->dec; eventually dec->hex; hex->dec
gather user input"""

import binary_converter

CONTINUE = True
print("Number Conversion Utility")
while CONTINUE:


    print("MENU:".center(23))
    print("1 - Decimal to Binary\n2 - Binary to Decimal")
    CHOICE = input("Option:_")
    if CHOICE == "1":
        YOUR_NUMBER = float(input("Enter a Decimal:_"))
        YOUR_OUTPUT = binary_converter.convert_dec_to_bin(YOUR_NUMBER)
        YOUR_TYPE = "binary"
    elif CHOICE == "2":
        YOUR_NUMBER = float(input("Enter a Binary:_"))
        YOUR_OUTPUT = binary_converter.convert_bin_to_dec(YOUR_NUMBER)
        YOUR_TYPE = "decimal"
        
    print(YOUR_NUMBER, " in ", YOUR_TYPE, " is ", YOUR_OUTPUT)
    CONT_FLAG = input("Continue: [Y]es/[N]o ").casefold()
    if CONT_FLAG[0] == "N".casefold():
        CONTINUE = False
