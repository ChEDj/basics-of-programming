
#include <iostream>

using namespace std;

int main()
{
	int n, a;
	cout << "Enter number: ";
	cin >> n; 

	for (int i = 1; i <= 4; i++) {
		a = 0;
		while (pow(a + 1, 2) <= n) {
			a++;
		}
		cout << a << endl;
		n -= pow(a, 2);
	}
}