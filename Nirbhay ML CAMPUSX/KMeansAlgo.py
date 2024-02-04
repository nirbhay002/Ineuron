# %%
import random
import numpy as np

class KMeans:
    def __init__(self,n_clusters=2,max_iter=100000):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None
        self.inertia_ = None

    def fit_predict(self,X):

        random_index = random.sample(range(0,X.shape[0]),self.n_clusters)
        #random.sample(range(0,10),4) --> output will be any 4 random values selected from (0,10)
        #X.shape[0] will give no. of rows from X dataframe & X.shape[1] will give no. of columns
        self.centroids = X[random_index]

        for i in range(self.max_iter):
            # assign clusters
            cluster_group = self.assign_clusters(X)
            old_centroids = self.centroids
            # move centroids
            self.centroids = self.move_centroids(X,cluster_group)
            # check finish
            if (old_centroids == self.centroids).all():
                break

        #to calculate WCSS
        self.inertia_ = self.calculate_wcss(X, cluster_group)
        
        return cluster_group

    def assign_clusters(self,X):
        cluster_group = []
        distances = []

        for row in X:
            for centroid in self.centroids:
                distances.append(np.sqrt(np.dot(row-centroid,row-centroid)))
            min_distance = min(distances)
            index_pos = distances.index(min_distance)
            cluster_group.append(index_pos)
            distances.clear()

        return np.array(cluster_group)

    def move_centroids(self,X,cluster_group):
        new_centroids = []

        cluster_type = np.unique(cluster_group)

        for type in cluster_type:                    
            new_centroids.append(X[cluster_group == type].mean(axis=0))
            #axis = 0, bcz we need mean column wise
            #suppose we have array a = [[1,2],[2,3],[3,4],[4,5],[5,6]]
            #then array.mean(axis=0) = (3,4)

        return np.array(new_centroids)


    #this function is written by me
    def calculate_wcss(self, X, cluster_group):
        wcss = 0
        cluster_type = np.unique(cluster_group)

        for i in cluster_type:
            cluster_points = X[cluster_group == i]
            centroid = X[cluster_group == i].mean(axis=0)
            for cluster_point in cluster_points:
                wcss += (np.sqrt(np.dot(cluster_point - centroid, cluster_point - centroid)))** 2

        return wcss



