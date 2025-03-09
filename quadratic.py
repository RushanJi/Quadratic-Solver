print("\033[1m\033[32mEnter the coefficient a: \033[0m", end='')
a = input("\033[1m")
while isinstance(a, str):
    try:
        a = float(a)
    except ValueError:
        print("Give A Valid Value")
        print("\033[1m\033[32mEnter the coefficient a: \033[0m", end='')
        a = input("\033[1m")
print("\033[1m\033[32mEnter the coefficient b: \033[0m", end='')
b = input("\033[1m")
while isinstance(b, str):
    try:
        b = float(b)
    except ValueError:
        print("Give A Valid Value")
        print("\033[1m\033[32mEnter the coefficient b: \033[0m", end='')
        b = input("\033[1m")
print("\033[1m\033[32mEnter the coefficient c: \033[0m", end='')
c = input("\033[1m")
while isinstance(c, str):
    try:
        c = float(c)
    except ValueError:
        print("Give A Valid Value")
        print("\033[1m\033[32mEnter the coefficient c: \033[0m", end='')
        c = input("\033[1m")

discriminant = b**2 - 4*a*c

def radic(n):
    if n > 1:
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
    if n < 1:
        i = 2
        factor = 1
        while i * i <= abs(n):
            if abs(n) % (i * i) == 0:
                factor *= i
                n //= i * i
            else:
                i += 1
    
        if factor > 1:
            return f"{factor}√{int(abs(n))}i"
        else:
            return f"√{abs(int(n))}i"
    if n == 1:
        factor = 1
        return f"√1"
    
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
    return ("" if k==1 or k==-1 and lradic != 1 else k)

def integ(value):
    if value.is_integer():
        return int(value)
    else:
        return value
    
def desqon(ip):
    return ("" if ip==1 else f"√{ip}")

def sqone(a,b,c):
    return ("1" if integ(lradic(c)) == 1 and integ(a / b) == 1 else "")

denominator = 2 * a
sign = "±"

def rdeas(h):
    if h == 0:
        return ""
    else:
        return f"{h}"
    
def cldiv(oi):
    if oi == 1:
        return ""
    else:
        return f" / {oi}"

def absone(he):
    if b == -1:
        return -he
    else:
        return he
    
def spcredcr(t,e):
    if integ(t / e) == 0:
        return f"{sign}"
    else:
        return f" {sign} "
    
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def csimpli(le,re):
    gcdl = gcd(int(le), int(denominator))
    gcdr = gcd(int(re), int(denominator))
    if gcdl == denominator and gcdr == denominator:
        if b == 0:
            return f"\033[1;35m{integ(re / denominator)}{desqon(lradic(integ(abs(discriminant))))}i"
        else:
            return f"{integ(le / denominator)} {sign} \033[1;35m{defactor(integ(re / denominator))}{sqone(re, denominator, discriminant)}{desqon(lradic(integ(abs(discriminant))))}i"
    elif gcdl != denominator and gcdr == denominator:
        return f"{integ(le / gcdl)} / {integ(denominator / gcdl)} {sign} \033[1;35m{defactor(integ(re / denominator))}{sqone(re, denominator, discriminant)}{desqon(lradic(integ(abs(discriminant))))}i"
    elif gcdl == denominator and gcdr != denominator:
        return f"{integ(le / denominator)} {sign} \033[1;35m{defactor(integ(re / gcdr))}{sqone(re, gcdr, discriminant)}{desqon(lradic(integ(abs(discriminant))))}i / {integ(denominator / gcdr)}"
    elif gcdl != denominator and gcdr != denominator:
        return f"{integ(le / gcdl)}{cldiv(integ(denominator / gcdl))} {sign} \033[1;35m{defactor(integ(re / gcdr))}{sqone(re, gcdr, discriminant)}{desqon(lradic(integ(abs(discriminant))))}i{cldiv(integ(denominator / gcdr))}"

def simpli(le,re):
    gcdl = gcd(int(le), int(denominator))
    gcdr = gcd(int(re), int(denominator))
    if gcdl == gcdr and re / gcdr != 1 or le / gcdl != 1 and isinstance(re / gcdr, float) == False or isinstance(le / gcdl, float) == False:
        if sign == "+":
            if integ((le / denominator) + round(re / denominator, 4)).is_integer():
                if lradic(discriminant) != 1:
                    return f"{rdeas(integ(le / denominator))}{spcredcr(le, denominator)}{defactor(integ(round(re / denominator, 4)))}{sqone(re, denominator, discriminant)}{desqon(lradic(integ(discriminant)))}"
                else:
                    return f"{integ(le / denominator + round(re / denominator, 4))}"
            else:
                return f"{integ((le + re) / gcd(int(le + re), int(denominator)))}{cldiv(integ(denominator / gcd(int(le + re), int(denominator))))}"
        if sign == "-":
            if integ((le / denominator) - round(re / denominator, 4)).is_integer():
                if lradic(discriminant) != 1:
                    return f"{rdeas(integ(le / denominator))}{spcredcr(le, denominator)}{defactor(integ(round(re / denominator, 4)))}{sqone(re, denominator, discriminant)}{desqon(lradic(integ(discriminant)))}"
                else:
                    return f"{integ(le / denominator - round(re / denominator, 4))}"
            else:
                return f"{integ((le - re) / gcd(int(le - re), int(denominator)))}{cldiv(integ(denominator / gcd(int(le - re), int(denominator))))}"
    else:
        if integ(denominator / gcdl) == integ(denominator / gcdr) and lradic(discriminant) == 1 and (integ(le / gcdl + re / gcdr)) % integ(denominator / gcdl) == 0:
            if sign == "+":
                return f"{integ((le / gcdl + re / gcdr) / gcd(int(le / gcdl + re / gcdr), int(denominator / gcdl)))}{cldiv(integ(denominator / gcdl / gcd(int(le / gcdl + re / gcdr), int(denominator / gcdl))))}"
            if sign == "-":
                return f"{integ((le / gcdl - re / gcdr) / gcd(int(le / gcdl - re / gcdr), int(denominator / gcdl)))}{cldiv(integ(denominator / gcdl / gcd(int(le / gcdl - re / gcdr), int(denominator / gcdl))))}"
        else:
            return f"{integ(le / gcdl)}{cldiv(integ(denominator / gcdl))} {sign} {defactor(integ(re / gcdr))}{sqone(re, gcdr, discriminant)}{desqon(lradic(integ(abs(discriminant))))}{cldiv(integ(denominator / gcdr))}"

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
    if int(-b) % int(denominator) == 0:
        print(f"\033[1;33m\033[1m= {integ(-b / denominator)}\033[0m")
    else:
        print(f"\033[1;33m\033[1m= {integ(-b / gcd(-b, denominator))}{cldiv(integ(denominator / gcd(-b, denominator)))}\033[0m")
    print(f"\033[1;36m\33[1m= {integ(round(-b / denominator, 4))}\033[0m")

elif a == 0:
    print("\n\033[1m\033[34m========SOLUTION========\033[0m")
    if a == 0 and b != 0:
        if -c % b == 0:
            print(f"\033[1;33m\033[1m= {integ(-c / b)}\033[0m")
        else:
            print(f"\033[1;33m\033[1m= {integ((absone(-c)) / gcd(integ(absone(-c)),integ(absone(b))))}{cldiv(integ(absone(b) / gcd(integ(absone(-c)),integ(absone(b)))))}\033[0m")
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
        print(f"\033[1;36m\33[1m= {rdeas(integ(round(-b / denominator, 4)))}{spcredcr(-b, denominator)}\033[1;35m{integ(round(abs(discriminant)**0.5 / denominator, 4))}i\033[0m")
        
        print(f"\033[1m\033[33mSolution 2: \033[0m")
        sign = "-"
        print(f"\033[1;33m\033[1m{csimpli(-b,integ(round(factor, 4)))}\033[0m")
        print(f"\033[1;36m\33[1m= {integ(round(-b / denominator, 4))} {sign} \033[1;35m{integ(round(abs(discriminant)**0.5 / denominator, 4))}i\033[0m")
    elif b == 0:
        print(f"\033[1;33m\033[1m{csimpli(-b,integ(round(factor, 4)))}\033[0m")
        print(f"\033[1m\033[33mSolution 1: \033[0m")
        sign = "+"
        print(f"\033[1;36m\33[1m= {rdeas(integ(round(-b / denominator, 4)))}\033[1;35m{spcredcr(-b, denominator)}{integ(round(abs(discriminant)**0.5 / denominator, 4))}i\033[0m")
        print(f"\033[1m\033[33mSolution 2: \033[0m")
        sign = "-"
        print(f"\033[1;36m\33[1m= {rdeas(integ(round(-b / denominator, 4)))}\033[1;35m{spcredcr(-b, denominator)}{integ(round(abs(discriminant)**0.5 / denominator, 4))}i\033[0m")
