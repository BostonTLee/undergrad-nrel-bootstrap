import pandas as pd
import numpy as np
import matplotlib as plt
import random

from random import sample


# Set random seed for repoducibility
random.seed(400)

# Benchmark 33-Node Test System (https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=25627)
class node:
    def __init__(self, ActiveMean, ReactiveMean, In, Out, TestCase):
        self.ActiveMean = ActiveMean
        self.ActiveSd = ActiveMean * .1
        self.ReactiveMean = ReactiveMean
        self.ReactiveSd = ReactiveMean * .1
        self.In = In
        self.Out = Out
        self.TestCase = TestCase
        self.Voltage = 1

    def getActiveMean(self):
        return self.ActiveMean

    def getActiveSd(self):
        return self.getActiveSd
    
    def getReactiveMean(self):
        return self.ReactiveMean

    def getReactiveSd(self):
        return self.ReactiveSd

    def getInput(self):
        return self.In
    
    def getOutput(self):
        return self.Out

    def getDER(self):
        if self.DER:
            return self.DER
        else:
            return None

    def addDER(self, DER):
        self.DER = DER


# Build lists of Node instances for each test case with Node i stored at index i-1
testCase1 = []
testCase1.append(node(0, 0, None, [2], 1))
testCase1.append(node(100, 60, 1, [3, 19], 1))
testCase1.append(node(90, 40, 2, [4, 23], 1))
testCase1.append(node(120, 80, 3, [5], 1))
testCase1.append(node(60, 30, 4, [6], 1))
testCase1.append(node(60, 20, 5, [7, 26], 1))
testCase1.append(node(200, 100, 6, [8], 1))
testCase1.append(node(200, 100, 7, [9], 1))
testCase1.append(node(60, 20, 8, [10], 1))
testCase1.append(node(60, 20, 9, [11], 1))
testCase1.append(node(45, 30, 10, [12], 1))
testCase1.append(node(60, 35, 11, [13], 1))
testCase1.append(node(60, 35, 12, [14], 1))
testCase1.append(node(120, 80, 13, [15], 1))
testCase1.append(node(60, 10, 14, [16], 1))
testCase1.append(node(60, 20, 15, [17], 1))
testCase1.append(node(60, 20, 16, [18], 1))
testCase1.append(node(90, 40, 17, None, 1))
testCase1.append(node(90, 40, 2, [20], 1))
testCase1.append(node(90, 40, 19, [21], 1))
testCase1.append(node(90, 40, 20, [22], 1))
testCase1.append(node(90, 40, 21, None, 1))
testCase1.append(node(90, 50, 3, [24], 1))
testCase1.append(node(420, 200, 23, [25], 1))
testCase1.append(node(420, 200, 24, None, 1))
testCase1.append(node(60, 25, 6, [27], 1))
testCase1.append(node(60, 25, 26, [28], 1))
testCase1.append(node(60, 20, 27, [29], 1))
testCase1.append(node(120, 70, 28, [30], 1))
testCase1.append(node(200, 600, 29, [31], 1))
testCase1.append(node(150, 70, 30, [32], 1))
testCase1.append(node(210, 100, 31, [33], 1))
testCase1.append(node(60, 40, 32, None, 1))
testCase1 = np.array(testCase1)

testCase2 = []
testCase2.append(node(0, 0, None, [2], 2))
testCase2.append(node(100, 60, 1, [3, 19], 2))
testCase2.append(node(90, 40, 2, [4, 23], 2))
testCase2.append(node(120, 80, 3, [5], 2))
testCase2.append(node(60, 30, 4, [6], 2))
testCase2.append(node(60, 20, 5, [7, 26], 2))
testCase2.append(node(200, 100, 6, [8], 2))
testCase2.append(node(200, 100, 7, [9], 2))
testCase2.append(node(60, 20, 8, [10], 2))
testCase2.append(node(60, 20, 9, [11], 2))
testCase2.append(node(45, 30, 10, [12], 2))
testCase2.append(node(60, 35, 11, [13], 2))
testCase2.append(node(60, 35, 12, [14], 2))
testCase2.append(node(120, 80, 13, [15], 2))
testCase2.append(node(60, 10, 14, [16], 2))
testCase2.append(node(60, 20, 15, [17], 2))
testCase2.append(node(60, 20, 16, [18], 2))
testCase2.append(node(90, 40, 17, None, 2))
testCase2.append(node(90, 40, 2, [20], 2))
testCase2.append(node(90, 40, 19, [21], 2))
testCase2.append(node(90, 40, 20, [22], 2))
testCase2.append(node(90, 40, 21, None, 2))
testCase2.append(node(90, 50, 3, [24], 2))
testCase2.append(node(420, 200, 23, [25], 2))
testCase2.append(node(420, 200, 24, None, 2))
testCase2.append(node(60, 25, 6, [27], 2))
testCase2.append(node(60, 25, 26, [28], 2))
testCase2.append(node(60, 20, 27, [29], 2))
testCase2.append(node(120, 70, 28, [30], 2))
testCase2.append(node(200, 600, 29, [31], 2))
testCase2.append(node(150, 70, 30, [32], 2))
testCase2.append(node(210, 100, 31, [33], 2))
testCase2.append(node(60, 40, 32, None, 2))
testCase2 = np.array(testCase2)

testCase3 = []
testCase3.append(node(0, 0, None, [2], 3))
testCase3.append(node(100, 60, 1, [3, 19], 3))
testCase3.append(node(90, 40, 2, [4, 23], 3))
testCase3.append(node(120, 80, 3, [5], 3))
testCase3.append(node(60, 30, 4, [6], 3))
testCase3.append(node(60, 20, 5, [7, 26], 3))
testCase3.append(node(200, 100, 6, [8], 3))
testCase3.append(node(200, 100, 7, [9], 3))
testCase3.append(node(60, 20, 8, [10], 3))
testCase3.append(node(60, 20, 9, [11], 3))
testCase3.append(node(45, 30, 10, [12], 3))
testCase3.append(node(60, 35, 11, [13], 3))
testCase3.append(node(60, 35, 12, [14], 3))
testCase3.append(node(120, 80, 13, [15], 3))
testCase3.append(node(60, 10, 14, [16], 3))
testCase3.append(node(60, 20, 15, [17], 3))
testCase3.append(node(60, 20, 16, [18], 3))
testCase3.append(node(90, 40, 17, None, 3))
testCase3.append(node(90, 40, 2, [20], 3))
testCase3.append(node(90, 40, 19, [21], 3))
testCase3.append(node(90, 40, 20, [22], 3))
testCase3.append(node(90, 40, 21, None, 3))
testCase3.append(node(90, 50, 3, [24], 3))
testCase3.append(node(420, 200, 23, [25], 3))
testCase3.append(node(420, 200, 24, None, 3))
testCase3.append(node(60, 25, 6, [27], 3))
testCase3.append(node(60, 25, 26, [28], 3))
testCase3.append(node(60, 20, 27, [29], 3))
testCase3.append(node(120, 70, 28, [30], 3))
testCase3.append(node(200, 600, 29, [31], 3))
testCase3.append(node(150, 70, 30, [32], 3))
testCase3.append(node(210, 100, 31, [33], 3))
testCase3.append(node(60, 40, 32, None, 3))
testCase3 = np.array(testCase3)

# Setup Test Case 1 with PV systems distributed in three microgrids
pvNodes = np.concatenate([range(18, 22), range(22, 25), range(25, 33)], axis=None).astype(int)
for pvNode in pvNodes:
    testCase1[pvNode].addDER('pv')

# Setup Test Case 2 with 6 Wind systems and 10 PV systems installed randomly
Nodes = sample(range(33), 16)
pvNodes = Nodes[0:10]
for pvNode in pvNodes:
    testCase2[pvNode].addDER('pv')
windNodes = Nodes[10:15]
for windNode in windNodes:
    testCase2[windNode].addDER('wind')

# Setup Test Case 3 with 21 PV systems and 12 Wind systems installed randomly
Nodes = sample(range(33), 33)
pvNodes = Nodes[0:21]
for pvNode in pvNodes:
    testCase3[pvNode].addDER('pv')
windNodes = Nodes[21:32]
for windNode in windNodes:
    testCase3[windNode].addDER('wind')




