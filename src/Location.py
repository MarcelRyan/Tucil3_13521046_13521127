class Location:
    '''
    Class Location for each location in map
    '''

    # CONSTRUCTOR
    def __init__(self, name, latitude, longitude):
        '''
        name: name of the location
        latitude: latitude of the location
        longtitude: longtitude of the location
        neighbour: list of string, neighbour of the location
        '''
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.weight = dict() # Dictionary of location, untuk menunjukkan weight antar lokasi yang bertetangga dengan lokasi ini
        self.neighbour = []

    # STRING REPRESENTATION OF Location
    def __str__(self):
        return f"{self.name}, {self.latitude}, {self.longitude}"
    
    # GETTER
    def getName(self):
        return self.name
    
    def getLat(self):
        return self.latitude
    
    def getLong(self):
        return self.longitude
    
    def getWeight(self):
        return self.weight
    
    # Key dictionarynya lokasi tetangganya
    def addWeight(self, Loc, weight):
        self.weight[Loc] = weight

    # ADD NEIGHBOUR
    def addNeighbour(self, neighbour):
        self.neighbour.append(neighbour)
        