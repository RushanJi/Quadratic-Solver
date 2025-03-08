import math

print("\033[1m\033[32mEnter the coefficient a: \033[0m", end='')
a = input("\033[1m")
while isinstance(a, str) == True:
    try:
        a = float(a)
    except ValueError:
        print("Give A Valid Value")
        print("\033[1m\033[32mEnter the coefficient a: \033[0m", end='')
        a = input("\033[1m")
print("\033[1m\033[32mEnter the coefficient b: \033[0m", end='')
b = input("\033[1m")
while isinstance(b, str) == True:
    try:
        b = float(b)
    except ValueError:
        print("Give A Valid Value")
        print("\033[1m\033[32mEnter the coefficient b: \033[0m", end='')
        b = input("\033[1m")
print("\033[1m\033[32mEnter the coefficient c: \033[0m", end='')
c = input("\033[1m")
while isinstance(c, str) == True:
    try:
        c = float(c)
    except ValueError:
        print("Give A Valid Value")
        print("\033[1m\033[32mEnter the coefficient c: \033[0m", end='')
        c = input("\033[1m")

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
    
def desqon(op):
    if op == 1:
        return ""
    else:
        return f"√{op}"
        
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
        return f"{h}"
    
def ldiv(oi):
    if oi == 1:
        return ""
    else:
        return f") / {oi}"
    
def cldiv(oi):
    if oi == 1:
        return ""
    else:
        return f" / {oi}"
    
def sldiv(oi):
    if oi == 1:
        return ""
    else:
        return f"("

def absone(he):
    if b == -1:
        return -he
    else:
        return he

def csimpli(le,re):
    gcdl = math.gcd(int(le), int(denominator))
    gcdr = math.gcd(int(re), int(denominator))
    return f"{rdeas(integ(le / gcdl))}{cldiv(integ(round(denominator / gcdl, 4)))}{defactor(integ(round(re / gcdr, 4)))} {sign} \033[1;35m{desqon(lradic(integ(abs(discriminant))))}{cldiv(integ(round(denominator / gcdr, 4)))}i\033[0m"

def simpli(le,re):
    gcdl = math.gcd(int(le), int(denominator))
    gcdr = math.gcd(int(re), int(denominator))
    if gcdl == gcdr:
        if le % gcdr == 0 and re % gcdl == 0 and denominator % gcdr == 1 and denominator % gcdl == 1:
            return f"{rdeas(integ(le / denominator))} {sign} {defactor(integ(round(re / denominator, 4)))}{desqon(lradic(integ(discriminant)))}"
        elif le % gcdr == 0 and re % gcdl == 0 and denominator % gcdr != 1 and denominator % gcdl != 1:
            return f"{ldiv(integ(round(denominator / math.gcd(gcdl, gcdr), 4)))}{rdeas(integ(le / math.gcd(gcdr, gcdl)))} {sign} {defactor(integ(round(re / math.gcd(gcdl, gcdr), 4)))}{desqon(lradic(integ(discriminant)))}{ldiv(integ(round(denominator / math.gcd(gcdl, gcdr), 4)))}"
    else:
        return f"{rdeas(integ(le / gcdl))} {sign} {ldiv(integ(round(denominator / gcdl, 4)))}{defactor(integ(round(re / gcdr, 4)))}{desqon(lradic(integ(discriminant)))}{ldiv(integ(round(denominator / gcdr, 4)))}"

if a !=0 and discriminant > 0:

    print("\n\033[1m\033[34m========REAL SOLUTIONS========\033[0m")
    print(f"\033[1m\033[33mSolution 1: \033[0m")
    sign = "+"
    print(f"\033[1;33m\033[1m{simpli(-b,integ(round(factor, 4)))}\033[0m")
    print(f"\033[1;36m\33[1m= {integ(round(-b / denominator + discriminant**0.5 / denominator, 4))}\033[0m")

    print(f"\033[1m\033[33mSolution 2: \033[0m")
    sign = "-"
    print(f"\033[1;33m\033[1m{simpli(-b,integ(round(factor, 4)))}\033[0m")
    print(f"\033[1;36m\33[1m= {integ(round(-b / denominator - discriminant** 0.5 / denominator, 4))}\033[0m")
    
elif a != 0 and discriminant == 0:
    print("\n\033[1m\033[34m========SOLUTION========\033[0m")
    print(f"\033[1;33m\033[1m= {integ(-b)} / {integ(denominator)}\033[0m")
    print(f"\033[1;36m\33[1m= {integ(round(-b / denominator, 4))}\033[0m")

elif a == 0:
    print("\n\033[1m\033[34m========SOLUTION========\033[0m")
    if a == 0 and b != 0:
        print(f"\033[1;33m\033[1m= {integ(absone(-c))}{cldiv(integ(absone(b)))}\033[0m")
        print(f"\033[1;36m\33[1m= {integ(round(-c / b, 4))}\033[0m")

    elif a == 0 and b == 0 and c != 0:
            print("\33[1mThe equation is contradictory.\033[0m")

    elif a == 0 and b == 0 and c == 0:
        print(f"\033[1m= 0 = 0")
        print(f"\33[1mThere are infinitely many solutions.\033[0m")

else:

    print("\n\033[1m\33[34m========COMPLEX SOLUTIONS========\033[0m")
    if b != 0:
        print(f"\033[1m\033[33mSolution 1: \033[0m")
        sign = "+"
        print(f"\033[1;33m\033[1m{csimpli(-b,integ(round(factor, 4)))}\033[0m")
        print(f"\033[1;36m\33[1m= {rdeas(integ(round(-b / denominator, 4)))} {sign} \033[1;35m{integ(round(abs(discriminant)**0.5 / denominator, 4))}i\033[0m")
        
        print(f"\033[1m\033[33mSolution 2: \033[0m")
        sign = "-"
        print(f"\033[1;33m\033[1m{csimpli(-b,integ(round(factor, 4)))}\033[0m")
        print(f"\033[1;36m\33[1m= {rdeas(integ(round(-b / denominator, 4)))} {sign} \033[1;35m{integ(round(abs(discriminant)**0.5 / denominator, 4))}i\033[0m")
    elif b == 0:
        print(f"\033[1;33m\033[1m{csimpli(-b,integ(round(factor, 4)))}\033[0m")
        print(f"\033[1;36m\33[1m= {rdeas(integ(round(-b / denominator, 4)))} {sign} \033[1;35m{integ(round(abs(discriminant)**0.5 / denominator, 4))}i\033[0m")