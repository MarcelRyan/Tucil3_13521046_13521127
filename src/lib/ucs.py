from datatype.Graph import Graph
from utils.haversine import haversine
import heapq

def ucs(graph: Graph, src: str, dest: str):

    # Find all location neighbors
    graph.setNeighbour()

    # Find all weight for neighboring locations
    graph.setAllLocationWeight()

    # Get source and destination location
    srcLoc = graph.findLocation(src)
    destLoc = graph.findLocation(dest)

    # Initialize priority queue
    priorityqueue = []

    # Initialize isVisited array
    isVisited = [False for i in range(len(graph.locations))]

    # Push source destination to priority queue
    heapq.heappush(priorityqueue, (0, srcLoc, srcLoc.name))

    # Variable for looping condition
    check = True

    # Looping until path from src to destination is found or until priority queue is empty
    while check:
        # Dequeue priority queue tuple to check
        checkLocation = heapq.heappop(priorityqueue)
        
        # Return checkLocation if Location == destination
        if (checkLocation[1] == destLoc):
            return checkLocation
        
        # Adding all neighbor for current location to priority queue
        for neighborsName in checkLocation[1].neighbour:
            # Get neighbor location
            neighbors = graph.findLocation(neighborsName)

            # Initialize new cost or weight for the neighbor location
            newWeight = checkLocation[0] + checkLocation[1].weight[neighborsName]

            # Initialize new path for the neighbor location
            newPath = checkLocation[2] + " - " + neighborsName

            # Remove current location from the neighbour's neighbor so there is no loop between location
            if (checkLocation[1].name in neighbors.neighbour):
                neighbors.neighbour.remove(checkLocation[1].name)

            # Adding neighbor to prioqueue
            heapq.heappush(priorityqueue, (newWeight, neighbors, newPath))

        # Looping condition
        check = (len(priorityqueue) != 0 or checkLocation[1] != destLoc)