#include <iostream>
#include <fstream>
#include <string>

int main (int argc, char* argv[]) {
	std::ifstream ifs(argv[1]);  //One call to start it all. . .
	ifs.seekg(-32768, std::ios_base::end);  // One call to find it. . .
	char tmpBuffer[32768];
	ifs.read(tmpBuffer, 32768);  //One call to read it all. . .
	ifs.close();
	std::ofstream ofs("JoeyFirmware.bin", std::ios::trunc);
	ofs.write(tmpBuffer, 32768); //And to the FS bind it.
	
	return 0;
}
