""" Contains functions for PCA, as well as eigen-decomposition"""
import numpy as np
from scipy.sparse.linalg import eigs


def decomposition(data, data_dim, dim_reduce):
    """ Takes in a matrix, the original dimensions and dimension to reduce to,
    and performs truncated decomposition."""
    if data_dim - 1 == dim_reduce:
        val, vec = np.linalg.eigh(data)
    elif data_dim - 1 > dim_reduce:
        val, vec = eigs(data, k=dim_reduce)
        val = np.real(val)
        vec = np.real(vec)
    else:
        return None
    return val, vec


def fit_transform(data):
    """ Fits the PCA model to the given data points,
    and then transforms the data points to be used in PCA.

    :var data: The given data points.
    :return: The transformed data points.
    """
    # dimensions to reduce to
    dim_reduce = 2
    data_dim = data.shape[1]
    center_data = data - data.mean(axis=0)
    # creates covariance matrix
    sigma = np.cov(data, rowvar=False)
    # truncated decomposition, sorted in asc order
    e_val, e_vec = decomposition(sigma, data_dim, dim_reduce)
    # the eigenvectors corresponding to d highest eigenvalues
    vectors = e_vec[:, -dim_reduce:]
    return center_data @ vectors
