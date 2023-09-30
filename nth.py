"""a module to return the string ordinal (nth) of a number.

Can be included as a module or run as a stand-alone for testing.

Usage:
    nth(n)
"""

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
}

def nth(n: int) -> str:
    """ a function to return the ordinal word for "nth" of any number """
    if n < 0:
        neg = "negative "
        n = -n
    else:
        neg = ""

    if n % 10 == 0 and n <= 100:
        num=ordinal[n]
    
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
    # TODO: Keep going!
    else:
        if n % 10 == 1:
            num=str(n)+"st"
        elif n % 10 == 2:
            num=str(n)+"nd"
        elif n % 10 == 3:
            num=str(n)+"rd"
        else:
            num=str(n)+"th"
    
    return neg+num

def main():
    number=None
    while number != "done":
        # FIXME: 'done' just crashes the program, which also works
        number=int(input("Enter a number, or 'done': "))
        print(f"the ordinal of {number} is {(nth(number))}")
    

if __name__ == "__main__":
    main()

