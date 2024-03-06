import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def process_for_testing(data,prefix, pcx=1, pcy=2):
  IGSRFILE="src/igsr_samples.tsv"
  samp = pd.read_csv(IGSRFILE, sep="\t")
  samp = samp[["Sample name", "Superpopulation code", "Population code"]]
  samp.rename(columns={"Sample name": "IID"}, inplace=True)
  data = pd.merge(data, samp, on=["IID"], how="left")
  data = data[[prefix + str(pcx), prefix + str(pcy),'Superpopulation code','Population code']]
  return data

def evaluate_homogeneity(df, cluster_col='kmeans_cluster', pop_col='Superpopulation code'):
    cluster_homogeneity = {}
    for cluster in df[cluster_col].unique():
        # Get the most common superpopulation code in each cluster
        most_common_code = df[df[cluster_col] == cluster][pop_col].value_counts().idxmax()
        # Check if all samples in the cluster have this superpopulation code
        if df[df[cluster_col] == cluster][pop_col].nunique() == 1:
            cluster_homogeneity[cluster] = (most_common_code, True)
        else:
            cluster_homogeneity[cluster] = (most_common_code, False)
    return cluster_homogeneity

def run_kmeans(data,prefix,pcx=1, pcy=2):
  k = int(sqrt(data.shape[0]))  # df.shape[0] gives the number of samples
  kmeans = KMeans(n_clusters=k)
  data['kmeans_cluster'] = kmeans.fit_predict(data[[prefix + str(pcx), prefix + str(pcy)]])
  return data, k

def compute_score(data,prefix="PC",pcx=1, pcy=2):
  data = process_for_testing(data,prefix,pcx=1, pcy=2)
  data, k = run_kmeans(data,prefix, pcx,pcy)
  homogeneity_info = evaluate_homogeneity(data)
  homogeneous_clusters = [cluster for cluster, data in homogeneity_info.items() if data[1]]
  proportion_homogeneous = len(homogeneous_clusters) / k
  return proportion_homogeneous