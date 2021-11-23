
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string isosceles_triangle(float x, float y, string& sides, string& angles) {
	if (pow(x, 2) == (pow(y, 2) + pow(y, 2))) {
		sides = "isosceles";
		angles = "right";
	}
	else if(pow(x, 2) > (pow(y, 2) + pow(y, 2))){
		sides = "isosceles";
		angles = "obtuse";
	}
	else {
		sides = "isosceles";
		angles = "acute";
	}
}

string versatile_triangle(float x, float y, float z, string& sides, string& angles) {
	if (pow(x, 2) == pow(y, 2) + pow(z, 2)) {
		sides = "versatile";
		angles = "right";
	}
	else if (pow(x, 2) < pow(y, 2) + pow(z, 2)) {
		sides = "versatile";
		angles = "acute";
	}
	else {
		sides = "versatile";
		angles = "obtuse";
	}
}

int main(){

	float a, b, c;
	string tr_sides, tr_angles;
	cout << "Enter a sides of traingle:";
	cin >> a >> b >> c;

	if (a <= 0 || b <= 0 || c <= 0  || a >= b + c || b >= a + c || c >= a + b) {
		cout << "There aren't triangles with such side lengths.";
	}
	else {
		if (a == b && b == c) {
			tr_sides = "equilateral";
			tr_angles = "acute";
		}
		else if (a == b) {
			isosceles_triangle(c, b, tr_sides, tr_angles);
		}
		else if (a == c) {
			isosceles_triangle(b, a, tr_sides, tr_angles);
		}
		else if (b == c) {
			isosceles_triangle(a, c, tr_sides, tr_angles);
		}
		else {
			if (a > b && a > c) {
				versatile_triangle(a, b, c, tr_sides, tr_angles);
			}
			else if (b > a && b > c) {
				versatile_triangle(b, a, c, tr_sides, tr_angles);
			}
			else if (c > b && c > a) {
				versatile_triangle(c, a, b, tr_sides, tr_angles);
			}
		}
		cout << "The triangle is " << tr_sides << " and " << tr_angles << endl;
	}
}