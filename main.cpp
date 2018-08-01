/*! @file flight-control/main.cpp
 *  @version 3.3
 *  @date Jun 05 2017
 *
 *  @brief
 *  main for Flight Control API usage in a Linux environment.
 *  Provides a number of helpful additions to core API calls,
 *  especially for position control, attitude control, takeoff,
 *  landing.
 *
 *  @Copyright (c) 2016-2017 DJI
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 */

// All the important flight control stuff
#include "flight_control_sample.hpp"
using namespace DJI::OSDK;
using namespace DJI::OSDK::Telemetry;

// Headers for reading a text file and waiting in (uint) millsecs
#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>
#include <vector>
#include <sstream>
#include <iterator>
//#include <stdio.h>
//#include <stdlib.h>
//#include <cstring>
using namespace std;

// Set up some global variables and set them to defaults
// TODO: Make this work again, passing args as optional broke em
bool isReading 		= true;
uint timeIn 		= 100000;
string txtFile 		= "example.txt";
string commandString 	= "none";

void doCommand(Vehicle* vehicle)
{
	if (commandString == "takeoff")
	{
		monitoredTakeoff(vehicle);	
		//cout << "Take off stuff would happen now. \n";
	}
	else if (commandString == "land")
	{
		monitoredLanding(vehicle);
		//cout << "Land Stuff would happen now. \n";
	}
	else if (commandString.find("move") != std::string::npos)
	{
		//move stuff
		//cout << "Move Stuff would happen now.\n";
		istringstream iss(commandString);
		vector<string> coords((istream_iterator<string>(iss)), istream_iterator<string>());
		
		moveByPositionOffset(vehicle, stod(coords[1]), stod(coords[2]), stod(coords[3]),stod(coords[4]));
		//cout << "COORDS PASSED: " + coords[1] + coords[2] + coords[3] + coords[4];

	}
	else if (commandString == "exit")
	{
		//cout << "Exit command recieved.";
		isReading = false;
	}
	else
	{
		//default state, so something I guess...
		cout << "Default state reached";
	}	
}


// Function to read in the text file
void readFile()
{
	string line;
	ifstream myfile (txtFile);
   
	if (myfile.is_open())
	{ 
		while ( getline (myfile,line) )
		{ 
			//cout << line << '\n';
			commandString = line;
		}
		myfile.close();
	}

	else cout << "Unable to open file " + txtFile + " will retry on next run.\n";	
}

int main(int argc, char** argv)
{
  	// Initialize variables
  	int functionTimeout = 1;

  	// Setup OSDK.
  	LinuxSetup linuxEnvironment(argc, argv);
  	Vehicle*   vehicle = linuxEnvironment.getVehicle();
	//Vehicle* vehicle = NULL;
  	if (vehicle == NULL)
  	{
    		cout << "Vehicle not initialized, exiting.\n";
		return -1;
	}

	// Obtain Control Authority
	vehicle->obtainCtrlAuthority(functionTimeout);

	// Use this if we wanna pass in default args else just use the defaults
	if (argv[2])
	{
		timeIn = stoul(argv[1]);
		txtFile = argv[2];	
	}	
	
	// Read in instruction sets
	while (isReading)
	{	
		readFile();
		doCommand(vehicle);	
		usleep(timeIn);
		cout << "Staring Next loop read...\n";
	}

  return 0;
}
