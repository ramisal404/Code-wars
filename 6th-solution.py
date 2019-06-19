"""

Convert string to camel case

https://www.codewars.com/kata/517abf86da9663f1d2000003

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

"""

def to_camel_case(text):
    new_text = text.replace("-", "_")
    split_text = new_text.split("_")
    new_text1 = split_text[0:1]
    new_text2 = [word.capitalize() for word in split_text[1:]]
    new_text3 = new_text1 + new_text2
    new_text4 = "".join(new_text3)


    return new_text4
