import numpy as np
from ucimlrepo import fetch_ucirepo
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns


# fetch dataset
heart_failure_clinical_records = fetch_ucirepo(id=519)

# data (as pandas dataframes)
target = heart_failure_clinical_records.data.targets
data = heart_failure_clinical_records.data.features

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

n_clusters = 2
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(data_scaled)

cluster_labels = kmeans.labels_


index_to_name = {
    0: 'deadge',
    1: 'livedge',
}

pred = [index_to_name[cluster] for cluster in cluster_labels]


# Create a pair plot including the cluster assignments

data['Cluster'] = pred  # Add cluster assignments as a new column

# Use Seaborn to create a pair plot
sns.set(style="ticks")
sns.pairplot(data, hue="Cluster")
plt.suptitle("Pair Plot with K-Means Clusters", y=1.02)
plt.show()  # Display the pair plot


from sklearn.cluster import DBSCAN

# Create and fit a DBSCAN model
# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(data_scaled)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

# Map cluster labels to names
dbscan_pred = [index_to_name[label] for label in labels]

# Add DBSCAN cluster assignments as a new column
data['Cluster_DBSCAN'] = dbscan_pred

# Use Seaborn to create a pair plot for DBSCAN clusters
sns.set(style="ticks")
sns.pairplot(data, hue="Cluster_DBSCAN")
plt.suptitle("Pair Plot with DBSCAN Clusters", y=1.02)
plt.show()


from sklearn.cluster import AgglomerativeClustering

# Create and fit an AgglomerativeClustering model
agg_clustering = AgglomerativeClustering(n_clusters=n_clusters)
agg_labels = agg_clustering.fit_predict(data_scaled)

# Map cluster labels to names
agg_pred = [index_to_name[label] for label in agg_labels]

# Add hierarchical clustering cluster assignments as a new column
data['Cluster_Hierarchical'] = agg_pred

from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Perform hierarchical clustering
linkage_matrix = linkage(data_scaled, method='ward')

# Plot the dendrogram
plt.figure(figsize=(30, 18))
dendrogram(linkage_matrix, orientation='top', labels=agg_pred, distance_sort='descending', show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index or (Cluster Size)')
plt.ylabel('Distance')
plt.show()

