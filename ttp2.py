# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 15:06:11 2025

@author: ew740
"""

import numpy as np
import math




#euclidean_distance to EuclideanDistance
def EuclideanDistance(point1, point2): #Function to find euclidean distance between the 2 given points
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)



#make_distance_matrix to MakeDistanceMatrix
def MakeDistanceMatrix(node_coord_section): #Create a matrix of the distance between cities via euclidean distance function
                                            #Input - node_coord_section : 2D numpy array of cities and their coordinates.
                                            #Returns  distance_matrix : 2D np array of distances between all cities.
   
    number_of_cities = len(node_coord_section) #Use the information from the dataset
    coords_only = node_coord_section[:,1:] #Take just the coordinates from the array

    dist_matrix = np.zeros((number_of_cities, number_of_cities), dtype=np.float64)  #Initilise the distance matrix by creating a square array of zeros 
                                                                                    #with length number_of_cities and 64 bit float data type

    for i in range(number_of_cities):      #Double for loop to fill in distance matrix with euclidean distance coordinates of each city
        for j in range(number_of_cities):
            if(i!=j):
                dist_matrix[i][j] = EuclideanDistance(coords_only[i], coords_only[j])

    return dist_matrix


