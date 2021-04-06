""" This module runs the whole program,
as well as containing the visualize function"""

from oving6.isomap import isomap
from oving6.pca import fit_transform
import matplotlib.pyplot as plt
import numpy as np


def visualize(data, color):
    """"
    Takes in a set of data points,
    visualizes them in a scatter plot, and shows them.

    :var data; THe data set.
    :var color: The coloring to be used in the visualization.
    """
    x_data = data[:, 0]
    y_data = data[:, 1]
    plt.scatter(x=x_data, y=y_data, s=10, marker='.', c=color, cmap='jet')
    plt.show()


# gets the data sets
dt_swiss = np.genfromtxt('swiss_data.csv', delimiter=',')
dt_digit = np.genfromtxt('digits.csv', delimiter=',')

# color for visualization
swiss_color = np.arange(2000)
digit_color = np.genfromtxt('digits_label.csv', delimiter=',')

# PCA
visualize(fit_transform(dt_swiss), swiss_color)
visualize(fit_transform(dt_digit), digit_color)

# isomap
visualize(isomap(dt_swiss, 10), swiss_color)
visualize(isomap(dt_digit, 50), digit_color)

# t-SNE
# visualize(t_sne(dt_digit), digit_color)
