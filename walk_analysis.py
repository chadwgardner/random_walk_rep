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



plt.show()
