import numpy as np

def calcTotalTime(D, Q, vmax, vmin, cityToItemDict, cities):
    """
    Calculates and returns the total travelling time of the thief for a solution in dictionary form.
    D: distance matrix, Q: capacity, vmax/vmin: velocity max and min, 
    cityToItemDict: dictionary with list of items to be picked and their weights, in order of cities to be visited
    cities: list of cities to visit
    """
    total_time = 0
    current_weight = 0 
    n = len(cities)
    
    #for each pair of cities in order
    for i in range(n - 1):
        city_from = cities[i]
        city_to = cities[i + 1]
        
        #get the items to pick from the current city
        items = cityToItemDict[city_from]
        for item in items: 
            current_weight += item[1] #add all the weight of the items to the knapsack
        
        #calculate the velocity based on current knapsack weight
        if current_weight < Q:
           velocity = vmax - (current_weight/Q)*(vmax - vmin)
        else:
           velocity = vmax
        
        distance = D[city_from-1][city_to-1]
        time_to_travel = distance / velocity
        total_time += time_to_travel
    
    # Return the total time
    return total_time


def generateRandomSolution(Q, n, cities, items):
    """
    Generates a random valid solution with random order of cities and items to select.
    Q: capacity, n: number of cities, cities: list of cities, items: 2d item array

  """
    city_tour = np.random.choice(cities, size=n, replace=False) #random list of cities to visit #first city should stay the same?

    weight_array = items[:,2] #array of weights only
    prob = Q / sum(weight_array) #probablity items are selected 

    invalid_sol = True
    items_choice = [] 
    while invalid_sol: #generate list until knapsack is not violated
        items_choice = np.random.choice([0, 1], p=[1 - prob, prob], size=len(items))
        weight = sum(weight_array * items_choice)
        if weight <= Q:
          invalid_sol = False

    return city_tour, items_choice


def calcTimeAndProfit(city_travel, items, items_choice, D, Q, vmax, vmin, R):
    """
    Calculates the total time and profit of a solution in binary form.

    D: distance matrix, Q: capacity, vmax/vmin: velocity max and min, R: renting ratio
    """

    # turn binary item array into a dict so that time can be calculated
    cities_items_dict = {}

    for city in city_travel:
      cities_items_dict[city] = []
      for item in items[:,0]:
        if items_choice[int(item-1)] == 1 and items[int(item-1), 3] == city: # checks if the item has been selected and check if the item is present in the city
          cities_items_dict[city].append((item, items[int(item-1), 2]))

    total_time = calcTotalTime(D, Q, vmax, vmin, cities_items_dict, city_travel)

    #calculate profit
    items_profit = sum(items_choice*items[:, 1])
    net_profit = items_profit - (total_time * R)

    return total_time, net_profit


