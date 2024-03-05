from sklearn.manifold import Isomap

def perform_Isomap(genotypes, n_components = 2, n_neighbors = 200):
    isomap = Isomap(n_neighbors=n_neighbors, n_components=n_components)
    X_transformed = isomap.fit_transform(genotypes)

    return X_transformed