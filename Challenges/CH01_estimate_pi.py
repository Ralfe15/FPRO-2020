import math
import random
import statistics

def monteCarlo(needles):
    needles_in_circle = 0
    for i in range(needles):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if math.sqrt(x**2 + y**2) <= 1:
            needles_in_circle += 1
    pi_estimative = (4*needles_in_circle)/needles
    return pi_estimative

def main(needles):
    estimatives= []
    for i in range(100):
        estimatives.append(monteCarlo(needles))
    currentEstimative = sum(estimatives)/len(estimatives)
    print("Current estimative: {}".format(str(round(currentEstimative,5))))
    print("Current needles ammount: {}".format(str(needles)))
    print("Current std dev: {}\n".format(str(statistics.stdev(estimatives))))
    if statistics.stdev(estimatives) > 0.005:
        needles *= 2
        main(needles)
    else:
        print("=====END=====\n")
        print("Final estimative: {}".format(str(round(currentEstimative,5))))
        print("Final needles ammount: {}".format(str(needles)))
        print("Final std dev: {}\n".format(str(statistics.stdev(estimatives))))