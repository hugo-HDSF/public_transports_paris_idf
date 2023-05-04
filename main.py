# Import necessary libraries
import heapq
import json
import math
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.patheffects as path_effects
import networkx as nx
import chardet
import fuzzywuzzy
from fuzzywuzzy import process

# https://www.transilien.com/

# Source and target stations
source = "garibaldi"
target = "mairie d'issy"
multiple_path_options = True
changing_line_penality = 300
walking_to_nearest_station_reward = 20
node_weight = 5
edge_weight = 50

matplotlib.use("module://mplcairo.base")
# Use Cairo background for the plot
plt.rcParams['figure.facecolor'] = '#111111'

# Function to get the color of the line
def get_line_color(line_label):
    for line, color in line_colors.items():
        if line == line_label:
            return color
    return "black"

# Function to check if an edge exists in the graph
def edge_exists(G, station1, station2, label):
    if G.has_edge(station1, station2):
        for edge_data in G.get_edge_data(station1, station2).values():
            if edge_data == label:
                return True
    return False

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Function to patch the shortest path for any useless changes
def patch_shortest_path(G, edge_labels, shortest_path):
    patched_labels = edge_labels.copy()
    prev_label = None
    known_labels = []
    z = 0
    for i in range(len(shortest_path) - 1):
        current_edge = (shortest_path[i], shortest_path[i + 1])
        current_edge_inversed = (shortest_path[i + 1], shortest_path[i])
        if G.has_edge(*current_edge) or G.has_edge(*current_edge_inversed):
            try:
                current_label = edge_labels[(current_edge[0], current_edge[1])]
            except KeyError:
                current_label = edge_labels[(current_edge[1], current_edge[0])]
            if prev_label is not None:
                if not current_label == prev_label:
                    prev_label = current_label
                    if (current_label in known_labels):
                        # Replace labels of edges before the current edge
                        for j in range(z):
                            prev_edge = (shortest_path[j], shortest_path[j + 1])
                            try:
                                patched_labels[(shortest_path[j], shortest_path[j + 1])] = current_label
                                patched_labels[(shortest_path[j + 1], shortest_path[j])] = current_label
                            except KeyError:
                                continue
                        # Reset known_labels to []
                        known_labels = []
                        z = 0
                    known_labels.append(current_label)
                    z += 1
                else:
                    z += 1
            else:
                patched_labels[current_edge] = current_label
                prev_label = current_label
                known_labels.append(current_label)
                z += 1
    return patched_labels

# Function to get the shortest path between two stations in the graph
def get_shortest_path(G, source, target):
    global AStarAndBellmanFord
    shortest_path_1, distance_1 = find_shortest_path(G, source, target)
    shortest_path_R_1, distance_R_1 = find_shortest_path(G, target, source)

    if AStarAndBellmanFord:
        AStarAndBellmanFord = False
    else:
        AStarAndBellmanFord = True

    shortest_path_2, distance_2 = find_shortest_path(G, source, target)
    shortest_path_R_2, distance_R_2 = find_shortest_path(G, target, source)

    # Find the shortest distance among the four distances
    shortest_distance, shortest_path = min((distance_1, shortest_path_1),
                                           (distance_R_1, shortest_path_R_1),
                                           (distance_2, shortest_path_2),
                                           (distance_R_2, shortest_path_R_2),
                                           key=lambda x: x[0])
    return shortest_path

# Function to get multiple shortest paths between two stations in the graph
def get_multiple_shortest_paths(G, source, target):
    global AStarAndBellmanFord
    shortest_path_1, distance_1 = find_shortest_path(G, source, target)
    shortest_path_R_1, distance_R_1 = find_shortest_path(G, target, source)

    if AStarAndBellmanFord:
        AStarAndBellmanFord = False

    else:
        AStarAndBellmanFord = True

    shortest_path_2, distance_2 = find_shortest_path(G, source, target)
    shortest_path_R_2, distance_R_2 = find_shortest_path(G, target, source)

    # Concatenate the two paths and edge colors
    shortest_path = dict(shortest_path_1.items() | shortest_path_R_1.items() | shortest_path_2.items() | shortest_path_R_2.items())
    return shortest_path

# Function to find the shortest path between two stations in the graph
def find_shortest_path(G, source, target):
    try:
        shortest_path, distance = a_star_or_bellman_ford_modified(G, source, target)
    except nx.NetworkXNoPath:
        return None  # Pas de chemins trouvé
    return shortest_path, distance

# Function to redefine the A* and Bellman-Ford algorithms
def a_star_or_bellman_ford_modified(G, source_node, target_node):
    # Initialize distances
    edge_labels = nx.get_edge_attributes(G, "line")
    distances = {node: float('infinity') for node in G.nodes}
    distances[source_node] = 0
    source = source_node
    target = target_node

    # Initialize priority queue
    pq = [(0, source_node, None)]

    # Visited set
    visited = set()

    # Initialize previous dictionary
    previous = {}

    while pq:
        # Get the node with the lowest total weight from the priority queue
        current_distance, current_node, prev_edge = heapq.heappop(pq)

        # If we have already visited this node, continue
        if current_node in visited:
            continue

        visited.add(current_node)

        previous[current_node] = prev_edge

        # If we reached the target node, return the total distance
        if current_node == target_node:
            # Build the path by backtracking from the target node to the source node
            path_edges = {}
            current_edge = prev_edge
            distance = pq[0][0]
            while current_edge is not None:
                path_edges[current_edge] = edge_labels[current_edge]
                prev_node = current_edge[0] if current_edge[0] != current_node else current_edge[1]
                current_edge = previous[prev_node]
                current_node = prev_node
            return path_edges, distance

        # when there is no more "neighbor" for the current "G[current_node].items()" in the for here "for neighbor, edge_data in G[current_node].items():" then the for ends, we go back to the while, and it resets the pq, i think i shouldn't or maybe i'm wrong, i don't know
        # Iterate over neighbors
        for neighbor, edge_data in G[current_node].items():
            # for i in range(G.number_of_edges(current_node, neighbor)):
            # Set the edge based on the current node and the neighbor
            edges = [((current_node, neighbor, i) if (current_node, neighbor, i) in edge_labels else (neighbor, current_node, i)) for i in range(G.number_of_edges(current_node, neighbor))]
            # Sort the edges by their label so that the edge with the same label is first in the list (prioritize the same line)
            edges.sort(key=lambda e: (edge_labels[e] != edge_labels[prev_edge] if prev_edge else False, edge_labels[e]))
            # Iterate over the edges
            for edge in edges:
                label = edge_labels[edge]
                # Check if the current line is a walking path to the next station
                if label == "¤":
                    weight = edge_weight  # edge weight
                    weight -= walking_to_nearest_station_reward  # node weight
                else:
                    # Calculate the total weight
                    weight = edge_weight  # edge weight
                    weight += node_weight  # node weight

                # Check if we were walking
                if prev_edge is not None and edge_labels[prev_edge] == '¤':
                    weight -= walking_to_nearest_station_reward
                # Check if the previous line is not the same as the current line (means we changed lines)
                if prev_edge is not None and edge_labels[prev_edge] != label:
                    if label == "¤":
                        weight -= walking_to_nearest_station_reward
                    else:
                        weight += changing_line_penality

                # Update the distance if it's smaller than the current distance
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    if AStarAndBellmanFord:
                        # Add the heuristic cost to the priority queue
                        total_cost = new_distance + euclidean_distance(G.nodes[neighbor]['pos'], G.nodes[target_node]['pos'])
                    else:
                        total_cost = new_distance
                    heapq.heappush(pq, (new_distance, neighbor, edge))

    # If the target node was not reached, return None
    return None

# Main function
if __name__ == '__main__':

    # Load the JSON data file
    with open("updated_data.json", "rb") as file:
        raw_data = file.read()
        detected_encoding = chardet.detect(raw_data)["encoding"]

    with open("updated_data.json", encoding=detected_encoding) as file:
        data = json.load(file)

    # Create the multi graph
    G = nx.MultiGraph()

    # Define dark color for white font
    white_labels = ['2', '4', '11', '12', '14', '15']
    # Define colors for each line
    line_colors = {
        "1": "#FFCE00",
        "2": "#0064B0",
        "3": "#9F9825",
        "3b": "#98D4E2",
        "4": "#C04191",
        "5": "#F28E42",
        "6": "#83C491",
        "7": "#F3A4BA",
        "7b": "#83C491",
        "8": "#CEADD2",
        "9": "#D5C900",
        "10": "#E3B32A",
        "11": "#8D5E2A",
        "12": "#00814F",
        "13": "#98D4E2",
        "14": "#662483",
        "15": "#B90845",
        "A": "#F7403A",
        "B": "#4B92DB",
        "C": "#F3D311",
        "D": "#3F9C35",
        "E": "#DE81D3",
        "¤": "#ffffff",
    }

    existing_stations = {}

    # mapping of the G graph (nodes and edges)
    for path_id, path_data in data.items():
        stations = path_data['stations']
        for i in range(1, len(stations) - 1, 3):
            node = stations[i - 1]
            node_lat = stations[i]
            node_lon = stations[i + 1]
            if not G.has_node(node):
                G.add_node(node, pos=(node_lat, node_lon))
    for path_id, path_data in data.items():
        stations = path_data['stations']
        label = path_data['transport']
        for i in range(1, len(stations) - 2, 3):
            prev_node = stations[i - 1]
            next_node = stations[i + 2]
            if not edge_exists(G, prev_node, next_node, label):
                G.add_edge(prev_node, next_node, line=label)

    # Extract the nodes labels for the matching process
    node_names = list(G.nodes())
    # Find the closest matching node name for the source and target
    source = process.extractOne(source, node_names)[0]
    target = process.extractOne(target, node_names)[0]

    # this make sur BellmanFord and AStar are used for any path
    AStarAndBellmanFord = True

    # Choose between single or multiple shortest paths
    # if not multiple_path_options, then we get the shortest path
    if not multiple_path_options:
        shortest_path = get_shortest_path(G, source, target)
    # else we get all the possible shortest paths
    else:
        shortest_path = get_multiple_shortest_paths(G, source, target)

    # Visualize the graph
    fig = plt.figure(figsize=(2000 / 96, 4000 / 96), dpi=96)  # 4K resolution
    fig.patch.set_facecolor('#111111')
    H = G.edge_subgraph(shortest_path)

    pos_G = nx.get_node_attributes(G, 'pos')
    edge_labels_G = nx.get_edge_attributes(G, "line")
    edge_colors_G = nx.get_edge_attributes(G, "line")

    shortest_path_nodes = set(H.nodes)

    nx.draw_networkx_nodes(G, pos_G, node_size=0.2, alpha=0.7)

    edge_labels_G = {(u, v): d['line'] for u, v, d in G.edges(data=True)}
    edge_colors_G = {(u, v): line_colors[d['line']] for u, v, d in G.edges(data=True)}
    for edge, label in edge_labels_G.items():
        edge_color = line_colors[label]
        text_color = 'white' if label in white_labels else 'black'
        nx.draw_networkx_edges(G, pos_G, edgelist=[edge], width=0.5, alpha=0.7, edge_color=edge_color)
        nx.draw_networkx_edge_labels(
            G, pos_G,
            edge_labels={edge: label},
            font_size=1,
            font_family="sans-serif",
            font_weight="bold",
            alpha=0.7,
            bbox=dict(
                facecolor=edge_colors_G[edge], edgecolor='none', boxstyle='round,pad=0.5,rounding_size=0.8', alpha=0.7),
            font_color=text_color
        )

    # nx.draw_networkx_labels(G, pos_G, font_size=1, font_family="sans-serif", alpha=0.7, labels={node: node for node in G.nodes if node not in shortest_path_nodes}, font_color='white')
    for node, (x, y) in pos_G.items():
        text = plt.text(x, y, node, fontsize=1, color='white', ha='center', va='center', alpha=0.7)
        text.set_path_effects([path_effects.Stroke(linewidth=0.3, foreground='black'), path_effects.Normal()])

    pos_H = nx.get_node_attributes(H, 'pos')
    edge_labels_H = nx.get_edge_attributes(H, "line")
    edge_colors_H = nx.get_edge_attributes(H, "line")

    edge_labels_H = {(u, v): d['line'] for u, v, d in H.edges(data=True)}
    edge_colors_H = {(u, v): line_colors[d['line']] for u, v, d in H.edges(data=True)}

    # patch path
    # edge_labels_H = patch_shortest_path(H, edge_labels_H, shortest_path)
    # edge_colors_H = {edge: line_colors[label] for edge, label in edge_labels_H.items()}

    nx.draw_networkx_nodes(H, pos_H, node_size=2, node_color='red')

    for edge, label in edge_labels_H.items():
        x = (pos_H[edge[0]][0] + pos_H[edge[1]][0]) / 2
        y = (pos_H[edge[0]][1] + pos_H[edge[1]][1]) / 2
        text_color = 'white' if label in white_labels else 'black'
        font_size = 2 if label == "¤" else 1.5
        edge_color = line_colors[label]
        nx.draw_networkx_edges(H, pos_H, edgelist=[edge], width=1.7, alpha=1, edge_color=edge_color)
        # force to use plt.text instead of nx.draw_networkx_edge_labels for white labels over darker edges
        plt.text(x,
                 y,
                 s=label,
                 fontsize=font_size,
                 family="sans-serif",
                 weight="bold",
                 alpha=0.9,
                 color=text_color,
                 bbox=dict(
                     facecolor=line_colors[label], edgecolor='none', boxstyle='round,pad=0.4,rounding_size=0.8', alpha=1),
                 )

    # nx.draw_networkx_labels(H, pos_H, font_size=1.5, font_family="sans-serif", font_weight="bold", font_color='white')
    for node, (x, y) in pos_H.items():
        text = plt.text(x, y, node, fontsize=1.5, fontweight="bold", color='white', ha='center', va='center', alpha=0.7)
        text.set_path_effects([path_effects.Stroke(linewidth=0.3, foreground='black'), path_effects.Normal()])

    plt.style.use('ggplot')
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("transports_paths.svg", format='svg', dpi=200, bbox_inches='tight')
    # plt.show()
