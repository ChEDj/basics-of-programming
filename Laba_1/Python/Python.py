
import math
side = float(input("Enter a side of squeare: ")) #Введення сторони квадрату
diagonal = math.sqrt(2 * math.pow(side, 2))#Обчислення діагоналі
perimeter = 4 * side #Обчислення периметру
area = math.pow(side, 2) #Обчислення площи
print("Diagonal =", diagonal) #Виведення результату
print("Perimeter =", perimeter) #Виведення результату
print("Area =", area) #Виведення результату
