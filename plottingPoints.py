import random
from sys import exit
import matplotlib.pyplot as plt
import math
import numpy as np
import time
# Graphing the circle
theta = np.linspace(0, 2*np.pi, 100)
radius = 1
a = radius*np.cos(theta)+radius
b = radius*np.sin(theta)+radius
figure, axes = plt.subplots(1)
axes.plot(a, b)
axes.set_aspect(1)
xPlot = []
yPlot = []
"""
Rejection Sampling: This method uses a simple algorithm to place the
points within the circle using a traditional cartesian plane.
for each point two random points between 0 and 1 are chosen for the x and
y values. Regularly this would lead to getting a square
distribution. In this case however, points that are over 0.5 units away
(using the distance between 2 2-D points formula) are
rejected and it looks for another point until this condition is met. The
result is an equally distributed plot in the shape of the circle.
"""


def rejectionSampling(n):
    while True:  # This is used to make sure the point is whithin the circle
        x = (random.random()) * 2
        y = (random.random()) * 2
        if (math.sqrt((radius-x)**2+(radius-y)**2)) < radius:
            return (x, y)


def basicPolar(n):
    # Picks a random number for the distance of the point from the origin
    r = random.uniform(0, radius)
    # Picks a random number for the angle of that point around the origin
    angle = random.uniform(0, 2*np.pi)
    return (((r * np.cos(angle))+radius), (r * np.sin(angle)+radius))


def manipulatedPolar(n):
    # Picks a random number for the distance of the point from the origin but squares this value
    r = math.sqrt(random.uniform(0, radius))
    # Picks a random number for the angle of that point around the origin
    angle = random.uniform(0, 2*np.pi)
    return (((r * np.cos(angle))+radius), (r * np.sin(angle)+radius))


def manipulatablePolar(n):
    # Picks a random number for the distance of the point from the origin but squares this value
    r = (random.uniform(0, radius) ** (1.0/n))
    # Picks a random number for the angle of that point around the origin
    angle = random.uniform(0, 2*np.pi)
    return (((r * np.cos(angle))+radius), (r * np.sin(angle)+radius))


def main():
    # Graph selection
    print('Which method would you like to use?\n1: Rejection sampling\n2: Basic Polar method\n3: Uniform Polar\n4: Manipulatable Polar')
    option = int(input())
    if option == 4:
        n = float(input("Which distribution would you like to use? 1 being concentrated to the center and higher numbers being concentrated farther from the center: "))
    else:
        n = None
    points = int(
        input("How many points would you like? Preferably over 3141:"))
    modes = {
        1: rejectionSampling,
        2: basicPolar,
        3: manipulatedPolar,
        4: manipulatablePolar
    }
    if option in modes:
        method = modes[option]
        startTime = time.time()
        for _ in range(points):
            x, y = method(n)
            xPlot.append(x)
            yPlot.append(y)
        endTime = time.time()
        print("Time Elapsed: ", (endTime - startTime))
    else:
        print("Invalid Option")
        exit()
    # Plotting points as a scatter plot
    plt.scatter(xPlot, yPlot, color="red", marker=".", s=5)
    # x-axis label
    plt.xlabel('x axis')
    # frequency label
    plt.ylabel('y axis')
    # plot title
    plt.title('Circle')
    # showing legend
    plt.legend()
    # function to show the plot
    plt.show()


if __name__ == "__main__":
    main()
