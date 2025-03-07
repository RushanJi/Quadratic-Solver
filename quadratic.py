import math

a = float(input("\033[31mEnter the coefficient a: \033[0m"))
b = float(input("\033[31mEnter the coefficient b: \033[0m"))
c = float(input("\033[31mEnter the coefficient c: \033[0m"))

# Comment
# * Lighter
# TODO implement inf uture
#! error
# ? query liek a question

while a == 0:
    print("You cant divide by zero. Input a again")
    a = float(input("Enter the coefficient a: "))

discriminant = b**2 - 4*a*c

def radic(n):
    i = 2
    global factor
    factor = 1
    while i * i <= n:
        if n % (i * i) == 0:
            factor *= i
            n //= i * i
        else:
            i += 1
    
    if factor > 1:
        return f"{factor}√{n}"
    else:
        return f"√{n}"
        
def lradic(l):
    i = 2
    global factor
    factor = 1
    while i * i <= l:
        if l % (i * i) == 0:
            factor *= i
            l //= i * i
        else:
            i += 1
    return l
    
    if factor > 1:
        return f"√{l}"
        
def deone(k):
    if k == 1:
        k = ""
        return k
    else:
        return k

def integ(value):
    if value.is_integer():
        return int(value)
    else:
        return value

denominator = 2 * a

if discriminant >= 0:

    print("\n\033[34m========REAL SOLUTIONS========\033[0m")
    print(f"\033[33mSolution 1: \033[0m")
    print(f"= {integ(-b)} + {radic(integ(discriminant))} / {integ(denominator)}")
    print(f"= {integ(-b / denominator)} + {deone(integ(factor / denominator))}{lradic(integ(discriminant))} = {integ(-b / denominator + discriminant**0.5 / denominator)}")

    print(f"\033[33mSolution 2: \033[0m")
    print(f"= {integ(-b)} - {radic(integ(discriminant))} / {integ(denominator)}")
    print(f"= {integ(-b / denominator)} - {deone(integ(factor / denominator))}{lradic(integ(discriminant))} = {integ(-b / denominator - discriminant**0.5 / denominator)}")
    
elif discriminant == 0:
    print("\n\033[34m========SOLUTION========\033[0m")
    print(f"= {integ(-b)} / {integ(denominator)}")
    print(f" = {integ(-b / denominator + discriminant**0.5 / denominator)}")
    
else:

    print("\n\033[34m========COMPLEX SOLUTIONS========\033[0m")
    print(f"\033[33mSolution 1: \033[0m")
    print(f"= {integ(-b)} + {integ(abs(discriminant))}i / {integ(denominator)}")
    print(f"= {integ(-b / denominator)} + {radic(integ(abs(discriminant)))}i")
    print(f"= {integ(-b / denominator)} + {integ(abs(discriminant)**0.5 / denominator)}i")
    
    print(f"\033[33mSolution 2: \033[0m")
    print(f"= {integ(-b)} - {radic(integ(abs(discriminant)))}i / {integ(denominator)}")
    print(f"= {integ(-b / denominator)} - √{deone(integ(factor / denominator))}{lradic(abs(integ(discriminant)))}i")
    print(f"= {integ(-b / denominator)} - {integ(abs(discriminant)**0.5 / denominator)}i")