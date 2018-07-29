#include<stdio.h>
#include<regex>
#include<string>
#include<iostream>

using namespace std;

int main() {

	string str;
	getline(cin, str);
	cout << str << endl;
	bool rs = false;
	string pattern = {"(((([0-9]+)(,)([0-9]+)(\\s)([0-9]+)(,)([0-9]+)(;))+)(([0-9]+)(,)([0-9]+)(\\s)([0-9]+)(,)([0-9]+)$))|(([0-9]+)(,)([0-9]+)(\\s)([0-9]+)(,)([0-9]+)$)"};
	regex re(pattern);
	rs = regex_match(str,re);

	if (rs) {
		cout << str << " is valid" << endl;
	}
	else {
		cout << str << " is not valid" << endl;
	}
	system("pause");
}