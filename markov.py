from __future__ import division
from itertools import compress
from itertools import starmap
from operator import mul
import fractions

def convertMatrix(transMatrix):
    probMatrix = []

    for x in range(len(transMatrix)):
        row = transMatrix[x]
        newRow = []
        rowSum = sum(transMatrix[x])

        if all([v == 0 for v in transMatrix[x]]):
            for y in transMatrix[x]:
                newRow.append(0)
            newRow[x] = 1
            probMatrix.append(newRow)

        else:
            for y in transMatrix[x]:
                if y == 0:
                    newRow.append(0)
                else:
                    newRow.append(y / rowSum)
            probMatrix.append(newRow)

    return probMatrix

def terminalStateFilter(matrix):
    terminalStates = []

    for row in range(len(matrix)):
        if all(x == 0 for x in matrix[row]):
            terminalStates.append(True)
        else:
            terminalStates.append(False)

    return terminalStates


def probDistributionVector(matrix, row, timesteps):
    vector = matrix[row]
    for i in range(timesteps):
        newVector = [sum(starmap(mul, zip(vector, col)))
                     for col in zip(*matrix)]
        vector = newVector

    return vector

def gcd(a, b):

    while b:
        a, b = b, a%b
    return a

def solution(m):

    if(len(m) == 1):
        return [1,1]
    
    probMatrix = convertMatrix(m)
    terminalStates = terminalStateFilter(m)
    probVector = probDistributionVector(probMatrix, 0, (len(m)*len(m)))

    numerators = []
    for i in probVector:
        numeratorNum = fractions.Fraction(str(i)).limit_denominator().numerator
        numerators.append(numeratorNum)

    denominators = []
    for i in probVector:
        denominatorNum = fractions.Fraction(str(i)).limit_denominator().denominator
        denominators.append(denominatorNum)


    factors = [max(denominators) // x for x in denominators]
    numeratorsTimesFactors = [a * b for a, b in zip(numerators, factors)]
    terminalStateNumerators = list(compress(numeratorsTimesFactors, terminalStates))

    answers = []
    for i in terminalStateNumerators:
        answers.append(i)

    answers.append(max(denominators))

    return list(answers)

print(solution([
    [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
    [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
    [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
    [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
    [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]))

# [
#     [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
#     [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
#     [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
#     [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
#     [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]