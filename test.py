import  numpy as np

csv=np.loadtxt('dataset/dist.csv',delimiter=',')


dist=csv.tolist()
print(dist)