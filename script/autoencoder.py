import tensorflow as tf
from tensorflow.keras import layers
import os
import numpy as np
import random

seed = 0
tf.random.set_seed(seed)
np.random.seed(seed)
random.seed(seed)
os.environ['PYTHONHASHSEED'] = str(seed)
os.environ['TF_DETERMINISTIC_OPS'] = '1'
# Define the size of your input data

def perform_autoEncoder(genotypes, n_components=4):
    input_dim = genotypes.shape[1]  # Number of features in your dataset

    encoder = tf.keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(input_dim,)),
        layers.Dense(32, activation='relu'),
        layers.Dense(16, activation='relu'),
        # layers.Dense(8, activation='relu'),
        layers.Dense(n_components, activation='relu'),
        # layers.Dense(2, activation='relu')# This layer represents the encoded representation
    ])

    # Decoder
    decoder = tf.keras.Sequential([
        layers.Dense(16, activation='relu', input_shape=(n_components,)),
        # layers.Dense(32, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(input_dim, activation='tanh')
    ])

    # Autoencoder
    autoencoder = tf.keras.Sequential([encoder, decoder])

    # Compile the model
    autoencoder.compile(optimizer='adam', loss='mse')

    history = autoencoder.fit(genotypes, genotypes,
                          epochs=100,
                          batch_size=1024,
                          shuffle=True,
                          validation_split=0.001,
                          # callbacks=[early_stopping]
                          )  # Add the EarlyStopping callback here
    
    encoded_data = encoder.predict(genotypes)

    return encoded_data