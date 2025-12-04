"""
Keep the current weight and value as a running total, no need to remove
items that have already been collected, just need a deterministic method to
always pick up the same ones.
"""



class item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    
class city:
    def __init__(self, xCoord, yCoord):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.itemList = []
        
    def addItem(self, item):
        self.itemList.append(item)

# Calculates the current speed of the van as a function of weight
def currentSpeed(vMax, vMin, currentWeight, maxWeight):
    if currentWeight >= maxWeight:
        outputSpeed = vMin
        
    else:
        vTemp = vMax - vMin
        ratio = currentWeight / maxWeight
        
        outputSpeed = vMax - (ratio * vTemp)
        
    return outputSpeed


# Calculates the travel travel based off the current speed and travel distance
def timeToTravel(speed, x1Coord, y1Coord, x2Coord, y2Coord):
    distanceToTravel = ((x1Coord - x2Coord)**2 + (y1Coord - y2Coord)**2)**(1/2)
    timeOutput = distanceToTravel / speed
    
    return timeOutput


# ITEMS SECTION	(INDEX, PROFIT, WEIGHT, ASSIGNED NODE NUMBER):
# NODE_COORD_SECTION	(INDEX, X, Y):
    
coordArray = []
itemArray = []
    
def loadFileIntoMemory(file, coordArray, itemArray):
    
    problemData = []
    ignoreValues = [0, 1, 8]
    
    f = open(file)
    for i in range(9):
        
        tempData = f.readline().split(":")
        
        # extract only necessary values
        if i in ignoreValues:
            continue
        
        # extract values from plain text format
        tempVal = tempData[1]
        tempVal = tempVal.translate({ord(i): None for i in '\t'})
        tempVal = tempVal.translate({ord(i): None for i in '\n'})
        
        # provides an array with (in order):
            # Dimension
            # Number of Items
            # Capacity of Knapsack
            # Min Speed
            # Max Speed
            # Renting Ratio
        problemData.append(float(tempVal))
        
    coordArray = [[0, city(0, 0)]]
    f.readline()
    
    # for each city in the file, add it as an object to an array of cities
    for i in range(int(problemData[0])):
        
        # extract values from plain text format
        tempVal = f.readline().translate({ord(i): None for i in '\n'})
        tempVal = tempVal.split("\t")
        
        coordArray.append([tempVal[0], city(tempVal[1], tempVal[2])])
        
    f.readline()
    
    # for each
    for i in range(int(problemData[1])):
        
        # extract values from plain text format
        tempVal = f.readline().translate({ord(i): None for i in '\n'})
        tempVal = tempVal.split("\t")
        
        # add the respective item to the city with its index
        cityIndex = int(tempVal[3])
        coordArray[cityIndex][1].addItem(item(int(tempVal[1]), int(tempVal[2])))
        

    
    
    return problemData, coordArray

val1, val2 = loadFileIntoMemory("a280-n1395.txt", 0, 0)

print(val1)
print(val2)

print("object at")
temp = val2[280][1].itemList
for i in temp:
    print("value = " + str(i.value) + ", weight = " + str(i.weight))
