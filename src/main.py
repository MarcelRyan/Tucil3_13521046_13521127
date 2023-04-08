from graph import Graph
from astar import astar

def main():
    # HEADER
    print('''\n
        =============================================
        UCS and A* Algorithm for Closest Path Finding
        =============================================
    ''')
    
    # INPUT FILENAME
    filename = input("Input filename [name].txt : ")
    graph = Graph(filename)

    # INPUT SOURCE
    source = input('Input source location name : ')
    
    # INPUT DESTINATION
    destination = input('Input destination location name : ')

    # INPUT ALGORITHM CHOICE
    print('''\n
        Algorithm :
        [1] Uniform Cost Search (UCS)
        [2] A*
    ''')
    choice = -1
    while choice < 1 or choice > 2 :
        choice = int(input("Input algorithm choices : "))
    
    # SELECT ALGORITHM
    result = None
    if choice == 1:
        pass
    else :
        result = astar(graph, source, destination)
    
    # PRINT RESULT
    distance = result.f 
    route = result.route.replace(' ', ' - ')
    print(f'''
        ============ RESULT ============
        Filename        : {filename}
        Source          : {source}
        Destination     : {destination}
        Distance (km)   : {distance}
        Route           : {route}
    ''')

if __name__== '__main__':
    main()
