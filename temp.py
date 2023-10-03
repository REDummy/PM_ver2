import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
import seaborn as sns
from ucimlrepo import fetch_ucirepo

# Load the data
heart_failure_clinical_records = fetch_ucirepo(id=519)
target = heart_failure_clinical_records.data.targets
data = heart_failure_clinical_records.data.features

# Perform k-means clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
kmeans_labels = kmeans.labels_

# Perform DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=10)
dbscan.fit(data)
dbscan_labels = dbscan.labels_

# Perform hierarchical clustering
ward = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
ward.fit(data)
ward_labels = ward.labels_

# Plot the data using pairplot
sns.set(style="ticks")
sns.pairplot(data, hue=kmeans_labels)
plt.suptitle("Pair Plot with KMeans Clusters", y=1.02)
plt.show()

# Plot the data using pairplot
sns.set(style="ticks")
sns.pairplot(data, hue=dbscan_labels)
plt.suptitle("Pair Plot with DBSCAN Clusters", y=1.02)
plt.show()

# Plot the data using pairplot
sns.set(style="ticks")
sns.pairplot(data, hue=ward_labels)
plt.suptitle("Pair Plot with Hierarchical Clusters", y=1.02)
plt.show()
