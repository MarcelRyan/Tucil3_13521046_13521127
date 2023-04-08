from datatype.Graph import Graph
from lib.astar import astar
from lib.ucs import ucs

def main_program():
    # HEADER
    print('''\n
        =============================================
        UCS and A* Algorithm for Closest Path Finding
        =============================================
    ''')
    
    # INPUT FILENAME
    filename = input("Input filename [name].txt : ")
    graph = Graph(filename)

    # PRINT ALL LOCATION NAME AVAILABLE IN FILE
    print(f'''ALL LOCATIONS IN {filename} :''')
    graph.printNames()

    # INPUT SOURCE INDEX
    sourceIndex = int(input('Input source location number : '))
    
    # VALIDATING SOURCE INDEX INPUT
    while (sourceIndex > len(graph.locations)):
        print("Input number based on the location number above")
        sourceIndex = int(input('Input source location number : '))

    
    # INPUT DESTINATION INDEX
    destinationIndex = int(input('Input destination location number : '))

    # VALIDATING DESTINATION INDEX INPUT
    while (destinationIndex > len(graph.locations)):
        print("Input number based on the location number above")
        destinationIndex = int(input('Input destination location number : '))
    
    # GET SOURCE AND DESTINATION LOCATION
    source = graph.locations[sourceIndex-1].name
    destination = graph.locations[destinationIndex-1].name

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
        result = ucs(graph, source, destination)
        distance = result[0]
        route = result[2]
    else :
        result = astar(graph, source, destination)
        distance = result.f 
        route = result.route.replace(' ', ' - ')
    
    # PRINT RESULT
    print(result)
    print(f'''
        ============ RESULT ============
        Filename        : {filename}
        Source          : {source}
        Destination     : {destination}
        Distance (km)   : {distance}
        Route           : {route}
    ''')

    print('''
TO VIEW VISUALIZER:
[1] In web browser go to localhost:5000
[2] Red Point   : Source Location
    Green Point : Destination Location
    Blue Point  : Regular Location
    Blue Line   : Shortest Route from source to destination
    Green Line  : Regular Route
    ''')

    # DATA MANIPULATION FOR VISUALIZING
    shortest_route_name_list = route.split(' - ')

    # CREATE LIST OF ROUTES BETWEEN EACH ADJACENT IN SHORTEST ROUTE NAME LIST
    shortest_routes = []
    for i in range(len(shortest_route_name_list) - 1):
        start_loc = graph.findLocation(shortest_route_name_list[i])
        end_loc = graph.findLocation(shortest_route_name_list[i+1])
        start = (start_loc.getLat(), start_loc.getLong())
        end = (end_loc.getLat(), end_loc.getLong())
        route = [start, end]
        shortest_routes.append(route)
        shortest_routes.append(list(reversed(route)))

    # GET SOURCE AND DESTINATION LOCATION
    source_loc = graph.findLocation(source)
    destination_loc = graph.findLocation(destination)

    return graph.locations, graph.adjacencyMatrix, source_loc, destination_loc, shortest_routes
