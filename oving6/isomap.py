""" Contains functions for isomap."""
import numpy as np
from sklearn.utils.graph_shortest_path import graph_shortest_path
from oving6.pca import decomposition


def isomap(data, k):
    """ Visualizes the given data set with isomap, and k nearest neighbors."""
    rows = data.shape[0]

    # geodesic distance matrix
    row_matrix = np.sum(np.square(data), axis=1, keepdims=True)
    distances = np.sqrt(np.abs(row_matrix + row_matrix.T - (2 * (data @ data.T))))
    zeroed_dist = np.array([np.where(row > sorted(row)[k], 0, row) for row in distances])
    short_path = graph_shortest_path(zeroed_dist, directed=False)

    # MSD
    proximity = short_path**2
    center = np.eye(rows) - (np.ones((rows, rows)) / rows)
    double = (-1/2) * center @ proximity @ center
    e_val, e_vec = decomposition(double, rows, 2)
    return e_vec @ np.diag(e_val**(1/2))
