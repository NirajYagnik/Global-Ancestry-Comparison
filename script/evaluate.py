import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# Function to process the input data for testing
# This includes merging with a sample information file to get population codes
def process_for_testing(data, prefix, pcx=1, pcy=2):
  # Path to the file containing sample information
  IGSRFILE = "src/igsr_samples.tsv"
  
  # Read the sample file, keeping only relevant columns
  samp = pd.read_csv(IGSRFILE, sep="\t")
  samp = samp[["Sample name", "Superpopulation code", "Population code"]]
  
  # Rename columns for consistency
  samp.rename(columns={"Sample name": "IID"}, inplace=True)
  
  # Merge the input data with the sample information
  data = pd.merge(data, samp, on=["IID"], how="left")
  
  # Select only the columns of interest for analysis
  data = data[[prefix + str(pcx), prefix + str(pcy), 'Superpopulation code', 'Population code']]
  return data

# Function to evaluate the homogeneity of clusters based on population codes
def evaluate_homogeneity(df, cluster_col='kmeans_cluster', pop_col='Superpopulation code'):
    cluster_homogeneity = {}
    
    # Iterate through each unique cluster
    for cluster in df[cluster_col].unique():
        # Identify the most common superpopulation code in the cluster
        most_common_code = df[df[cluster_col] == cluster][pop_col].value_counts().idxmax()
        
        # Check if all members of the cluster share the same superpopulation code
        if df[df[cluster_col] == cluster][pop_col].nunique() == 1:
            cluster_homogeneity[cluster] = (most_common_code, True)
        else:
            cluster_homogeneity[cluster] = (most_common_code, False)
    return cluster_homogeneity

# Function to run KMeans clustering on the data
def run_kmeans(data, prefix, pcx=1, pcy=2):
  # Estimate the number of clusters as the square root of the sample size
  k = int(sqrt(data.shape[0]))  # data.shape[0] gives the number of samples
  
  # Initialize and fit the KMeans model
  kmeans = KMeans(n_clusters=k)
  data['kmeans_cluster'] = kmeans.fit_predict(data[[prefix + str(pcx), prefix + str(pcy)]])
  return data, k

# Function to compute the score of clustering based on homogeneity
def compute_score(data, prefix="PC", pcx=1, pcy=2):
  # Process the data for testing
  data = process_for_testing(data, prefix, pcx, pcy)
  
  # Perform KMeans clustering
  data, k = run_kmeans(data, prefix, pcx, pcy)
  
  # Evaluate the homogeneity of clusters
  homogeneity_info = evaluate_homogeneity(data)
  
  # Identify clusters that are completely homogeneous
  homogeneous_clusters = [cluster for cluster, data in homogeneity_info.items() if data[1]]
  
  # Calculate the proportion of clusters that are homogeneous
  proportion_homogeneous = len(homogeneous_clusters) / k
  return proportion_homogeneous
