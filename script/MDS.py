from sklearn.manifold import MDS

def perform_MDS(genotypes, n_components = 2):
    mds = MDS(n_components=n_components)
    # Fit the MDS model to your data
    X_reduced = mds.fit_transform(genotypes)
    return X_reduced


