from sklearn.decomposition import PCA

# Perform pca

def perform_PCA(genotypes, n_components = 10):
    pca = PCA(n_components=n_components)
    pca.fit(genotypes)
    pcs = pca.transform(genotypes).transpose()

    return pcs