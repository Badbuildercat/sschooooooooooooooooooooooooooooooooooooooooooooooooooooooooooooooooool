"""
Uzrakstiet programmu definējot klasi,lai veselu 
skaitli pārveidotu par romiešu ciparu.

"""
"""
list vektor ...
dictionary is a data structure whose elements
 are identified by key

 tabul with 2 colombs with key and value

 ___________________________
|    key             value  |
|___________________________|
|   four               4    |
|   three              3    |
|   two                2    |
|   one                1    |
|___________________________|

empty dictionary {} or ()
full dictionary {...}
with methods fromkeys()   
"""


class AAA:
    def __init__(self):
        self.roman_number={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }
    def to_roman(self, num):
        result="" #define an empty line
        for value, numeral in sorted(self.roman_number.items(), key=lambda x: x[0], reverse=True):
            while num>=value:
                result+=numeral
                num-=value
        return result #define inner function

#piem
number=input("input number to romanize:")
convert = AAA()
roman_number = convert.to_roman(number)
print(f"{number} roman number is {roman_number}")