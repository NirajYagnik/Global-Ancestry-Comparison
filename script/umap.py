import umap

def perform_umap(genotypes):
    reducer = umap.UMAP(random_state=42)
    umap_embedding = reducer.fit_transform(genotypes)

    return umap_embedding