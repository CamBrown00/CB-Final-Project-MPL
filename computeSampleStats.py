# Import matplotlib so we can graph the data
import matplotlib.pyplot as plt
import math

def main():
    # Read data and choice from file 
    data = []
    data = readIntsFromFile("data.txt")
    choice = data[-1]-1
    del data[-1]
    print("Sample Data: ", end="")
    print(data)

    # Calculate mean, median, mode
    print("Mean: ", end="")
    print(round(calculateMean(data), 4), end="\t")
    print("Median: ", end="")
    print(round(calculateMedian(data), 4), end="\t")
    print("Mode: ", end="")
    print(round(calculateMode(data), 4), end="\t")
    print("\n")

    # Calculate standard deviation, variance
    print("Standard Deviation: ", end="")
    print(round(calculateStandardDeviation(data), 4), end="\t")
    print("Variance: ", end="")
    print(round(calculateVariance(data), 4), end="\t")
    print("\n")

    # Generate graph of choice
    graphFunctions = [generateLineGraph, generatePieChart, generateHistogram]

    if choice < len(graphFunctions) and choice >= 0:
        graphFunctions[choice](data)


def readIntsFromFile(filename):
    # Open the txt file, read into list
    data = []
    with open(filename) as file:
        for line in file:
            line = line.strip("\n")
            data.append(int(line))
    return data

def getFrequencyLists(data):
    # Return lists containing frequencies of values, and each unique value
    values = []
    frequencyList = []
    for value in data:
        if not(value in values):
            values.append(value)
            frequencyList.append(1)
        else:
            frequencyList[values.index(value)]+= 1
    return frequencyList, values

def calculateMean(data):
    # Total values in data, divide by len(data) and return
    total = 0
    for value in data:
        total += value

    return total/len(data)

def calculateMedian(data):
    # Sort data, return value at middle index or average at middle
    median = 0
    tempData = data
    tempData.sort()
    
    if len(data) % 2 != 0:
        median = tempData[math.floor(len(tempData)/2)]
    else:
        median = (tempData[math.floor(len(tempData)/2)] + tempData[math.ceil(len(tempData)/2)])/2

    return median

def calculateMode(data):
    # Return most frequent value in list
    frequencies, values = getFrequencyLists(data)
    return  values[frequencies.index(max(frequencies))]

def calculateStandardDeviation(data):
    # Calculate the sqrt of each value minus the mean, squared, divided by len(data)
    mean = calculateMean(data)
    standardDeviation = 0
    for value in data:
        standardDeviation += (abs(value - mean))**2

    standardDeviation = math.sqrt(standardDeviation/(len(data)-1))
    return standardDeviation

def calculateVariance(data):
    # Calculate the standard deviation squared
    variance = calculateStandardDeviation(data)**2
    return variance

def generateLineGraph(data):
    print(data)
    # Generate line graph using sorted sample data
    tempData = data
    tempData.sort()
    x = [item for item in range(1, len(tempData)+1)]
    y = tempData
    plt.plot(x,y, 'bo')
    plt.plot(x,y)
    plt.xlabel("Value ID's")
    plt.ylabel("Values")
    plt.show()

def generatePieChart(data):
    # Generate pie chart using the value and frequency lists
    frequencies, values = getFrequencyLists(data)
    labels = values
    sizes = frequencies

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')
    plt.show()

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

def generateBoxPlot(data):
    fig1, ax1 = plt.subplots()
    ax1.set_title('Box-Plot of Sample Data')
    ax1.boxplot(data)

main()


