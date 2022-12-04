from typing import List

from matplotlib import pyplot as plt
from numpy import ndarray


def elbow_plot(k: List[int], inertia: List[float]):
    plt.figure(figsize=(10, 8))
    plt.plot(k, inertia, marker='o', color='green')
    plt.xlabel('number of clusters : k')
    plt.ylabel('inertia')
    plt.tight_layout()
    plt.show()


def plot_clusters(data: ndarray, labels: ndarray, centroids: ndarray):
    plt.figure(figsize=(10, 7))
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=300)
    plt.show()
