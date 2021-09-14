
#include <iostream>

using namespace std;

int main()
{
	float side; //Змінна для сторони квадрату
	cout << "Enter side of square:" << endl;
	cin >> side; //Введення сторони квадрату
	float diagonal = sqrt(2 * pow(side, 2)); //Обчислення діагоналі
	float perimeter = 4 * side; //Обчислення периметру
	float area = pow(side, 2); //Обчислення площи
	cout << "Diagonal = " << diagonal << endl; //Виведення результату
	cout << "Perimeter = " << perimeter << endl; //Виведення результату
	cout << "Area = " << area << endl; //Виведення результату
}
