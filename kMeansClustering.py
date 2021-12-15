import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def readData(path):
    data = []
    file = open(path, "r")
    for line in file:
        li = line.split(",")
        data.append([float(li[0]), float(li[1]), -1])
    file.close()
    return data


def objectiveFunction(data, centers):
    value = 0   # Sum of the squared error (SSE)
    for d in data:
        value += ((d[0] - centers[d[2]][0]) ** 2) + ((d[1] - centers[d[2]][1]) ** 2)
    return value


def kMeans(k, data):
    centers = []
    for i in range(k):  # Choose random cluster centers
        centers.append(random.choice(data))
        while i > 0 and centers[i] == centers[i - 1]:
            centers[i] = random.choice(data)  # Avoid duplicate centers
        centers[i][2] = i  # i = cluster name

    iteration = 0
    objectiveValue = 0
    objectiveValues = []
    while 1:
        iteration += 1
        for index, d in enumerate(data):  # Assign each point to the closest cluster center
            shortestDistance = 1000
            for index2, c in enumerate(centers):
                dist = np.math.sqrt(((d[0] - c[0]) ** 2) + ((d[1] - c[1]) ** 2))
                if dist < shortestDistance:
                    shortestDistance = dist
                    data[index][2] = index2

        clustersAverage = []
        clustersQuantity = []
        for j in range(k):
            clustersAverage.append([0, 0])
            clustersQuantity.append(0)
        for d in data:  # Calculate the average of clusters
            clustersAverage[d[2]] = [clustersAverage[d[2]][0] + d[0], clustersAverage[d[2]][1] + d[1]]
            clustersQuantity[d[2]] += 1
        for j in range(k):
            clustersAverage[j] = [clustersAverage[j][0] / clustersQuantity[j],
                                  clustersAverage[j][1] / clustersQuantity[j]]
        for j in range(k):  # Assign the centers their new values
            centers[j] = [clustersAverage[j][0], clustersAverage[j][1], j]

        previousObjectiveValue = objectiveValue
        objectiveValue = objectiveFunction(data, centers)
        objectiveValues.append(objectiveValue)

        if iteration == 1:
            plotClusters(data, centers, "Initial", iteration, objectiveValue)
        elif objectiveValue + 0.1 > previousObjectiveValue:
            break   # Threshold: 0.1

    print("Iterations:", iteration, "Objective Function Value:", objectiveValue)
    plotClusters(data, centers, "Final", iteration, objectiveValue)
    plotLineGraph(objectiveValues)


def plotLineGraph(values):
    x = []
    for i in range(len(values)):
        x.append(i + 1)
    plt.figure(figsize=(10, 7))
    plt.plot(x, values, marker='o')
    plt.title('Objective Function')
    plt.xlabel('Iteration')
    plt.ylabel('Objective Function Value')
    plt.show()


def plotClusters(data, centers, state, iteration, objectiveValue):
    if data[0][0] == 0.89:
        dataName = "Data 1"
    elif data[0][0] == 336.20:
        dataName = "Data 2"
    else:
        dataName = "Data 3"
    minX = 1000
    maxX = -1000
    minY = 1000
    maxY = -1000
    for row in data:
        if row[0] < minX:
            minX = row[0]
        elif row[0] > maxX:
            maxX = row[0]
        if row[1] < minY:
            minY = row[1]
        elif row[1] > maxY:
            maxY = row[1]

    colorsLight = ['#ec3dff', '#ffd83b', '#2beaff', '#61ff5e', '#fa2a5e', '#5c4aff']
    colorsDark = ['#8d2399', '#b09527', '#1c8f9c', '#3da13b', '#961a39', '#362c96']
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x=list(zip(*data))[0], y=list(zip(*data))[1], hue=list(zip(*data))[2],
                    palette=colorsLight[:len(centers)], alpha=0.5, s=10, edgecolor="white")
    sns.scatterplot(x=list(zip(*centers))[0], y=list(zip(*centers))[1], hue=list(zip(*centers))[2],
                    palette=colorsDark[:len(centers)], alpha=1, s=20, edgecolor="white")
    plt.xlim(minX - 5, maxX + 5)
    plt.ylim(minY - 5, maxY + 5)
    plt.title("K-Means %s Clusters  -  %s  -  Iterations=%i  -  Objective Function Value=%f  -  K=%i" % (
        state, dataName, iteration, objectiveValue, len(centers)))
    plt.xlabel("x coordinates")
    plt.ylabel("y coordinates")
    plt.show()


def scikitCluster(k, data):
    for d in data:
        del d[2]
    kmeans = KMeans(n_clusters=k, n_init=1, max_iter=50).fit(data)
    for index, d in enumerate(data):
        d.append(kmeans.labels_[index])
    centers = []
    for i in range(k):
        centers.append([kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1], i])
    plotClusters(data, centers, "Scikit-Learn", kmeans.n_iter_, kmeans.inertia_)


data1 = readData("data1.txt")
data2 = readData("data2.txt")
data3 = readData("data3.txt")
kMeans(3, data1)
kMeans(6, data1)
kMeans(4, data2)
kMeans(4, data3)
scikitCluster(3, data1)
scikitCluster(6, data1)
