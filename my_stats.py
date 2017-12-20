import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, len(data)+1) / n

    return x, y

#variance is the mean of the squared distances of data points from the mean (nb: weird units)
def variance(data):
    """Compute the variance of a one-dimensional array"""
    differences = data - np.mean(data)
    diff_sq = differences ** 2
    variance = np.mean(diff_sq)

    return variance

#standard deviation is the squareroot of the variance (nb: same units as data)
#in numpy use np.std()
def standard_deviation(data):
    """Compute the standard deviation of a one-dimensional array"""

    return np.sqrt(variance(data))


#covariance is the mean of the product of the distances of each points' coordinates from that coordinate's mean
def covariance(x, y):
    x_dist = x - np.mean(x)
    y_dist = y - np.mean(y)
    cov = np.mean(x_dist * y_dist)

    return cov

# The Pearson correlation coeffiecient is a dimensionless measurement of the covariance
def pearson_cov(x,y):
    return covariance(x, y) / (standard_deviation(x) * standard_deviation(y))
