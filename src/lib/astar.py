from datatype.Graph import Graph
from datatype.Node import Node
from utils.haversine import haversine
import heapq

def astar(graph: Graph, src: str, dest: str):
    '''
    Function to find shortest path using A* algorithm
    graph : Graph of the map
    src: Source location name
    dest: Destination location name
    '''

    # FIND ALL LOCATIONS NEIGHBOUR
    graph.setNeighbour()

    # GET SOURCE AND DESTINATION LOCATION
    locSrc = graph.findLocation(src)
    locDest = graph.findLocation(dest)
    
    # INITIALIZE PRIORITY QUEUE
    prioqueue = []

    # PUSH THE SOURCE LOCATION TO PRIORITY QUEUE
    heapq.heappush(prioqueue, Node(locSrc, 0, haversine(locSrc, locDest), locSrc.name))

    # SET BOOLEAN FOR CHECKING SO THAT IT WILL NOT CHECK THE SAME LOCATION TWICE
    checked = [0 for _ in range(len(graph.locations))]

    # SET BOOLEAN FOR CHECK CONDITION
    check = True

    while check:
        # DEQUEUE NODE TO CHECK
        checkNode = heapq.heappop(prioqueue)

        # CHECK IF CURRENT NODE IS DESTINATION
        if checkNode.loc == locDest:
            return checkNode
    
        # FIND CURRENT NODE INDEX
        indexCheckNode = graph.findLocationIndex(checkNode.loc)

        # SET CHECKED TO TRUE
        checked[indexCheckNode] = True

        # ITERATE ALL NEIGHBOUR IN CURRENT NODE
        for neighbour in checkNode.loc.neighbour:
            # GET LOCATION OF CURRENT NEIGHBOUR
            locToAdd = graph.findLocation(neighbour)

            # FIND THE INDEX LOCATION FOR CURRENT NEIGHBOUR
            indexToAdd = graph.findLocationIndex(locToAdd)

            # IF NEIGHBOUR HAS NEVER BEEN CHECKED
            if (not checked[indexToAdd]): 
                # CREATE NODE TO BE ADDED TO PRIOQUEUE
                nodeToAdd = Node(locToAdd, haversine(checkNode.loc, locToAdd) + checkNode.g, haversine(locToAdd, locDest), checkNode.route + " " + locToAdd.name)

                # ENQUEUE TO PRIOQUEUE
                heapq.heappush(prioqueue, nodeToAdd)

        # CHECK ENDING CONDITION
        check = (len(prioqueue) != 0 or checkNode.loc != locDest)


