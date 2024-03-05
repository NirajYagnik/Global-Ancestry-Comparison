import umap

def perform_UMAP(genotypes, random_state = 42):
    reducer = umap.UMAP(random_state=random_state)
    umap_embedding = reducer.fit_transform(genotypes)

    return umap_embedding