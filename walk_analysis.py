import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from random_walk import get_walks
from my_stats import ecdf

sns.set()


#getting walks
x, y = get_walks(10000, 100)
#x_np = np.array(x)
#y_np = np.array(y)

#get end points of walks, calculate distances from origin, find mean
end_points = [[i[-1],j[-1]] for i,j in zip(x, y)]
distances = np.sqrt([i[0]**2 + i[1]**2 for i in end_points])
mean_dist = np.mean(distances)
std_dist = np.std(distances)

conf_int = np.percentile(distances, [2.5,97.5])

#prepare normal samples
samples = np.random.normal(mean_dist, std_dist, size=10000)
x_ther, y_ther = ecdf(samples)
x_ecdf, y_ecdf = ecdf(distances)


#examining avg coordinates and their distribution
flat_coords = [list(i) for i in x]
for i in range(len(flat_coords)):
    flat_coords[i].extend(y[i])
coords_avg = [np.mean(i) for i in flat_coords]
coords_avg_avg = np.mean(coords_avg)
coords_std = np.std(coords_avg)
coords_normal = np.random.normal(coords_avg_avg, coords_std, size=10000)

#ecdf and pdf of coords
plt.subplot(2,1,1)
x_coords_ecdf, y_coords_ecdf = ecdf(coords_avg)
x_coords_ther, y_coords_ther = ecdf(coords_normal)
plt.plot(x_coords_ecdf, y_coords_ecdf, marker='.', linestyle='none')
plt.plot(x_coords_ther, y_coords_ther)
plt.legend(['mean', 'normal', 'random walk'])
plt.xlabel('Mean coordinate of walks')
plt.ylabel('Probability')
plt.title('CDFs')

#hist of coords
plt.subplot(2,1,2)
plt.hist(coords_avg, normed=True, bins=40, alpha=0.40)
plt.hist(coords_normal, normed=True, bins=40, alpha=0.4, histtype='stepfilled')
plt.axvline(x=coords_avg_avg, color='r', alpha=0.5)
plt.legend(['mean', 'normal', 'mean coords'])
plt.xlabel('Mean coordinates of walks')
plt.ylabel('Fraction of walks')

"""
#plotting ecdf and pdf of coords


#histogram
plt.subplot(2,1,1)
plt.hist(distances, normed=True, bins=40, alpha=0.4)
plt.hist(samples, histtype='stepfilled', normed=True, bins=100, alpha=0.4)
plt.axvline(x=mean_dist, color='r', alpha=0.4)
plt.legend(['mean', 'normal', 'random walk'])
plt.xlabel('Distance walked in steps')
plt.ylabel('Fraction of walks')

#ecdf and pdf plots
plt.subplot(2,1,2)
plt.plot(x_ecdf, y_ecdf, marker='.', linestyle='none', alpha=.4)
plt.plot(x_ther, y_ther)
plt.xlim(xmin=0)
plt.axvline(x=mean_dist, color='r', alpha=.4)
plt.legend(['random walk', 'normal', 'mean'])
"""


plt.show()
