#include <fstream>
#include <iostream>
using namespace std;

string getUserChoice(string prompt);
bool writeToFile(string filename, string message);
void clearFile(string filename);

int main() {
    cout << "Welcome to the fun questionnaire!" << endl;
    string filename = "answers.txt";
    if (writeToFile(filename, getUserChoice("What is your favorite color? ")) &&
        writeToFile(filename, getUserChoice("Who do you admire? ")) &&
        writeToFile(filename, getUserChoice("Where would you want to travel? ")) &&
        writeToFile(filename, getUserChoice("Why is the sky blue? ")) &&
        writeToFile(filename, getUserChoice("How do you like your coffee? "))) {
        cout << "Your answers have been recorded! Let's compute some magic." << endl;
        system("letterHistogram.py");
    } else {
        cout << "Oops, something went wrong!" << endl;
    }

    clearFile(filename);

    return 0;
}

string getUserChoice(string prompt) {
    cout << prompt;
    string answer;
    getline(cin, answer);
    return answer;
}

bool writeToFile(string filename, string message) {
    ofstream outFile(filename, ios::app);
    if (outFile) {
        cout << message << endl;
        outFile << message << endl;
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