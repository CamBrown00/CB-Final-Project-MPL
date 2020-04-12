# Import matplotlib so we can graph the data
import matplotlib.pyplot as plt

def main():
    # Read data and choice from file 
    data = []
    data = readIntsFromFile('answers.txt')
    choice = data[-1]
    del data[-1]

    # Generate graph of choice
    graphFunctions = [generateHistogram]
    print(data)

    if choice < len(graphFunctions) and choice > 0:
        graphFunctions[choice](data)


def readIntsFromFile(filename):
    # Open the txt file, read into list
    data = []
    with open(filename) as file:
        for line in file:
            line = line.strip("\n")
            data.append(int(line))
    return data
                

def generateHistogram(data):
    numbers = []
    numberCounts = []

    for number in data:
        if not(number in numbers):
            numbers.append(number)
            numberCounts.append(1)
        else:
            numberCounts[numbers.index(number)]+= 1
        
    # Use matplotlib to graph the data
    ax = plt.subplot(111)
    # Bar graph
    ax.bar(numbers, numberCounts)
    # Get range of y values to make sure y axis is labeled with integers
    yint = range(min(numberCounts), max(numberCounts)+1)
    plt.yticks(yint)
    # Label graph
    plt.gcf().canvas.set_window_title('Sample Data Histogram')
    plt.title('Sample Data Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    # Display the graph in a new window
    plt.show()

main()


