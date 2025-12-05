import numpy as np

# defines the item object, which contains a value and weight
class Item:
    def __init__(self, index, value, weight, cityNumber):
        self.index = int(index)
        self.value = int(value)
        self.weight = int(weight)
        self.cityNumber = int(cityNumber)

# defines the city object, which contains x and y coordinates plus item array
class City: #changed from Node
    def __init__(self, index, x_coord, y_coord):
        self.index = int(index)
        self.x = int(x_coord)
        self.y = int(y_coord)



class FileData: #changed from Dataset
    # loads all of the selected file into memory, in arrays made up of cities and items
    def __init__(self, file):
        
        problemData = []
        
        f = open(file)
        for i in range(9):
            
            tempData = f.readline().split(":")
            
            # extract values from plain text format
            tempVal = tempData[1]
            tempVal = tempVal.translate({ord(i): None for i in '\t'})
            tempVal = tempVal.translate({ord(i): None for i in '\n'})
            
            problemData.append(tempVal)
            
        
        # saves all data values from file as attributes
        self.problemData = problemData
        
        self.fileName = str(problemData[0]) #changed from name
        self.knapsackType = [problemData[1]] #changed from knapsack_type
        self.dimension = int(problemData[2])
        self.numberOfItems = int(problemData[3]) #changed from number_items
        self.knapsackCapacity = int(problemData[4]) #changed from knapsack_capacity
        self.minSpeed = float(problemData[5]) #changed from min_speed
        self.maxSpeed = float(problemData[6]) #changed from max_speed
        self.rentingRatio = float(problemData[7]) #changed from renting_ratio
        self.edgeType = str(problemData[8]) #changed from edge_type
            
        
        f.readline() # skips a line to reach city values
        
        tempCitys = []
        
        # for each city in the file, add it as an object to an array of cities
        for i in range(self.dimension):
            
            # extract values from plain text format
            tempVal = f.readline().translate({ord(i): None for i in '\n'})
            tempVal = tempVal.split("\t")
            
            tempCitys.append(City(tempVal[0], tempVal[1], tempVal[2]))
            
        
        cities = np.array(tempCitys)
        
        
        f.readline() #skips a line to reach item values
        
        tempItems = []
        
        # for each item
        for i in range(self.numberOfItems):
            
            # extract values from plain text format
            tempVal = f.readline().translate({ord(i): None for i in '\n'})
            tempVal = tempVal.split("\t")
            
            tempItems.append(Item(tempVal[0], tempVal[1], tempVal[2], tempVal[3]))
        
        items = np.array(tempItems)
            

        self.cities = cities
        self.items = items
        

# creates a list for the main file to read out of the data gathered from the dataset
def createCityFromData(dataset): #changed from node_coord_section

    cityData = np.zeros((dataset.dimension, 3), dtype=np.float64)
    cityData[:, 0] = [dataset.cities[i].index for i in range(dataset.dimension)]
    cityData[:, 1] = [dataset.cities[i].x for i in range(dataset.dimension)]
    cityData[:, 2] = [dataset.cities[i].y for i in range(dataset.dimension)]

    return cityData
        
# creates a list for the main file to read out of the data gathered from the dataset
def createItemFromData(dataset): #changed from item_section

    itemData = np.zeros((len(dataset.items), 4))
    itemData[:, 0] = [dataset.items[i].index for i in range(dataset.numberOfItems)]  # item indices
    itemData[:, 1] = [dataset.items[i].value for i in range(dataset.numberOfItems)]  # item profits
    itemData[:, 2] = [dataset.items[i].weight for i in range(dataset.numberOfItems)]  # item weights
    itemData[:, 3] = [dataset.items[i].cityNumber for i in
                           range(dataset.numberOfItems)]  # which city each item is in

    return itemData



