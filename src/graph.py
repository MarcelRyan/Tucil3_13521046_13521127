from Location import *
from parse import *
from haversine import *

class Graph:
    # Kalau mau ganti gas aja w jg msh blm yakin

    # Locations as vertices and adjacencyMatrix as edges (?)
    def __init__(self, filename):
        self.locations, self.adjacencyMatrix = parse(filename)
    
    # Function to search location with name equal to parameter name
    def findLocation(self, name):
        for location in self.locations:
            if (location.getName() == name):
                return location
    
    # Function to set all weight for location that are neighbors
    def setAllLocationWeight(self):
        for i in range(len(self.locations)):
            for j in range(len(self.locations)):
                if (self.adjacencyMatrix[i][j] == 1):
                    self.locations[i].addWeight(self.locations[j], haversine(self.locations[i], self.locations[j]))
