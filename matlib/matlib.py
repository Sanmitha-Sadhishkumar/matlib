'''matlib module gives access to functions that includes additional mathematical functions.
These functions make python programming easier and more effective than before.

'''

__all__=['addinv', 'aprog', 'area_rec', 'area_cir', 'area_cube', 'area_ellipse', 'area_parallelogram',
         'area_rectangular_prism', 'area_sector', 'area_sq', 'area_torus', 'area_trapezium', 'area_tri',
         'aseries', 'composite', 'csa_hcylinder', 'csa_hhemisphere', 'csa_scone', 'csa_scylinder',
         'csa_shemisphere', 'csa_ssphere', 'distance', 'fact', 'fibo', 'gprog', 'gseries', 'hprog', 'hseries', 'ilen',
         'iscomposite', 'iseven', 'isleap', 'isodd', 'isprime', 'midpt', 'mulinv', 'perimeter_cir', 'perimeter_parallelogram',
         'perimeter_rec', 'perimeter_sq', 'perimeter_trapezium', 'perimeter_tri', 'prime', 'reciprocal', 'simint', 'sumeven',
         'sumnat', 'sumodd', 'sumsq', 'tsa_hcylinder', 'tsa_scone', 'tsa_scylinder', 'tsa_shemisphere', 'vol_cube',
         'vol_cuboid', 'vol_ellipsoid', 'vol_frustum', 'vol_hcylinder', 'vol_hhemisphere', 'vol_hsphere', 'vol_pyramid',
         'vol_rectangular_prism', 'vol_scone', 'vol_scylinder', 'vol_shemisphere', 'vol_ssphere', 'vol_torus']

# fact() - gives the factorial of a given number
# input - a integer(upper limit of the factorial)
# output - factorial of the given input
def fact(a):
    if isinstance(a,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if a<0:
            raise ValueError('Input should be positive')
        else:
            f=1
            if f==0:
                print(1) 
            else:
                for i in range(1,a+1):
                    f*=i
                return f

# ilen() - returns the number of digits in the given integer
# input - an integer
# output - the number of digits in the given input
def  ilen(a):
    if isinstance(a,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        b=str(a)
        return len(b)

# simint() - returns the simple interest
# inputs - three (p - principal amount, n - number of years, r - rate 0f interest)
# output - simple interest of given principal amount, number of years and rate 0f interest
def simint(p,n,r):
    a=[]
    a.extend([p,n,r])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (p<0 or n<0) or r<0:
        raise ValueError('Input should be positive')
    else:
        amt=p*n*r
        return amt/100

# distance() - it gives the distance between the given co-ordinates
# inputs - 4(x1, y1, x2, y2)
# output - gives the distance between (x1,y1) and (x2,y2)
def distance(x1,y1,x2,y2):
    a=[]
    a.extend([x1,y1,x2,y2])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    x,y=x2-x1,y2-y1
    disq=(x**2+y**2)
    di=disq**(1/2)
    return di

# midpt() - gives the midpoint of the given pts
# input - 4(x1,y1,x2,y2)
# output - gives the midpoint between (x1,y1) and (x2,y2)
def midpt(x1,y1,x2,y2):
    a=[]
    a.extend([x1,y1,x2,y2])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    x,y=x1+x2,y1+y2
    return (x/2,y/2)

# fibo() - generates a fibonacci series till the upper limit
# input - an integer(upper limit)
# output - Fibonacci series till the upper limit
def fibo(n):
    if isinstance(n,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if n<0:
            raise ValueError('Input should be positive')
        else:
            a,b,c=-1,1,0
            for i in range(n):
                c=a+b
                print(c, end=' ')
                a=b
                b=c
            return '...'

# iseven() - checks whether the given input is even or not
# input - an integer
# output - True/False. Returns True if the given number is even. False otherwise
def iseven(a):
    if isinstance(a,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if a<0:
            raise ValueError('Input should be positive')
        else:
            if a%2==0:
                return True
            else:
                return False

# isodd() - checks whether the given input is odd or not
# input - an integer
# output - True/False. Returns True if the given number is odd. False otherwise
def isodd(a):
    if isinstance(a,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if a<0:
            raise ValueError('Input should be positive')
        else:
            if a%2!=0:
                return True
            else:
                return False


# isleap() - checks whether the given input is a leap year or not
# input - an integer
# output - True/False. Returns True if the given year is leap. False otherwise
def isleap(year):
    if isinstance(year,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if a<0:
            raise ValueError('Input should be positive')
        else:
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return True

# sumnat() - returns the sum of natural numbers upto n terms
# input - an integer(upper limit)
# output - sum to n(upper limit) terms
def sumnat(n):
    if isinstance(n,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if n<0:
            raise ValueError('Input should be positive')
        else:
            a=n*(n+1)
            b=a//2
            return b

# sumeven() - returns the sum of even numbers upto n terms
# input - an integer(upper limit)
# output - sum of even numbers to n(upper limit) terms
def sumeven(n):
    if isinstance(n,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if n<0:
            raise ValueError('Input should be positive')
        else:
            n=n//2
            a=n*(n+1)
            return a

# sumodd() - returns the sum of odd numbers upto n terms
# input - an integer(upper limit)
# output - sum of odd numbers to n(upper limit) terms
def sumodd(n):
    if isinstance(n,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if n<0:
            raise ValueError('Input should be positive')
        else:
            if n%2==0:
                n-=1
            a=0.5
            return (a*(n+1))**2

# sumsq() - returns the sum of squares upto n terms
# input - an integer(upper limit)
# output - sum of squares to n(upper limit) terms
def sumsq(n):
    if isinstance(n,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if a<0:
            raise ValueError('Input should be positive')
        else:
            m,o=n+1,(2*n)+1
            return (n*m*o)/6

# aprog() - returns an arithmetic progression
# inputs - 3(first term, common difference and number of terms)
# output - an arithmetic sequence as per the given first term, common diference and number of terms
def aprog(a,d,n):
    if (((isinstance(a,int) or isinstance(a,float)) and (isinstance(d,int) or isinstance(d,float))) and isinstance(n,int))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if n<0:
            raise ValueError("Number of terms should be positive")
        else:
            for i in range(n):
                print(a+(i*d),end=', ')
            print('...',end='')

# gprog() - returns an geometric progression
# inputs - 3(first term, common ratio and number of terms)
# output - an geometric sequence as per the given first term, common ratio and number of terms
def gprog(a,r,n):
    if (((isinstance(a,int) or isinstance(a,float)) and (isinstance(r,int) or isinstance(r,float))) and isinstance(n,int))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if n<0:
            raise ValueError("Number of terms should be positive")
        else:
            print(a, end=', ')
            for i in range(1,n):
                print(a*(r**i),end=', ')
            print('...',end='')

# hprog() - returns an harmonic progression
# inputs - 3(first term, common difference and number of terms)
# output - an harmonic sequence as per the given first term, common diference and number of terms
def hprog(a,d,n):
    if (((isinstance(a,int) or isinstance(a,float)) and (isinstance(d,int) or isinstance(d,float))) and isinstance(n,int))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if n<0:
            raise ValueError("Number of terms should be positive")
        else:
            for i in range(n):
                print((a+(i*d))**(-1),end=', ')
            print('...',end='')

# aseries() - returns an arithmetic series
# inputs - 3(first term, common difference and number of terms)
# output - the sum of the arithmetic sequence as per the given first term, common diference and number of terms
def aseries(a,d,n):
    if (((isinstance(a,int) or isinstance(a,float)) and (isinstance(d,int) or isinstance(d,float))) and isinstance(n,int))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if n<0:
            raise ValueError("Number of terms should be positive")
        else:
            sum=0
            for i in range(n):
                sum+=a+(i*d)
            return sum

# gseries() - returns an geometric series
# inputs - 3(first term, common ratio and number of terms)
# output - the sum of the geometric sequence as per the given first term, common ratio and number of terms
def gseries(a,r,n):
    if (((isinstance(a,int) or isinstance(a,float)) and (isinstance(r,int) or isinstance(r,float))) and isinstance(n,int))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if n<0:
            raise ValueError("Number of terms should be positive")
        else:
            sum=0
            for i in range(n):
                sum+=a*(r**i)
            return sum

# hseries() - returns an harmonic series
# inputs - 3(first term, common difference and number of terms)
# output - the sum of the harmonic sequence as per the given first term, common diference and number of terms
def hseries(a,d,n):
    if (((isinstance(a,int) or isinstance(a,float)) and (isinstance(d,int) or isinstance(d,float))) and isinstance(n,int))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if n<0:
            raise ValueError("Number of terms should be positive")
        else:
            sum=0
            for i in range(n):
                sum+=(a+(i*d))**(-1)
            return sum

# reciprocal() - returns the reciprocal of the given input
# input - an integer other than zero
# output - reciprocal of the given input
def reciprocal(a):
    if (isinstance(a,int) or isinstance(a,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        return (1/a)

# addinv() - returns the additive inverse of the given input
# input - an integer
# output - additive inverse of the given input
def addinv(a):
    if (isinstance(a,int) or isinstance(a,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        return (-a)

# mulinv() - returns the multiplicative inverse of the given input
# input - an integer other than zero
# output - multiplicative inverse of the given input
def mulinv(a):
    if (isinstance(a,int) or isinstance(a,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        return (1/a)

# isprime() - checks whether the given input is prime or not
# input - an integer
# output - True/False. Returns True if the given number is prime. False otherwise
def isprime(a):
    if isinstance(a,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if a==0 or a==1:
            return False
        for i in range(2,a):
            if a%i==0:
                return False
        else:
            return True

# iscomposite() - checks whether the given input is composite or not
# input - an integer
# output - True/False. Returns True if the given composite is even. False otherwise
def iscomposite(a):
    if isinstance(a,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        if a==0 or a==1:
            return False
        for i in range(2,a):
            if a%i==0:
                return True
        else:
            return False

# prime() - returns the sequence of prime numbers till the upper limit
# input - an integer(upper limit)
# output - a sequence of prime numbers till the upper limit
def prime(a):
    if isinstance(a,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        p=[]
        for i in range(2,a):
            for j in range(2,i):
                 if i%j==0:
                     break
            else:
                p.append(i)
        return p

# composite() - returns the sequence of composite numbers till the upper limit
# input - an integer(upper limit)
# output - a sequence of composite numbers till the upper limit
def composite(a):
    if isinstance(a,int)==False:
        raise TypeError("Invalid inputs for type 'int'")
    else:
        p,u=[],{x for x in range(2,a+1)}
        for i in range(2,a):
            for j in range(2,i):
                 if i%j==0:
                     break
            else:
                p.append(i)
        return list(u-set(p))

# perimeter_sq() - gives the perimeter of the square
# input - an integer(side of the square)
# output - perimeter using the given side
def perimeter_sq(s):
    if (isinstance(s,int) or isinstance(s,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if s<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            return 4*s

# perimeter_rec() - gives the perimeter of the rectangle
# inputs - two integers(length and breadth of the rectangle)
# output - perimeter using the given length and breadth
def perimeter_rec(l,b):
    a=[]
    a.extend([l,b])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if l<0 or b<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        return 2*(l+b)

# perimeter_parallelogram() - gives the perimeter of the parallelogram
# inputs - two integers(length and width of the rectangle)
# output - perimeter using the given length and width
def perimeter_parallelogram(l,w):
    a=[]
    a.extend([l,w])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (l<0 or w<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        return 2*(l+w)

# perimeter_tri() - gives the perimeter of the triangle
# inputs - three integers(sides of the triangle)
# output - perimeter using the given sides
def perimeter_tri(a,b,c):
    d=[]
    d.extend([a,b,c])
    for i in d:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (a<0 or b<0) or c<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        return a+b+c

# perimeter_trapezium() - gives the perimeter of the trapezium
# inputs - three integers(height, base1 and base2 of trapezium)
# output - perimeter using the given height, base1 and base2
def perimeter_trapezium(a,b,c,d):
    a1=[]
    a1.extend([a,b,c,d])
    for i in a1:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (a<0 or b<0) or (c<0 or d<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        return a+b+c+d

# perimeter_cir() - gives the perimeter of the circle
# inputs - an integer(radius of the circle)
# output - perimeter using the given circle
def perimeter_cir(r):
    if (isinstance(r,int) or isinstance(r,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if r<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            pi=22/7
            return 2*pi*r

# area_tri() - gives the area of the triangle
# inputs - two integers(base and height of the triangle)
# output - area using the given base and height
def area_tri(b,h):
    a=[]
    a.extend([b,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (b<0 or h<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        return 0.5*b*h

# area_sq() - gives the area of the square
# inputs - an integer(side of the square)
# output - area using the given side
def area_sq(a):
    if (isinstance(a,int) or isinstance(a,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if a<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            return a**2

# area_rec() - gives the area of the rectangle
# inputs - two integers(length and breadth of the rectangle)
# output - area using the given length and breadth
def area_rec(l,b):
    a=[]
    a.extend([l,b])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (l<0 or b<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        return l*b

# area_cir() - gives the area of the circle
# inputs - an integer(radius of the circle)
# output - area using the given radius
def area_cir(r):
    if (isinstance(r,int) or isinstance(r,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if r<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            pi=22/7
            return pi*(r**2)

# area_sector() - gives the area of the sector
# inputs - two integers(theta(angle) and radius of the sector)
# output - area using the given angle and radius
def area_sector(theta,r):
    a=[]
    a.extend([theta,r])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (theta<0 or r<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        pi=22/7
        t=theta/360
        return pi*(r**2)*t

# area_parallelogram() - gives the area of the parallelogram
# inputs - two integers(base and width of the parallelogram)
# output - area using the given base and width
def area_parallelogram(b,w):
    a=[]
    a.extend([b,w])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (b<0 or w<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        return b*w

# area_trapezium() - gives the area of the trapezium
# inputs - three integers(height, base1 and base2 of the trapezium)
# output - area using the given height, base1 and base2
def area_trapezium(h,b1,b2):
    a=[]
    a.extend([h,b1,b2])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (h<0 or b1<0) or b2<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        t=b1+b2
        return h*(t/2)

# area_ellipse() - gives the area of the ellipse
# inputs - two integers(radius1 and radius2 of the ellipse)
# output - area using the given radius1 and radius2
def area_ellipse(a,b):
    d=[]
    d.extend([a,b])
    for i in d:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (a<0 or b<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        pi=22/7
        return pi*a*b

# area_cube() - gives the area of the cube
# inputs - an integer(side of the cube)
# output - area using the given side
def area_cube(a):
    if (isinstance(a,int) or isinstance(a,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if a<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            return 6*(a**2)

# area_rectangular_prism() - gives the area of the rectangular_prism
# inputs - three integers(width, length and height of the rectangular_prism)
# output - area using the given width, length and height
def area_rectangular_prism(w,l,h):
    a=[]
    a.extend([w,l,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (w<0 or l<0) or h<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        return 2*((w*l)+(h*l)+(h*w))

# area_torus() - gives the area of the torus
# inputs - two integers(radius1 and radius2 of the torus)
# output - area using the given radius1 and radius2
def area_torus(r1,r2):
    a=[]
    a.extend([r1,r2])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (r1<0 or r2<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        pi=22/7
        return (pi**2)*((r2**2)-(r1**2))

# vol_cube() - gives the volume of the cube
# inputs - an integer(side of a cube)
# output - area using the given side
def vol_cube(a):
    if (isinstance(a,int) or isinstance(a,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if a<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            return a**3

# vol_cuboid() - gives the volume of the cuboid
# inputs - three integers(length, breadth and height)
# output - volume using the given length, breadth and height
def vol_cuboid(l,b,h):
    a=[]
    a.extend([l,b,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (l<0 or b<0) or h<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        return l*b*h

# vol_rectangular_prism() - gives the volume of the rectangular_prism
# inputs - three integers(side1, side2 and side3)
# output - volume using the given side1, side2 and side3
def vol_rectangular_prism(s1,s2,s3):
    a=[]
    a.extend([s1,s2,s3])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (s1<0 or s2<0) or s3<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        return s1*s2*s3

# vol_ellipsoid() - gives the volume of the ellipsoid
# inputs - three integers(radius1, radius2 and radius3)
# output - volume using the given radius1, radius2 and radius3
def vol_ellipsoid(r1,r2,r3):
    a=[]
    a.extend([r1,r2,r3])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (r1<0 or r2<0) or r3<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        a=4/3
        pi=22/7
        return a*pi*r1*r2*r3

# vol_pyramid() - gives the volume of the pyramid
# inputs - two integers(base area and height)
# output - volume using the given base area and height
def vol_pyramid(barea,h):
    a=[]
    a.extend([barea,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (barea<0 or h<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        a=1/3
        return a*barea*h

# vol_torus() - gives the volume of the torus
# inputs - two integers(radius1 and radius2)
# output - volume using the given radius1 and radius2
def vol_torus(r1,r2):
    a=[]
    a.extend([r1,r2])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (r1<0 or r2<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        a=1/4
        pi=22/7
        return (a*(pi**2)*(r1+r2)*((r1-r2)**2))

# csa_scylinder() - gives the curved surface area of the solid cylinder
# inputs - two integers(radius and height)
# output - curved surface area using the given radius and height
def csa_scylinder(r,h):
    a=[]
    a.extend([r,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (r<0 or h<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        pi=22/7
        return 2*pi*r*h

# tsa_scylinder() - gives the total surface area of the solid cylinder
# inputs - two integers(radius and height)
# output - total surface area using the given radius and height
def tsa_scylinder(r,h):
    a=[]
    a.extend([r,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (r<0 or h<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        pi=22/7
        return 2*pi*r*(r+h)

# vol_scylinder() - gives the volume of the solid cylinder
# inputs - two integers(radius and height)
# output - volume using the given radius and height
def vol_scylinder(r,h):
    a=[]
    a.extend([r,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (r<0 or h<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        pi=22/7
        return pi*(r**2)*h

# csa_hcylinder() - gives the curved surface area of the hollow cylinder
# inputs - three integers(outer radius, inner radius and height)
# output - curved surface area using the given outer radius, inner radius and height
def csa_hcylinder(R,r,h):
    a=[]
    a.extend([R,r,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (R<0 or r<0) or h<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        if r>R:
            raise ValueError('Outer radius smaller than inner radius')
        else:
            pi=22/7
            return 2*pi*(R+r)*h

# tsa_hcylinder() - gives the total surface area of the hollow cylinder
# inputs - three integers(outer radius, inner radius and height)
# output - total surface area using the given outer radius, inner radius and height
def tsa_hcylinder(R,r,h):
    a=[]
    a.extend([R,r,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (R<0 or r<0) or h<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        if r>R:
            raise ValueError('Outer radius smaller than inner radius')
        else:
            pi=22/7
            return 2*pi*(R+r)*(R-r+h)

# vol_hcylinder() - gives the volume of the solid cylinder
# inputs - two integers(radius and height)
# output - volume using the given radius and height
def vol_hcylinder(R,r,h):
    a=[]
    a.extend([R,r,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (R<0 or r<0) or h<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        if r>R:
            raise ValueError('Outer radius smaller than inner radius')
        else:
            pi=22/7
            return pi*h*((R**2)-(r**2))

# csa_scone() - gives the curved surface area of the solid cone
# inputs - two integers(radius and slant height)
# output - curved surface area using the given radius and slant height
def csa_scone(r,l):
    a=[]
    a.extend([r,l])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (r<0 or l<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        pi=22/7
        return pi*r*l

# tsa_scone() - gives the total surface area of the solid cone
# inputs - two integers(radius and slant height)
# output - total surface area using the given radius and slant height
def tsa_scone(r,l):
    a=[]
    a.extend([r,l])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (r<0 or l<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        pi=22/7
        return pi*r*(l+r)

# vol_scone() - gives the volume of the solid cone
# inputs - two integers(radius and slant height)
# output - volume using the given radius and slant height
def vol_scone(r,l):
    a=[]
    a.extend([r,l])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (r<0 or l<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        pi=22/7
        h=((l**2)-(r**2))**0.5
        return 1/3*pi*(r**2)*h

# vol_frustum() - gives the volume of the frustum
# inputs - two integers(outer radius and inner radius)
# output - volume using the given outer radius and inner radius
def vol_frustum(R,r,h):
    a=[]
    a.extend([R,r,h])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (R<0 or r<0) or h<0:
        raise ValueError('Inputs for measurement should be positive')
    else:
        if r>R:
            raise ValueError('Outer radius smaller than inner radius')
        else:
            pi=22/7
            return 1/3*pi*h*((R**2)+(r**2)+(R*r))

# csa_ssphere() - gives the curved surface area of the solid sphere
# inputs - an integer(radius)
# output - curved surface area using the given radius
def csa_ssphere(r):
    if (isinstance(r,int) or isinstance(r,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if r<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            pi=22/7
            return 4*pi*(r**2)

# vol_ssphere() - gives the volume of the solid sphere
# inputs - an integer(radius)
# output - volume using the given radius
def vol_ssphere(r):
    if (isinstance(r,int) or isinstance(r,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if r<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            pi=22/7
            return 4/3*pi*(r**3)

# vol_hsphere() - gives the volume of the hollow sphere
# inputs - an integer(radius)
# output - volume using the given radius
def vol_hsphere(R,r):
    a=[]
    a.extend([R,r])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (R<0 or r<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        if r>R:
            raise ValueError('Outer radius smaller than inner radius')
        else:
            pi=22/7
            return 4/3*pi*((R**3)-(r**3))

# csa_shemisphere() - gives the curved surface area of the solid hemisphere
# inputs - an integer(radius)
# output - curved surface area using the given radius
def csa_shemisphere(r):
    if (isinstance(r,int) or isinstance(r,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if r<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            pi=22/7
            return 2*pi*(r**2)

# tsa_shemisphere() - gives the total surface area of the solid hemisphere
# inputs - an integer(radius)
# output - total surface area using the given radius
def tsa_shemisphere(r):
    if (isinstance(r,int) or isinstance(r,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if r<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            pi=22/7
            return 3*pi*(r**2)

# vol_shemisphere() - gives the volume of the solid hemisphere
# inputs - an integer(radius)
# output - volume using the given radius
def vol_shemisphere(r):
    if (isinstance(r,int) or isinstance(r,float))==False:
        raise TypeError("Invalid inputs for type 'int' or 'float'")
    else:
        if r<0:
            raise ValueError('Inputs for measurement should be positive')
        else:
            pi=22/7
            return 2/3*pi*(r**3)

# csa_hhemisphere() - gives the curved surface area of the hollow hemisphere
# inputs - an integer(radius)
# output - hollow surface area using the given radius
def csa_hhemisphere(R,r):
    a=[]
    a.extend([R,r])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (R<0 or r<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        if r>R:
            raise ValueError('Outer radius smaller than inner radius')
        else:
            pi=22/7
            return 2*pi*((R**2)-(r**2))

# tsa_hhemisphere() - gives the curved surface area of the hollow hemisphere
# inputs - an integer(radius)
# output - total surface area using the given radius
def tsa_hhemisphere(R,r):
    a=[]
    a.extend([R,r])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (R<0 or r<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        if r>R:
            raise ValueError('Outer radius smaller than inner radius')
        else:
            pi=22/7
            return pi*(((3*R)**2)+(r**2))

# vol_hhemisphere() - gives the volume of the hollow hemisphere
# inputs - an integer(radius)
# output - volume using the given radius
def vol_hhemisphere(R,r):
    a=[]
    a.extend([R,r])
    for i in a:
        if isinstance(i,int) or isinstance(i,float):
            break
        else:
            raise TypeError("Invalid inputs for type 'int' or 'float'")
    if (R<0 or r<0):
        raise ValueError('Inputs for measurement should be positive')
    else:
        if r>R:
            raise ValueError('Outer radius smaller than inner radius')
        else:
            pi=22/7
            return 2/3*pi*((R**3)-(r**3))
