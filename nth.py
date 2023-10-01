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
    100: "hundredth",
    1000: "thousandth",
}

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

    # get 10th 20th 30th etc from dict
    if n % 10 == 0 and n <= 1000:
        num=ordinal[n]
    
    # generate strings for numbers in tens position
    elif n < 20:
        num=ordinal[n]
    elif n < 30:
        num="twenty-"+ordinal[n%10]
    elif n < 40:
        num="thirty-"+ordinal[n%10]    
    elif n < 50:
        num="forty-"+ordinal[n%10]
    elif n < 60:
        num="fifty-"+ordinal[n%10]
    elif n < 70:
        num="sixty-"+ordinal[n%10]
    elif n < 80:
        num="seventy-"+ordinal[n%10]
    elif n < 90:
        num="eighty-"+ordinal[n%10]
    elif n < 100:
        num="ninety-"+ordinal[n%10]
    elif n < 1000:
        num=f"{cardinal[n // 100]}-hundred {nth(n % 100)}"

# TODO: generate nths for 1000s to millions

# TODO: generate nths for n <= sys.maxsize
    
# but for now just use numerals for big nths
    else:
        if n % 10 == 1:
            num=str(n)+"st"
        elif n % 10 == 2:
            num=str(n)+"nd"
        elif n % 10 == 3:
            num=str(n)+"rd"
        else:
            num=str(n)+"th"
    
    # put the negative sign back if ever it was
    return neg+num

def main():
    number=None
    while number != "done":
        # FIXME: santize input
        number=int(input("Enter a number, or 'done': "))
        # BUG: ValueError for non-integer user input
        print(f"the ordinal of {number} is {(nth(number))}")
    

if __name__ == "__main__":
    main()

