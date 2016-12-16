#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool is_abba(string data, uint32_t i) {
	return data[i] == data[i + 3] 
		&& data[i + 1] == data[i + 2] 
		&& data[i] != data[i + 1];
}

int supports_tls(string line) {
	int supports_tls = 0;
	bool is_in_hypernet = false;

	for (uint32_t i = 0; i < line.size() - 3; ++i) {
		if (is_abba(line, i)) {
			if (is_in_hypernet) {
				return 0;				
			}
			supports_tls = 1;
		}
		else if (line[i] == '[') {
			is_in_hypernet = true;
		}
		else if (line[i] == ']') {
			is_in_hypernet = false;
		}
	}

	return supports_tls;
}

int main() {
	ifstream file;
	string line;
	int nb_tls = 0;
	int ip_count = 0;

	file.open("data.txt");
	if (file.is_open()) {
		while (!file.eof()) {
			file >> line;
			nb_tls += supports_tls(line);
			ip_count++;
		//http://stackoverflow.com/questions/236129/split-a-string-in-c
		}

		cout << nb_tls << " on " << ip_count << " IPs supports TLS" << endl;
	}
	file.close();

	char c;
	cin >> c;
}