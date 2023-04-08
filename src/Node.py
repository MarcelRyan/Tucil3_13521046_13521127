class Node:
    '''
    Class Node to be used while finding shortest_path
    '''

    # CONSTRUCTOR
    def __init__(self, loc, g ,h, route):
        '''
        loc: Location of node
        g: distance from source to current node
        h: straight-line from current node to destination
        f: g + h
        route: route used from source to current node
        '''
        self.loc = loc
        self.g = g
        self.h = h
        self.f = g + h
        self.route = route
    
    # OVERRIDE LESS THAN OPERATOR
    def __lt__(self, other):
        return self.f < other.f
    
    # STRING REPRESENTATION OF Node
    def __str__(self):
        return f"{self.loc}, {self.g}, {self.h}, {self.f}, {self.route}"