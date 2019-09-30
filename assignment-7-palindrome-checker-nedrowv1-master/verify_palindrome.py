"""a series of functions that, together, will check whether
any default object (except dictionaries) would be considered a
palindrome.  lists accept any supported data type: nested lists
or tuples are expanded in such a way that the items in the nested object
are placed in the same position: example: [1, 2 [3, 4, 5], [4, 3], 2, 1] and
[1, 2, [3, 4, 5, [4, 3]], 2, 1] would both be treated as
[1, 2, 3, 4, 5, 4, 3, 2, 1], as would [1, (2, 3, 4, 5), [4, (3, 2)], 1].
Standard punctuation is ignored in strings, but
not strings embedded in lists.  'Madam, I'm Adam' would return as a palindrome,
["Adam", "im", "I'm", "Adam"] would not. [1, '1'] is not a palindrome, 
[1, 1] or ['1', '1'] are.  Capitalization is ignored in both strings
and lists"""


def item_checker(obj1, obj2):
    """check that two objects are the same"""
    if obj1 == obj2:
        return True
    return False


def nest_check(tested_list):
    """find nested lists and un-nest them and return un-nested list, or if
    the original list is un-nested, return it"""

    new_list = []
    for item in tested_list:
        if isinstance(item, (list, tuple)):
            new_item = nest_check(item)
            for cell in new_item:
                new_list.append(cell)  # removes nesting
        elif isinstance(item, str):
            # makes string upper case, eliminating case mismatches
            new_list.append(item.upper())

        else:  # integers and floats
            # and dictionaries; since unsorted they will always return true as long as the keys match
            # [{'A':1, 'B':2, 'C':3}, 'infinity', {'B':2, 'A':1, "C":3}] will return as a palindrome,
            # [{'A':1, 'B':2, 'C':3}, 'infinity', {'B':3, 'A':2, "C":1}] will not
            new_list.append(item)
    return new_list


def pal_check(i_palindrome_i):
    """handles different types and reducing the original input"""
    valid_type = True
    if isinstance(i_palindrome_i, str):
        test_item = ""
        for let in i_palindrome_i:
            if let not in ":;,.?'!" and let != " ":
                # ignore basic punctuation and spaces,
                # but not symbols and shorthand
                # or hyphens; race-car != racecar but race, car == racecar!
                test_item += let.upper()
                # makes string upper case, eliminating case mismatches
    elif isinstance(i_palindrome_i, list):
        test_item = nest_check(i_palindrome_i)
        # check and un-nest nested lists (now with added tuples!)
    else:  # quick and dirty error handling
        valid_type = False
        data_type = type(i_palindrome_i)
        print("Oops! Data type,", data_type, ", isn't supported!")

    if valid_type:
        while len(test_item) > 1:
            if item_checker(test_item[0], test_item[-1]):
                test_item = test_item[1:-1]
            else:
                break  # exit at first non-matching pair

        if test_item and len(test_item) == 1 or len(test_item) == 0:
            # if the length of test_item (once un-nested if applicable) is
            # odd, one item will be left and it compares to itself
            # otherwise, all pairs matched
            print(i_palindrome_i, "is a palindrome")
        else:
            print(i_palindrome_i, " is not a palindrome")
