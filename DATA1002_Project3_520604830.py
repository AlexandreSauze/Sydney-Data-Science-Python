# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N-qty7kXuV-5j7vCWVqa9eK2340AVoMu
"""

import pandas as pd
from math import sqrt
from sklearn import metrics
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from tabulate import tabulate
from numpy.core.fromnumeric import mean

df = pd.read_csv('SDG_goal3_clean.csv')
X = df[list(df.columns)[3:]]      # slice dataFrame for input variables
y = df['Region']        # slice dataFrame for target variable
# Data Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1201) # 70% training 30% test

# We choose 4 neighbours to get a better result
neigh = neighbors.KNeighborsClassifier(n_neighbors=4).fit(X_train, y_train)

# We will use row 150 as a sample
sample = list(df.iloc[150][3:])        # We use row 150 of the dataframe to confirm
sample_pred = neigh.predict([sample])
print('----- Sample case -----')
print('Original Region:', df.iloc[150][2])
print('Predicted Region:', sample_pred[0])
print('-----------------------')

# Use the model to predict X_test
y_pred = neigh.predict(X_test)
# Compare predicted values vs actual values
print('Accuracy Score (Proportion):', metrics.accuracy_score(y_test, y_pred))

# Compare different k values with different seeds to simulate different events
ks = [1,2,3,4,5,6,7,8,9,10]
seeds = [1201,3063,4267,1560,1329]
results = []
columns= []
tf = True
c = 0
for seed in seeds:
  columns.append(seed)
  for k in ks:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed)
    neigh = neighbors.KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    y_pred = neigh.predict(X_test)
    if tf:
      results.append([metrics.accuracy_score(y_test, y_pred)])
      tf = False
    else:
      results[c].append(metrics.accuracy_score(y_test, y_pred))
  tf = True
  c += 1

columns.append("Average Accuracy")
av = {}
tf = True
for lis in results:
  if tf:
    c = 0
    for v in lis:
      av[c] = [v]
      c += 1
    tf = False
  else:
    c = 0
    for v in lis:
      av[c].append(v)
      c += 1

av
best = []
c = 0
for s in av:
  best.append(mean(av[c]))
  c += 1
results.append(best)

print(tabulate(results, headers=column, tablefmt="fancy_grid", showindex=columns))