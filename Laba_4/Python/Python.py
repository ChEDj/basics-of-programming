
n = 0
while n <= 2:
    n = int(input("Enter n: "))
x = 1
y = 1
xi = 0
yi = 0

for i in range(2, n+1):
    xi = x + (y / i**2)
    yi = y + (x / i)
    x = xi
    y = yi
print("xn =", xi)

