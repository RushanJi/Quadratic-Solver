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
    
radicdiscrim = radic(discriminant)
     
def lradic(l):
    i = 2
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
    
def ldiv(oi):
    if oi == 1:
        return ""
    else:
        return f" / {oi}"

def csimpli(le,re):
    gcdv = math.gcd(int(le),int(re), int(denominator))
    if le % gcdv == 0 and re % gcdv == 0 and denominator % gcdv == 1 and denominator / gcdv == 1:
        return f"Simplified = {rdeas(integ(le / gcdv))}{defactor(integ(round(re / gcdv, 4)))}√{lradic(integ(abs(discriminant)))}i"
    elif le % gcdv == 0 and re % gcdv == 0:
        return f"Simplified = ({rdeas(integ(le / gcdv))}{defactor(integ(round(re / gcdv, 4)))}√{lradic(integ(abs(discriminant)))}i){ldiv(integ(round(denominator / gcdv, 4)))}"
    elif gcdv == 1:
        return f"Simplified = {rdeas(integ(le / math.gcd(le, denominator)))}{ldiv(integ(round(denominator / math.gcd(le, denominator), 4)))} {sign} {defactor(integ(round(re / math.gcd(re,denominator), 4)))}√{lradic(integ(abs(discriminant)))}i{ldiv(integ(round(denominator / math.gcd(re, denominator), 4)))}"

def simpli(le,re):
    gcdv = math.gcd(int(le),int(re), int(denominator))
    if le % gcdv == 0 and re % gcdv == 0 and denominator % gcdv == 1 and denominator / gcdv == 1:
        return f"Simplified = {rdeas(integ(le / gcdv))}{defactor(integ(round(re / gcdv, 4)))}√{lradic(integ(discriminant))}"
    elif le % gcdv == 0 and re % gcdv == 0:
        return f"Simplified = ({rdeas(integ(le / gcdv))}{defactor(integ(round(re / gcdv, 4)))}√{lradic(integ(discriminant))}){ldiv(integ(round(denominator / gcdv, 4)))}"
    elif gcdv == 1:
        return f"Simplified = {rdeas(integ(le / math.gcd(le, denominator)))}{ldiv(integ(round(denominator / math.gcd(le, denominator), 4)))} {sign} {defactor(integ(round(re / math.gcd(re,denominator), 4)))}√{lradic(integ(discriminant))}{ldiv(integ(round(denominator / math.gcd(re, denominator), 4)))}"

if a !=0 and discriminant > 0:

    print("\n\033[34m========REAL SOLUTIONS========\033[0m")
    print(f"\033[33mSolution 1: \033[0m")
    sign = "+"
    print(simpli(-b,integ(round(factor, 4))))
    print(f"= {integ(round(-b / denominator + discriminant**0.5 / denominator, 4))}")

    print(f"\033[33mSolution 2: \033[0m")
    sign = "-"
    print(simpli(-b,integ(round(factor, 4))))
    print(f"= {integ(round(-b / denominator - discriminant** 0.5 / denominator, 4))}")
    
elif a != 0 and discriminant == 0:
    print("\n\033[34m========SOLUTION========\033[0m")
    print(f"= {integ(-b)} / {integ(denominator)}")
    print(f"= {integ(round(-b / denominator, 4))}")

elif a == 0:
    print("\n\033[34m========SOLUTION========\033[0m")
    if a == 0 and b != 0:
        print(f"= {integ(-c)} / {integ(b)}")
        print(f"= {integ(round(-c / b, 4))}")

    elif a == 0 and b == 0 and c != 0:
            print("The equation is contradictory.")

    elif a == 0 and b == 0 and c == 0:
        print(f"= 0 = 0")
        print(f"There are infinite possibilities.")

else:

    print("\n\033[34m========COMPLEX SOLUTIONS========\033[0m")
    print(f"\033[33mSolution 1: \033[0m")
    sign = "+"
    print(csimpli(-b,integ(round(factor, 4))))
    print(f"= {rdeas(integ(round(-b / denominator, 4)))}{integ(round(abs(discriminant)**0.5 / denominator, 4))}i")
    
    print(f"\033[33mSolution 2: \033[0m")
    sign = "-"
    print(csimpli(-b,integ(round(factor, 4))))
    print(f"= {rdeas(integ(round(-b / denominator, 4)))}{integ(round(abs(discriminant)**0.5 / denominator, 4))}i")