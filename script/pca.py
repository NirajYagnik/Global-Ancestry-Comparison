from sklearn.decomposition import PCA

# Perform pca

def perform_pca(genotypes, n_components = 10):
    pca = PCA(n_components=10)
    pca.fit(genotypes)
    pcs = pca.transform(genotypes).transpose()

    return pcs