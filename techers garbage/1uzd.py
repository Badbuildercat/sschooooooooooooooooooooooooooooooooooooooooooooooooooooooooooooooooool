""""
aprēkians fakrtorial un parbaudi vai ir pirmskaitlis
1 kas faktroieals   n  3!=1*2*3 7!=1*2*3*4*5*6*7
2 kast pirmskatlis  dalas tikai ar viens un sevi
3 ko niozimae ievidiet  python ievadi termināli
"""

def faktorials(n):
    rezultats = 1
 
    # Aprēķina faktoriālu, izmantojot ciklu for
    for i in range(1, n + 1):
        rezultats *= i
 
    return rezultats
 
def ir_pirmskaitlis(num):
    # Pārbauda vai skaitlis ir pirmskaitlis, izmantojot ciklu while
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
 
# Ievada skaitlis
n = int(input("Ievadiet veselu pozitīvu skaitli: "))
 
# Pārbauda vai ievadītais skaitlis ir pirmskaitlis
if ir_pirmskaitlis(n):
    print(f"{n} ir pirmskaitlis.")
else:
    print(f"{n} nav pirmskaitlis.")
 
# Aprēķina faktoriālu un izvada rezultātu
print(f"Faktoriāls no {n} ir {faktorials(n)}.")