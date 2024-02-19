import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
import seaborn as sns
from ucimlrepo import fetch_ucirepo

# fetch dataset
breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17)

temp = breast_cancer_wisconsin_diagnostic.data.original

temp.to_csv('breast_cancer.csv', sep=',', index=False)

