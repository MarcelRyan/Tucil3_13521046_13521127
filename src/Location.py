class Location:
    # CONSTRUCTOR
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    # STRING RETURN FOR DEBUGGING
    def __str__(self):
        return f"{self.name}, {self.latitude}, {self.longitude}"
    
    # GETTER
    def getName(self):
        return self.name
    
    def getLat(self):
        return self.latitude
    
    def getLong(self):
        return self.longitude
    