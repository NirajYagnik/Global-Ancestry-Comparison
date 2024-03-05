# Load the 0/1/2 matrix
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(fname="1kg_chr16_pca_recode.raw"):
    data = pd.read_csv(fname, delim_whitespace=True)
    data.dropna(axis=1, how='any', inplace=True)

    snpcols = data.columns[6:]

    # Get data matrix
    genotypes = np.array(data[snpcols])

    scaler = StandardScaler()
    genotypes = scaler.fit_transform(genotypes)

    return genotypes


def make_plot_ready(data, pcs, n_components = 10, prefix="PC"):
    pca_df = pd.DataFrame(pcs.T, columns=[f"{prefix}{i+1}" for i in range(n_components)])
    data_subset = data[['FID', 'IID']]
    pca_df = pd.concat([data_subset, pca_df], axis=1)

    return pca_df