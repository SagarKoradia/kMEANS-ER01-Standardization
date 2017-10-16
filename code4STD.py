from numpy import genfromtxt
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
#import matplotlib.pyplot as plt
fn = r'C:\Users\DELL I5558\Desktop\Python\NSW-ER01.csv'
my_data = genfromtxt(fn, delimiter=',')
scaler = StandardScaler()
model = KMeans(n_clusters=4)
pipeline = make_pipeline(scaler, model)
labels = pipeline.fit_predict(my_data)
print(type(labels))
print(len(labels))
day_type = ['SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SPRING','SPRING', 'SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','SUMMER','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','AUTUMN','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER','WINTER']
print(type(day_type))
print(len(day_type))
print(day_type)
dff = pd.DataFrame({'labels': labels, 'day_type': day_type})
ct = pd.crosstab(dff['labels'], dff['day_type'])
print(ct)
