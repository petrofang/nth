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

# TODO: numbers up to a zillion
# The English names for large numbers are taken 
# from Latin names for small numbers n by adding 
# the ending '-illion' as suggested by 'million.' 
# Thus billion and trillion are from the Latin 
# prefixes bi- (n = 2) and tri- (n = 3). In the 
# US system for naming large numbers, the name
# from the Latin number n applies to the number:
#                             10**(3n+3)
zillion = { # key = how many commas does it have
    2: "m",
    3: "b",
    4: "tr",
    5: "quadr",
    6: "quint",
    7: "sext",
    8: "sept",
    9: "oct",
    10: "non",
    11: "dec",
    12: "undec",
    13: "duodec",
    14: "tredec",
    15: "quattuordec",
    16: "quindec",
    17: "sexdec",
    18: "septendec",
    19: "octodec",
    20: "novemdec",
    21: "vigint",
    22: "unvigint",
    23: "duovigint",
    24: "trevigint",
    25: "quattuorvigint",
    26: "quinvigint",
    27: "sexvigint",
    28: "septenvigint",
    29: "octovigint",
    30: "novemvint",
    31: "trigint",
    32: "unrigint",
    33: "duotrigint",
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
    elif digits < 10: num= _subBillion(n)
    elif digits < 13: num= _subTrillion(n)
    elif digits < 15: num= _subQuad(n)
    else: num = _overMax(n)

    # put the negative sign back if ever it was
    return neg+num

def main():
    number=None
    while True:
        try:
            number=int(input("Enter a number, Ctrl-C to quit: "))
            # BUG: try/except precludes keyboard interrupt
            print(f"\nThe ordinal of {number} is the {(nth(number))}\n")
        except:
            # FIXME: add handler for keyboard interrupt
            print("\n(an integer number)\n")

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
        num=f"{cardinal[n // 100]}-hundred-{nth(n % 100)}"
    return num

def _subMillion(n:int) -> str:
    if n % 1000 == 0:
        num=f"{_cardinal(n // 1000)}-thousandth"
    else:
        num = _cardinal(n//1000) + " thousand " + nth(n % 1000)
    return num

def _subBillion(n:int) -> str:
    if n % 1000000 == 0:
        num=f"{_cardinal(n // 1000000)}-millionth"
    else:
        num = _cardinal(n//1000000) + " million " + nth(n % 1000000)
    return num

def _subTrillion(n:int) -> str:
    if n % 1000000000 == 0:
        num=f"{_cardinal(n // 1000000000)}-billionth"
    else:
        num = _cardinal(n//1000000000) + " billion " + nth(n % 1000000000)
    return num

def _subQuad(n:int) -> str:
    if n % (10**12) == 0:
        num=f"{_cardinal(n // (10**12))}-trillionth"
    else:
        num = _cardinal(n//(10**12)) + " trillion " + nth(n % (10**12))
    return num
        
def _cardinal(n: int) -> str:
    # return cardinal 0 < number < 1000 as string
    # useful for numbers over 1000
    if n % 100 == 0: 
        num=f"{cardinal[n // 100]}-hundred"
    elif n % 10 == 0: 
        if n < 100: num=cardinal[n]
        else:
            num = _cardinal(n//100)+"-hundred-"+cardinal[n%100]
    elif n < 20: 
        num=cardinal[n]
    elif n < 100: 
        num=cardinal[(n // 10)*10]+"-"+cardinal[n%10]
    else: 
        num=f"{_cardinal(n // 100)}-hundred-{_cardinal(n % 100)}"

    return num

def _overMax(n: int) -> str:
    # respond heuristically for numbers over the threshold.
    # exceptions for 11, 12, 13 to avoid 11st 12nd 13rd 
    if (n % 10 == 1) and (n % 100 != 11): num=f"{n:,}st"
    elif (n % 10 == 2) and (n % 100 != 12): num=f"{n:,}nd"
    elif (n % 10 == 3) and (n % 100 != 13): num=f"{n:,}rd"
    else: num=f"{n:,}th"
    return num

if __name__ == "__main__":
    main()

