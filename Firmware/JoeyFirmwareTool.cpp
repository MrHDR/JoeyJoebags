#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <iomanip>

int main (int argc, char* argv[]) {
	std::ifstream ifs(argv[1]);
	ifs.seekg(512, std::ios_base::beg);
	char tmpBuffer[33280];
	ifs.read(tmpBuffer, 32768);
	ifs.close();
	std::ofstream ofs("JoeyFirmware.bin", std::ios_base::binary | std::ios::trunc);
	ofs.write(tmpBuffer, 32768);
	return 0;
}
