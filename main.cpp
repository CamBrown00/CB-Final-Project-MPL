#include <fstream>
#include <iostream>
using namespace std;

string getUserInput(string prompt);
string getUserInputInRange(string prompt, int min, int max);
bool writeToFile(string filename, string input);
void clearFile(string filename);

int main() {
    cout << "Welcome to the statistics calculator!" << endl;
    cout << "Please enter the numerical data in the random sample" << endl;
    cout << "Enter any positive or negative number, or 'e' to conclude entering data" << endl;
    string filename = "data.txt";
    clearFile(filename);

    // Get user input for data
    string input;
    while (input != "e") {
        input = getUserInput("Enter the next number (or 'e'): ");
        if (!(input == "e")) {
            if (!writeToFile(filename, input)) {
                cout << "ERROR: " << filename << " could not be written to, terminating program." << endl;
                input = "e";
            }
        }
    }

    // Get user input for choice of graph
    string choice;

    while(choice != "e") {
        cout << "\nWhich graph/chart would you like to display?" << endl;
        cout << "Line graph(1) Pie Chart(2) Histogram(3) Pareto Chart(4) Box-plot(5) End Program(e)" << endl;
        choice = getUserInputInRange("Please enter your choice: ", 5, 1);
        writeToFile(filename, choice);
        if (choice != "e") {
            cout << "\nThe data for the sample has been entered, computing statistics..." << endl;
            system("computeSampleStats.py");
        } else {
            cout << "\nTerminating program, bye!" << endl;
        }
    }

    return 0;
}

string getUserInputInRange(string prompt, int max, int min) {
    // Get numerical input from user within range
    int input = 0;
    string junk;
    cout << prompt;
    while (!(cin >> input) || input > max || input < min) {
        cin.clear();
        getline(cin, junk);
        if (junk == "e") {
            return junk;
        } else {
            cout << "Input data was invalid, please try again:";
        }
    }
    return to_string(input);
}

string getUserInput(string prompt) {
    // Get numerical input from user, return as string
    int answer = 0;
    string junk;
    cout << prompt;
    while (!(cin >> answer)) {
        cin.clear();
        getline(cin, junk);
        if (junk == "e") {
            return junk;
        }
    }
    return to_string(answer);
}

bool writeToFile(string filename, string input) {
    // Write string data to file
    ofstream outFile(filename, ios::app);
    if (outFile) {
        outFile << input << endl;
        outFile.close();
        return true;
    }
    outFile.close();
    return false;
}

void clearFile(string filename) {
    // Close file stream
    ofstream outFile(filename);
    outFile.close();
}