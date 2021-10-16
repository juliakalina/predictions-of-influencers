# -*- coding: utf-8 -*-
"""Kmeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15bBLs-yaEGka72gTVL_G3s2Y6utHU2RO
"""

from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd
#df = pd.read_excel("/content/gdrive/My Drive/database_1.xlsx")
df = pd.read_csv("/content/gdrive/My Drive/database_2.csv")
df.head()

df = df.drop('number_of_symbols', axis=1)
df.head()

from sklearn.preprocessing import StandardScaler
import numpy as np
x = df.values[:,1:]
x = np.nan_to_num(x)
x

Clus_dataSet = StandardScaler().fit_transform(x)
Clus_dataSet

from sklearn.cluster import KMeans
k_means = KMeans(init = 'k-means++', n_clusters = 3, n_init = 12)
k_means.fit(x)
labels = k_means.labels_
print(labels)

df['Clus_num'] = labels
X = df.drop("Clus_num", axis = 1)
Y = df["Clus_num"]
df.head(5)

df.groupby('Clus_num').mean()

from imblearn.over_sampling import SMOTE

sm = SMOTE(kind='regular',k_neighbors=1)
#random_state = 42
x_res, y_res = sm.fit_sample(X, Y.ravel())
print(f'''Shape of X before SMOTE: {X.shape}
Shape of X after SMOTE: {x_res.shape}''')

import matplotlib.pyplot as plt
area = np.pi * (x_res[:, 1])**2
plt.scatter(x_res[:, 1], x_res[:, 2], c=y_res.astype(np.float))
plt.xlabel('followers', fontsize=20)
plt.ylabel('number of posts', fontsize=20)
plt.show()