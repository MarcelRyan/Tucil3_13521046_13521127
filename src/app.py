from flask import Flask, render_template
import folium
from mainProgram import main_program

app = Flask(__name__)

# GLOBAL VARIABLE RESULT TO VISUALIZE
result = None

@app.route('/')
def index():
    # FETCH DATAS
    locations, adjacency_matrix, source_loc, destination_loc, shortest_routes = result
    
    # FIND ALL ROUTES BASED ON ADJACENCY MATRIX
    routes = []
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] > 0:
                start = (locations[i].getLat(), locations[i].getLong())
                end = (locations[j].getLat(), locations[j].getLong())
                route = [start, end]
                routes.append(route)

    # SET UP MAP
    m = folium.Map(location=[(locations[0].getLat()+locations[-1].getLat())/2, (locations[0].getLong()+locations[-1].getLong())/2], zoom_start=13)

    # VISUALIZE LOCATIONS
    for loc in locations:
        point_color = 'blue'
        if (loc == source_loc):
            point_color = 'red'
        if (loc == destination_loc):
            point_color = 'green'
        folium.Marker(location=[loc.getLat(), loc.getLong()], tooltip=loc.getName(), icon=folium.Icon(color=point_color)).add_to(m)

    # VISUALIZE ROUTES
    for route in routes:
        route_color = 'green'
        if route in shortest_routes:
            route_color = 'blue'
        folium.PolyLine(locations=route, color=route_color).add_to(m)

    return m._repr_html_()

if __name__ == '__main__':
    try:
        result = main_program()
        app.run(debug=False)
    except:
        print("""Since the txt file didn't suit the format we use, you can use another
            txt file by running the program again :)""")
