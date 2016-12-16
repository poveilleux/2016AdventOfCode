#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool is_aba(string data, uint32_t i) {
	return data[i] == data[i + 2]
		&& data[i] != data[i + 1];
}

bool is_bab_of_aba(string aba, string bab) {
	return aba[0] == bab[1]
		&& aba[1] == bab[0];
}

int supports_ssl(string line) {
	bool is_in_hypernet = false;
	vector<string> babs;
	vector<string> abas;

	for (uint32_t i = 0; i < line.size() - 2; ++i) {
		if (is_aba(line, i)) {
			string aba = line.substr(i, 3);
			if (is_in_hypernet) {
				babs.push_back(aba);
			}
			else {
				abas.push_back(aba);
			}
		}
		else if (line[i] == '[') {
			is_in_hypernet = true;
		}
		else if (line[i] == ']') {
			is_in_hypernet = false;
		}
	}
	
	for (auto aba_it = abas.begin(); aba_it != abas.end(); aba_it++) {
		for (auto bab_it = babs.begin(); bab_it != babs.end(); bab_it++) {
			if (is_bab_of_aba(*aba_it, *bab_it)) {
				return 1;
			}
		}
	}

	return 0;
}

int main() {
	ifstream file;
	string line;
	//int nb_tls = 0;
	int nb_ssl = 0;
	int ip_count = 0;

	file.open("data.txt");
	if (file.is_open()) {
		while (!file.eof()) {
			file >> line;
			nb_ssl += supports_ssl(line);
			ip_count++;		
		}

		cout << nb_ssl << " on " << ip_count << " IPs supports TLS" << endl;
	}
	file.close();

	char c;
	cin >> c;
}