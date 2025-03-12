GREEN = "\033[1m\033[32m"
BLUE = "\033[1m\033[34m"
YELLOW = "\033[1;33m\033[1m"
PURPLE = "\033[1m\033[1;35m"
CYAN = "\033[1;36m\33[1m"
WHITE = "\033[1m"
STOP = "\033[0m"

print(f"{GREEN}Enter the coefficient a: {STOP}", end='')
a = input(f"{WHITE}")
while isinstance(a, str):
    try:
        a = float(a)
    except ValueError:
        print("Give A Valid Value")
        print(f"{GREEN}Enter the coefficient a: {STOP}", end='')
        a = input(f"{WHITE}")
print(f"{GREEN}Enter the coefficient b: {STOP}", end='')
b = input(f"{WHITE}")
while isinstance(b, str):
    try:
        b = float(b)
    except ValueError:
        print("Give A Valid Value")
        print(f"{GREEN}Enter the coefficient b: {STOP}", end='')
        b = input(f"{WHITE}")
print(f"{GREEN}Enter the coefficient c: {STOP}", end='')
c = input(f"{WHITE}")
while isinstance(c, str):
    try:
        c = float(c)
    except ValueError:
        print("Give A Valid Value")
        print(f"{GREEN}Enter the coefficient c: {STOP}", end='')
        c = input(f"{WHITE}")

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

def defactor(k):
    return ("" if k==1 or k==-1 and lradic != 1 else k)

def integ(value):
    if value.is_integer():
        return int(value)
    else:
        return round(value, 4)
    
def desqon(ip):
    if discriminant > 0:
        return ("" if ip==1 else f"√{ip}")
    elif discriminant < 0:
        return ("" if ip==1 else f"√({ip})")

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
            if sign == "+":
                return f"{PURPLE}{defactor(integ(round(re / denominator , 4)))}{desqon(lradic(integ(abs(discriminant))))}i"
            else:
                return f"{PURPLE}{sign}{defactor(integ(round(re / denominator, 4)))}{desqon(lradic(integ(abs(discriminant))))}i"
        else:
            return f"{integ(round(le / denominator, 4))} {sign} {PURPLE}{defactor(integ(round(re / denominator, 4)))}{desqon(lradic(integ(abs(discriminant))))}i"
    elif gcdl != denominator and gcdr == denominator:
        return f"{integ(round(le / gcdl, 4))} / {integ(round(denominator / gcdl, 4))} {sign} {PURPLE}{defactor(integ(round(re / denominator, 4)))}{desqon(lradic(integ(abs(discriminant))))}i"
    elif gcdl == denominator and gcdr != denominator:
        if sign == "+":
            return f"{rdeas(integ(round(le / denominator, 4)))} {sign} {PURPLE}{defactor(integ(round(re / gcdr)))}{desqon(lradic(integ(abs(discriminant))))}i / {integ(round(denominator / gcdr, 4))}"
        elif sign == "-":
            return f"{integ(round(le / denominator))} {sign} {PURPLE}{defactor(integ(round(re / gcdr)))}{desqon(lradic(integ(abs(discriminant))))}i / {integ(round(denominator / gcdr, 4))}"
    elif gcdl != denominator and gcdr != denominator:
        return f"{integ(round(le / gcdl, 4))}{cldiv(integ(round(denominator / gcdl, 4)))} {sign} {PURPLE}{defactor(integ(round(re / gcdr, 4)))}{desqon(lradic(integ(abs(discriminant))))}i{cldiv(integ(round(denominator / gcdr, 4)))}"

def simpli(le,re):
    gcdl = gcd(int(le), int(denominator))
    gcdr = gcd(int(re), int(denominator))
    if gcdl == gcdr and re / gcdr != 1 or le / gcdl != 1 and isinstance(re / gcdr, float) == False or isinstance(le / gcdl, float) == False:
        if sign == "+":
            if integ((round(le / denominator, 4)) + round(re / denominator, 4)).is_integer():
                if lradic(discriminant) != 1:
                    return f"{rdeas(integ(round(le / denominator, 4)))}{spcredcr(le, denominator)}{defactor(integ(round(re / denominator, 4)))}{sqone(re, denominator, discriminant)}{desqon(lradic(integ(discriminant)))}"
                else:
                    return f"{integ(round(le / denominator + re / denominator, 4))}"
            else:
                if lradic(discriminant) != 1:
                    return f"{rdeas(integ(round(le / denominator, 4)))}{spcredcr(le, denominator)}{defactor(integ(round(re / denominator, 4)))}{sqone(re, denominator, discriminant)}{desqon(lradic(integ(discriminant)))}"
                else:
                    return f"{integ(round((le + re) / gcd(int(le + re), int(denominator)), 4))}{cldiv(integ(round(denominator / gcd(int(le + re), int(denominator)))))}"
        if sign == "-":
            if integ((le / denominator) - round(re / denominator, 4)).is_integer():
                if lradic(discriminant) != 1:
                    return f"{rdeas(integ(round(le / denominator, 4)))}{spcredcr(le, denominator)}{defactor(integ(round(re / denominator, 4)))}{sqone(re, denominator, discriminant)}{desqon(lradic(integ(discriminant)))}"
                else:
                    return f"{integ(round(le / denominator - re / denominator, 4))}"
            else:
                if lradic(discriminant) != 1:
                    return f"{rdeas(integ(round(le / denominator, 4)))}{spcredcr(le, denominator)}{defactor(integ(round(re / denominator, 4)))}{sqone(re, denominator, discriminant)}{desqon(lradic(integ(discriminant)))}"
                else:
                    return f"{integ(round((le - re) / gcd(int(le - re), int(denominator)), 4))}{cldiv(integ(round(denominator / gcd(int(le - re), int(denominator)), 4)))}"
    else:
        if integ(denominator / gcdl) == integ(denominator / gcdr) and lradic(discriminant) == 1 and (integ(le / gcdl + re / gcdr)) % integ(denominator / gcdl) == 0 or (integ(le / gcdl - re / gcdr)) % integ(denominator / gcdl) == 0:
            if sign == "+":
                return f"{integ(round((le / gcdl + re / gcdr) / gcd(int(le / gcdl + re / gcdr), int(denominator / gcdl)), 4))}{cldiv(integ(round(denominator / gcdl / gcd(int(le / gcdl + re / gcdr), int(denominator / gcdl)), 4)))}"
            if sign == "-":
                return f"{integ(round((le / gcdl - re / gcdr) / gcd(int(le / gcdl - re / gcdr), int(denominator / gcdl)), 4))}{cldiv(integ(round(denominator / gcdl / gcd(int(le / gcdl - re / gcdr), int(denominator / gcdl)), 4)))}"
        else:
            return f"{integ(round(le / gcdl, 4))}{cldiv(integ(round(denominator / gcdl, 4)))} {sign} {defactor(integ(round(re / gcdr, 4)))}{sqone(re, gcdr, discriminant)}{desqon(lradic(integ(abs(discriminant))))}{cldiv(integ(round(denominator / gcdr, 4)))}"

if a !=0 and discriminant > 0:

    print(f"\n{BLUE}========REAL SOLUTIONS========{STOP}")
    print(f"{YELLOW}Solution 1: {STOP}")
    sign = "+"
    print(f"{YELLOW}{simpli(-b,integ(round(factor, 4)))}{STOP}")
    print(f"{CYAN}= {integ(round(-b / denominator + discriminant**0.5 / denominator, 4))}{STOP}")

    print(f"{YELLOW}Solution 2: {STOP}")
    sign = "-"
    print(f"{YELLOW}{simpli(-b,integ(round(factor, 4)))}{STOP}")
    print(f"{CYAN}= {integ(round(-b / denominator - discriminant** 0.5 / denominator, 4))}{STOP}")
    
elif a != 0 and discriminant == 0:
    print(f"\n{BLUE}========SOLUTION========{STOP}")
    if -b % denominator == 0:
        print(f"{YELLOW}= {integ(-b / denominator)}{STOP}")
    else:
        print(f"{YELLOW}= {integ(-b / gcd(-b, denominator))}{cldiv(integ(denominator / gcd(-b, denominator)))}{STOP}")
    print(f"{CYAN}= {integ(round(-b / denominator, 4))}{STOP}")

elif a == 0:
    print(f"\n{BLUE}========SOLUTION========{STOP}")
    if a == 0 and b != 0:
        if -c % b == 0:
            print(f"{YELLOW}= {integ(-c / b)}{STOP}")
        else:
            print(f"{YELLOW}= {integ((absone(-c)) / gcd(integ(absone(-c)),integ(absone(b))))}{cldiv(integ(absone(b) / gcd(integ(absone(-c)),integ(absone(b)))))}{STOP}")
        print(f"{CYAN}= {integ(round(-c / b, 4))}{STOP}")

    elif a == 0 and b == 0 and c != 0:
            print(f"{WHITE}The equation is contradictory.{STOP}")

    else:
        print(f"{WHITE}= 0 = 0")
        print(f"{WHITE}There are infinitely many solutions.{STOP}")

else:

    print(f"\n{BLUE}========COMPLEX SOLUTIONS========{STOP}")
    if b != 0:
        print(f"{YELLOW}Solution 1: {STOP}")
        sign = "+"
        print(f"{YELLOW}{csimpli(-b,integ(round(factor, 4)))}{STOP}")
        print(f"{CYAN}= {rdeas(integ(round(-b / denominator, 4)))}{spcredcr(-b, denominator)}{PURPLE}{integ(round(abs(discriminant)**0.5 / denominator, 4))}i{STOP}")
        
        print(f"{YELLOW}Solution 2: {STOP}")
        sign = "-"
        print(f"{YELLOW}{csimpli(-b,integ(round(factor, 4)))}{STOP}")
        print(f"{CYAN}= {integ(round(-b / denominator, 4))} {sign} {PURPLE}{integ(round(abs(discriminant)**0.5 / denominator, 4))}i{STOP}")
    else:
        print(f"{YELLOW}Solution 1: {STOP}")
        sign = "+"
        print(f"{YELLOW}{csimpli(-b,integ(round(factor, 4)))}{STOP}")
        print(f"{CYAN}= {rdeas(integ(round(-b / denominator, 4)))}{PURPLE}{defactor(integ(round(abs(discriminant)**0.5 / denominator, 4)))}i{STOP}")

        print(f"{YELLOW}Solution 2: {STOP}")
        sign = "-"
        print(f"{YELLOW}{csimpli(-b,integ(round(factor, 4)))}{STOP}")
        print(f"{CYAN}= {rdeas(integ(round(-b / denominator, 4)))}{PURPLE}{spcredcr(-b, denominator)}{defactor(integ(round(abs(discriminant)**0.5 / denominator, 4)))}i{STOP}")
