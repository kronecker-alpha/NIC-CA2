# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 16:12:20 2025

@author: ew740
"""
#Import necessary tools
import numpy as np
import csv


#Import our modules
import sys
from parsing import Dataset

sys.path.append('../src') #Enable reading from the correct location

#Input filenames of results to be formatted
filename_costs = r"cache/a280-TTP_n279_30_iter_costs_2025-12-05 15-48-04.npy"
filename_population = r"cache/a280-TTP_n279_30_iter_population_2025-12-05 15-48-04.csv"

data_name = "../data/a280-n279.txt" #Load mathcing dataset

#Load costs (time + profit) from npy
fake_costs_extended = np.load(filename_costs)[:, :2]  # only two objectives

#Load population from CSV
population = []
with open(filename_population, "r") as f: #Open the file in read mode
    reader = csv.reader(f)                #Read csv file
    next(reader)  #Skip header row

    for row in reader: #Take desired data 
        tour_str, packing_str = row
        tour = list(map(int, tour_str.split()))
        packing = list(map(int, packing_str.split()))
        population.append((tour, packing))

#Load dataset info
dataset = Dataset.new(open(data_name, 'r').read())


#----- Team 'Kronecker Alpha and the Beta Bois' ------


with open(f"../results/myteam_{dataset.name}.x", "w") as xfile: #Format all relevant data in an x file
    for (tour, packing) in population:
        xfile.write(" ".join(map(str, tour)) + "\n")
        xfile.write(" ".join(map(str, packing)) + "\n\n")


with open(f"../results/myteam_{dataset.name}.f", "w") as ffile: #Format all relevant data in an f file
    for time, profit in fake_costs_extended:
        ffile.write(f"{time} {profit}\n")

print("New files created successfully") 
