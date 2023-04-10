from datatype.Location import Location

def parse(filename):
    # ASSUMPTION : filename is defined and exist in tests directory
    # FILENAME FORMAT : name.txt
    filepath = 'tests/' + filename

    # CREATE LIST OF LOCATION
    locations = []

    # CREATE ADJACENCY MATRIX
    adjacency = []

    try: 
        # OPEN FILE
        with open(filepath, 'r') as f:
            lines = f.readlines()

            # FIRST LINE : NUMBER OF VERTICES
            number_of_vertices = int(lines[0])

            # VERTICES LOCATION
            for line in range(1, 2 * number_of_vertices + 1, 2):
                # EXTRACT DATA
                loc_name = lines[line].strip()
                loc_latitude, loc_longtitude = map(float, lines[line+1].strip().split(", "))

                # CREATE LOCATION
                location = Location(loc_name, loc_latitude, loc_longtitude)

                # APPEND TO LOCATION LIST
                locations.append(location)

            # ADJACENCY MATRIX
            for line in range(2 * number_of_vertices + 1, len(lines)):
                row = list(map(float, lines[line].split()))
                adjacency.append(row)

        # RETURN LOCATIONS AND ADJACENCY MATRIX
        return locations, adjacency
    except Exception as e:
        print(e)
        