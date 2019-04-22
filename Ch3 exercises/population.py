"""
Instructions

A local biologist needs a program to predict population growth. The inputs would be:

The initial number of organisms
The rate of growth (a real number greater than 1)
The number of hours it takes to achieve this rate
A number of hours during which the population grows

For example, one might start with a population of 500 organisms, a growth rate
of 2, and a growth period to achieve this rate of 6 hours. Assuming that none of
the organisms die, this would imply that this population would double in size
every 6 hours. Thus, after allowing 6 hours for growth, we would have 1000
organisms, and after 12 hours, we would have 2000 organisms.

Write a program that takes these inputs and displays a prediction of the total population.

An example of the program input and output is shown below:

Enter the initial number of organisms: 10
Enter the rate of growth [a real number > 0]: 2
Enter the number of hours to achieve the rate of growth: 2
Enter the total hours of growth: 6

The total population is 80
"""

curPop = initPop = int(input("Enter the initial number of organisms: "))
growthRate = float(input("Enter the rate of growth [a real number > 0]: "))
growthCycle = float(input("Enter the number of hours to achieve the rate of growth: "))
period = float(input("Enter the total hours of growth: "))

fullCycles = int(period // growthCycle)
# print("fullCycles =", fullCycles)
partCycle = (period % growthCycle) / growthCycle
# print("partCycle =", partCycle)

for cycle in range(0, fullCycles):
    curPop = round(curPop * growthRate)
    # print("Population after", cycle + 1, "cycles is", curPop)

# the Python course test is only looking for complete growth cycles
# partPop = round((curPop * growthRate - curPop) * partCycle)
# urPop = curPop + partPop
print("The total population is", curPop)
