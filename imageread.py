import numpy as np
from scipy.spatial.distance import pdist, squareform

def extract_edges(nodes, distance_threshold):
    """
    Extract edges from a set of nodes with 3D coordinates based on a Euclidean distance threshold.

    Parameters:
    - nodes (numpy.ndarray): Array of shape (N, 3) representing N nodes with 3D coordinates.
    - distance_threshold (float): Euclidean distance threshold for edge extraction.

    Returns:
    - edges (list): List of tuples representing edges where the Euclidean distance is below the threshold.
    """

    # Calculate pairwise distances between nodes
    pairwise_distances = pdist(nodes)

    # Convert pairwise distances to a square matrix
    distance_matrix = squareform(pairwise_distances)

    # Find indices where distances are below the threshold
    edges_indices = np.where(distance_matrix < distance_threshold)

    # Create a list of edges as tuples
    edges = [(i, j) for i, j in zip(edges_indices[0], edges_indices[1]) if i < j]

    return edges

# Example usage:
nodes = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1]
])

distance_threshold = 1.5
edges = extract_edges(nodes, distance_threshold)
print("Edges:", edges)
print ("number of edges", len(edges))

