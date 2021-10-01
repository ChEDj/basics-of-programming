
def isosceles_triangle(x, y):
    if x > y:
        if pow(x, 2) == pow(y, 2) * 2: 
            sides = "isosceles"
            angles = "right"
        else:
            sides = "isosceles"
            angles = "obtuse"
    else:
        sides = "isosceles"
        angles = "acute"
    return (sides, angles)

def equilateral_triangle(x, y, z):
    if pow(x, 2) == pow(y, 2) + pow(z, 2):
        sides = "equilateral"
        angles = "right"
    elif pow(x, 2) <= pow(y, 2) + pow(z, 2):
        sides = "equilateral"
        angles = "acute"
    else:
        sides = "equilateral"
        angles = "obtuse"
    return (sides, angles)

a = float(input("Enter a sides of traingle:"))
b = float(input())
c = float(input())
tr_sides = ""
tr_angles = ""

if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
    print("There aren't triangles with such side lengths.")
else:
    if a == b and a == c:
        tr_sides = "equilateral"
        tr_angles = "acute"
    elif a == b:
        tr_sides = isosceles_triangle(c, a)[0]
        tr_angles = isosceles_triangle(c, a)[1]
    elif a == c:
        tr_sides = isosceles_triangle(b, a)[0]
        tr_angles = isosceles_triangle(b, a)[1]
    elif b == c:
        tr_sides = isosceles_triangle(a, b)[0]
        tr_angles = isosceles_triangle(a, b)[1]
    else:
        if a > b and a > c:
            tr_sides = equilateral_triangle(a, b, c)[0]
            tr_angles = equilateral_triangle(a, b, c)[1]
        elif b > a and b > c:
            tr_sides = equilateral_triangle(b, a, c)[0]
            tr_angles = equilateral_triangle(b, a, c)[1]
        else:
            tr_sides = equilateral_triangle(c, b, a)[0]
            tr_angles = equilateral_triangle(c, b, a)[1]
    print("The triangle is", tr_sides , "and", tr_angles)