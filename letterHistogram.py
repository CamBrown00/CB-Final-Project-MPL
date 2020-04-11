# Import matplotlib so we can graph the data
import matplotlib.pyplot as plt

letterCounts = []
letters = []
for i in range(26):
    letterCounts.append(0)
    letters.append(chr(ord('a') + i))

# Open the txt file
with open('answers.txt') as file:
    for line in file:
        for letter in line:
            if letter.lower() >= 'a' and letter.lower() <= 'z':
                letterCounts[ord(letter.lower())-ord('a')] += 1

print(letterCounts)

# Use matplotlib to graph the data
ax = plt.subplot(111)
# Bar graph
ax.bar(letters, letterCounts)
# Get range of y values to make sure y axis is labeled with integers
yint = range(min(letterCounts), max(letterCounts)+1)
plt.yticks(yint)
# Label graph
plt.gcf().canvas.set_window_title('Letter Histogram')
plt.title('Letter Histogram')
plt.xlabel('Letter')
plt.ylabel('Number of occurrences')
# Display the graph in a new window
plt.show()
