#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

string getUserInput(string prompt);
bool writeToFile(string filename, string input);
void clearFile(string filename);

int main() {
    cout << "Welcome to the statistics calculator!" << endl;
    cout << "Please enter the numerical data in the random sample" << endl;
    cout << "Enter any positive or negative number, or 'e' to conclude entering data" << endl;
    string filename = "../answers.txt";
    clearFile(filename);

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
    cout << "\nWhich graph/chart would you like to display?" << endl;
    cout << "Line graph(1) Pie Chart(2) Histogram(3) Pareto Chart(4) Box-plot(5) End Program(e)" << endl;
    writeToFile(filename, getUserInput("Please enter your choice: "));
    cout << "\nThe data for the sample has been entered, computing statistics..." << endl;

    system("letterHistogram.py");

    return 0;
}

string getUserInput(string prompt) {
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
    ofstream outFile(filename);
    outFile.close();
}