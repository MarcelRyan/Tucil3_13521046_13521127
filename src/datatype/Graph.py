from datatype.Location import *
from utils.parse import *
from utils.haversine import *

class Graph:
    '''
    Class Graph for mapping the map
    '''

    # CONSTRUCTOR
    def __init__(self, filename):
        '''
        locations: list of Location in the map
        adjacencyMatrix: adjacency matrix of locations in map
        '''
        self.locations, self.adjacencyMatrix = parse(filename)
    
    # FIND LOCATION BY NAME
    def findLocation(self, name):
        for location in self.locations:
            if (location.getName() == name):
                return location
    
    # FIND LOCATION BY INDEX
    def findByIndex(self, index):
        return self.locations[index]
    
    # FIND INDEX LOCATION
    def findLocationIndex(self, location):
        for index in range(len(self.locations)):
            if (self.locations[index] == location):
                return index
    
    # SET NEIGHBOUR OF ALL LOCATIONS
    def setNeighbour(self):
        for i in range(len(self.locations)):
            for j in range(len(self.locations)):
                if (self.adjacencyMatrix[i][j] > 0):
                    self.locations[i].addNeighbour(self.locations[j].name)
    
    # Print names of all locations
    def printNames(self):
        for i in range(len(self.locations)):
            print(f'''[{i+1}] {self.locations[i].name}''')
