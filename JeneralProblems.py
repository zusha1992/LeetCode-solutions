# https://leetcode.com/problems/stone-game-vi/description/
# time complexity : O(nlogn) where n is the size of aliceValues
def stoneGameVI(aliceValues, bobValues):
    data = []
    for i in range(len(aliceValues)):
        data.append([aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]])
    data.sort(reverse=True)

    a, b = 0, 0
    for i in range(len(data)):
        if i % 2 == 0:
            a += data[i][1]
        else:
            b += data[i][2]
    if a > b:
        return 1
    if a < b:
        return -1
    return 0