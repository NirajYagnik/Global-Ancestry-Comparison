# Global-Ancestry-Comparison
Project that compares a bunch of methods for global ancestry in python

- Niraj Yagnik, Vivek Sharma, Jay Jhaveri


## Dimensionality Models tested
1. **PCA** (Principal Component Analysis): Transforms data into principal components, capturing maximum variance with fewer dimensions.
2. **UMAP** (Uniform Manifold Approximation and Projection): Reduces dimensions based on manifold learning, preserving local and global data structure.
3. **t-SNE** (t-Distributed Stochastic Neighbor Embedding): Reduces data to two or three dimensions, emphasizing on keeping similar instances close.
4. **MDS** (Multidimensional Scaling): Visualizes data similarity in a low-dimensional space, aiming for similar objects to be plotted closely.
5. **Isomap** (Isometric Mapping): Computes a low-dimensional embedding by preserving geodesic distances, maintaining the data's geometric structure.
6. **Autoencoders**: Neural networks that learn compressed representations of input data, aiming for dimensionality reduction through unsupervised learning.


## Steps to run

We have compiled all the code at one place in main.ipynb file. It contains the plots for all the dimensionality reduction algorithms running with the best hyperparameters we received for them all.

Steps to run on your local machine:

1. (A new virtual environment recommended) `pip install -r requirements.txt`
2. Download all preprocessed raw zip files from this drive [link](https://drive.google.com/drive/folders/1x_wgb0GMv1P-MgQGI-pufjn-XgcSToi8?usp=sharing)
    - Extract each of them in the src folder.
3. Open main.ipynb
4. You can now press run all in the jupyter notebook (approx run time 6-7 mins).
    - At start, it will ask you to input a chromosome number of your choice from the preprocessed files.
5. At the end you can visualize and compare each of the dimensionality reduction algorithms with each other.
6. OPTIONAL: You may use the following plink command to create raw files for other chromosomes too.
    ```
     plink \
    --vcf ~/public/pca-exercise/1000G_mgymrek_merged.vcf.gz \
    --recode A \
    --maf 0.05 \
    --chr 16 \
    --out 1kg_chr16_pca_recode
    ```
