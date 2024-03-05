from sklearn.manifold import TSNE

def perform_TSNE(genotypes, n_components=2, perplexity=30, learning_rate=200, random_state=0):
    tsne = TSNE(n_components=n_components, perplexity=perplexity, learning_rate=learning_rate, random_state=random_state)
    tsne_results = tsne.fit_transform(genotypes)

    return tsne_results