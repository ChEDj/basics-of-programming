
n = int(input("Enter a number: "))

for i in range(1, 5):
    a = 0
    while pow(a + 1, 2) <= n:
        a = a + 1
    print(a)
    n = n - pow(a, 2)