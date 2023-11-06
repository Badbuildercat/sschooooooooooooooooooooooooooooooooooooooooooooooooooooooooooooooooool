"""
Aprēķināt noteiktas skaitļu summu no 1 līdz n, kur n ir lietotāja ievadīts skaitlis.
"""

n=int(input("gimie numba: "))
sum=0

for numba in range(1, n+1):
    sum+=numba

print(f"number is {n} in {sum}.")