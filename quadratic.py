import math

a = input("\033[32mEnter the coefficient a: \033[0m")
while isinstance(a, str) == True:
    try:
        a = float(a)
    except ValueError:
        print("Give A Valid Value")
        a = input("\033[32mEnter the coefficient a: \033[0m")
b = input("\033[32mEnter the coefficient b: \033[0m")
while isinstance(b, str) == True:
    try:
        b = float(b)
    except ValueError:
        print("Give A Valid Value")
        b = input("\033[32mEnter the coefficient b: \033[0m")
c = input("\033[32mEnter the coefficient c: \033[0m")
while isinstance(c, str) == True:
    try:
        c = float(c)
    except ValueError:
        print("Give A Valid Value")
        c = input("\033[32mEnter the coefficient c: \033[0m")

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
        
def defactor(k):
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
sign = "<operator>"

def rdeas(h):
    if h == 0:
        return ""
    else:
        return f"{h} {sign} "

def simpli(le,re):
    gcdv = math.gcd(int(le),int(re), int(denominator))
    if le % gcdv == 0 and re % gcdv == 0 and denominator % gcdv == 1:
        return f"Simplified = {integ(le / gcdv)} {sign} {defactor(integ(round(re / gcdv, 4)))}√{lradic(integ(discriminant))}"
    elif le % gcdv == 0 and re % gcdv == 0:
        return f"Simplified = {integ(le / gcdv)} {sign} {defactor(integ(round(re / gcdv, 4)))}√{lradic(integ(discriminant))} / {integ(round(denominator / gcdv, 4))}"
    
if a !=0 and discriminant >= 0:

    print("\n\033[34m========REAL SOLUTIONS========\033[0m")
    print(f"\033[33mSolution 1: \033[0m")
    sign = "+"
    print(f"= {integ(-b)} + {radic(integ(round(discriminant, 4)))} / {integ(round(denominator, 4))}")
    print(simpli(-b,integ(round(factor, 4))))
    print(f"= {integ(round(-b / denominator + discriminant**0.5 / denominator, 4))}")

    print(f"\033[33mSolution 2: \033[0m")
    sign = "-"
    print(f"= {integ(-b)} - {radic(integ(round(discriminant, 4)))} / {integ(round(denominator, 4))}")
    print(simpli(-b,integ(round(factor, 4))))
    print(f"= {integ(round(-b / denominator - discriminant** 0.5 / denominator, 4))}")
    
elif a != 0 and discriminant == 0:
    print("\n\033[34m========SOLUTION========\033[0m")
    print(f"= {integ(-b)} / {integ(denominator)}")
    print(f" = {integ(round(-b / denominator, 4))}")

elif a == 0:
    print("\n\033[34m========SOLUTION========\033[0m")
    print(f"= {integ(-b)} / {integ(2)}")
    print(f" = {integ(round(-b / 2, 4))}")

else:

    print("\n\033[34m========COMPLEX SOLUTIONS========\033[0m")
    print(f"\033[33mSolution 1: \033[0m")
    sign = "+"
    print(f"= {rdeas(integ(-b))}{radic(integ(abs(discriminant)))}i / {integ(denominator)}")
    print(f"= {rdeas(integ(round(-b / denominator, 4)))}{defactor(integ(round(factor / denominator, 4)))}√{lradic(abs(integ(discriminant)))}i")
    print(f"= {rdeas(integ(round(-b / denominator, 4)))}{integ(round(abs(discriminant)**0.5 / denominator, 4))}i")
    
    print(f"\033[33mSolution 2: \033[0m")
    sign = "-"
    print(f"= {rdeas(integ(-b))}{radic(integ(abs(discriminant)))}i / {integ(denominator)}")
    print(f"= {rdeas(integ(round(-b / denominator, 4)))}{defactor(integ(round(factor / denominator, 4)))}√{lradic(abs(integ(discriminant)))}i")
    print(f"= {rdeas(integ(round(-b / denominator, 4)))}{integ(round(abs(discriminant)**0.5 / denominator, 4))}i")