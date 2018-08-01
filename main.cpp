// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>
using namespace std;

bool isReading = true;
uint timeIn = 10000000;
string txtFile = "example.txt";

void readFile()
{
	string line;
	ifstream myfile (txtFile);
   
	if (myfile.is_open())
	{ 
		while ( getline (myfile,line) )
		{ 
			cout << line << '\n';
			if (line == "exit")
			{
				isReading = false;
			}	
		}
		myfile.close();
	}

	else cout << "Unable to open file";	
}

int main (int argc, char** argv) {

	if (argv[1])
	{
		txtFile = argv[1];
		timeIn = stoul(argv[2]);	
	}	

	while (isReading)
	{	
		readFile();	
		usleep(timeIn);
		cout << "Waited 10 seconds I think...";
	}	

	return 0;
}
