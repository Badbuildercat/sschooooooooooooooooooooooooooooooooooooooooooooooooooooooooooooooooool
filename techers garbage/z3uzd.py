"""
Izvadīt visus pirmsskaitļus no 1 līdz 100, izmantojot for un if.
"""

def is_prime_number(number):
    if number<2:
        return False
    for divsion in range(2, int(number**0.5)+1):
        if number% divsion==0:
            return False
    return True
for number in range(1, 101):
    if is_prime_number(number):
        print( number, end= " ")
