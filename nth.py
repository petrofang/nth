""" a Python module to determine the ordinal of a number.

Can be imported as a module or run in stand-alone mode.

Usage:
    nth(n)
"""

# ordinal dictionary for ones and tens places
ordinal = {
    0: "zeroth",
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
    13: "thirteenth",
    14: "fourteenth",
    15: "fifteenth",
    16: "sixteenth",
    17: "seventeenth",
    18: "eighteenth",
    19: "ninteenth",
    20: "twentieth",
    30: "thirtieth",
    40: "fortieth",
    50: "fiftieth",
    60: "sixtieth",
    70: "seventieth",
    80: "eightieth",
    90: "ninetieth",
}

# cardinal dictionary for ones and tens places
cardinal = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
}

def nth(n: int) -> str:
    """ return string ordinal for "nth" of any integer 
    
    usage: nth(n)
    """
    
    # check for and strip negative as needed
    if n < 0:
        neg = "negative "
        n = -n
    else:
        neg = ""

    # determine the length of the number:
    digits=(len(str(n))) 

    # get the number's name by hundreds and thousands
    if digits < 3: num = _sub100(n)
    elif digits < 4: num = _sub1000(n)
    elif digits < 7: num = _subMillion(n)
    else: num = _overMax(n)

    # put the negative sign back if ever it was
    return neg+num

def main():
    number=None
    while number != "done":
        # FIXME: santize input
        number=int(input("Enter a number, or 'done': "))
        # BUG: ValueError for non-integer user input
        print(f"the ordinal of {number} is the {(nth(number))}")

def _sub100(n: int) -> str:
    # get 10th 20th 30th etc from dict
    if n % 10 == 0:
        num=ordinal[n]

    # get numbers under 20 from dict
    elif n < 20:
        num=ordinal[n]

    # generate strings for numbers in tens position
    else:
        num=cardinal[(n // 10)*10]+"-"+ordinal[n%10]
    return num     

def _sub1000(n: int) -> str:
    if n % 100 == 0:
        num=f"{cardinal[n // 100]}-hundredth"
    else:
        num=f"{cardinal[n // 100]}-hundred {nth(n % 100)}"
    return num

def _subMillion(n:int) -> str:
    # TODO: complete this stub function
    return _overMax(n)


def _overMax(n: int) -> str:
    if n % 10 == 1: num=str(n)+"st"
    elif n % 10 == 2: num=str(n)+"nd"
    elif n % 10 == 3: num=str(n)+"rd"
    else: num=str(n)+"th"
    return num

if __name__ == "__main__":
    main()

