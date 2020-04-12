# Import matplotlib so we can graph the data
import matplotlib.pyplot as plt
import math

def main():
    # Read data and choice from file 
    data = []
    data = readIntsFromFile("data.txt")
    choice = data[-1]-1
    del data[-1]
    removeChoice("data.txt")

    # Display sorted data list
    tempData = data
    tempData.sort()
    print("Sorted Data: ", end="")
    print(tempData)

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
    graphFunctions = [generateLineGraph, generatePieChart, generateHistogram, generateParetoChart, generateBoxPlot]

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

def removeChoice(filename):
    readFile = open(filename)
    fileLines = readFile.readlines()
    readFile.close()
    writeFile = open(filename,'w')
    writeFile.writelines([item for item in fileLines[:-1]])
    writeFile.close()

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
    # Generate line graph using sorted sample data
    tempData = data
    tempData.sort()
    x = [item for item in range(1, len(tempData)+1)]
    y = tempData
    plt.gcf().canvas.set_window_title('Sample Data Line Graph')
    plt.title('Sample Data Line Graph')
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
    # Generate box-plot for sample data
    fig1, ax1 = plt.subplots()
    ax1.set_title("Plot of Sample Data")
    ax1.boxplot(data)
    plt.show()

def generateParetoChart(data):
    cumulativeFrequencies = []
    percentages = []
    frequencies, values = getFrequencyLists(data)

    cumulativeFrequency = 0
    totalFrequency = 0
    for frequency in frequencies:
        totalFrequency += frequency

    # Get percentages from frequencies
    for i in range(0, len(frequencies)):
        percentages.append(round(frequencies[i]/totalFrequency, 2) * 100)

    # Get cumulative frequencies
    for percentage in percentages:
        cumulativeFrequency += percentage
        cumulativeFrequencies.append(cumulativeFrequency)
            
    # Reverse data in lists for pareto
    values.sort(reverse = True)
    frequencies.sort(reverse = True)
        
    # Create modified bar-chart
    ax = plt.subplot(111)
    ax.bar(values, frequencies)
    ax.set_xlim(max(values)+1, min(values)-1)
    yint = range(min(frequencies), max(frequencies)+1)
    plt.yticks(yint)
    plt.gcf().canvas.set_window_title("Sample Data Pareto Chart")
    plt.title("Sample Data Pareto Chart")
    plt.xlabel("Value")
    plt.ylabel("Frequency", color="b")
    ax2 = ax.twinx()
    ax2.set_ylabel("Percentage", color="r")
    ax2.set_ylim(0, 100)
    plt.plot(values, cumulativeFrequencies, "ro")
    plt.plot(values, cumulativeFrequencies, "r")
    plt.show()

main()


