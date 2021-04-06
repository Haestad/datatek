import numpy as np
import matplotlib.pyplot as plt
import IPython

data = np.genfromtxt('digits.csv', delimiter=',')
labels = np.genfromtxt('digits_label.csv', delimiter=',')

data = data[:100, :]
labels = labels[:100]

k = 50
row_matrix = np.sum(np.square(data), axis=1, keepdims=True)
distances = np.sqrt(np.abs(row_matrix + row_matrix.T - (2 * (data @ data.T))))
new_thing = np.array([np.where(row > sorted(row)[k], 0, 1) for row in distances])


""" checking knn graph 
ind = np.argsort(labels)
plt.spy(new_thing[:, ind][ind, :], markersize=0.1)
plt.show()
"""
IPython.embed()
