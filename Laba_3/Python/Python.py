import math 
 
x = 2
while not x < 1 and x > -1:
    x = float(input("Enter x within the interval (-1;1): "))

e = 10**(-6)
n = 0
S = 0
x_n = ((-1)**(n - 1)) * ((2 * n - 1) * x**n) / (math.factorial(2 * n)) 

while not (abs(x_n)) < e:  
    x_n = (-1)**(n - 1) * (2 * n - 1) * x**n / (math.factorial(2 * n))
    n += 1
    S += x_n
    
print("The value of the function for x =", str(x), "is:", round(S, 6)) 
