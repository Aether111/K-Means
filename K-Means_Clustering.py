import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
N = 4000
while True:
    try:
        k = int(input('Please choose the number of centroids:'))
        if k <= 0 or k > N:
            raise ValueError
        break
    except ValueError:
        print("You need a positive integer:")
temp = make_blobs(n_samples=N, n_features=2, centers=k, cluster_std=1, random_state=445)
x = temp[0]
rng = np.random.default_rng()
y = x[rng.choice(N,size = k,replace = False)]
s = y.copy() + 1
def mem(x,y):
    for r in range(N):
        f = np.empty(len(y))
        for h in range(len(y)):
            g = np.zeros(len(x[r]))
            for i in range(len(x[r])):
                g[i] = (x[r][i] - y[h][i])**2
            f[h] = np.sqrt(np.sum(g))
        m[np.argmin(f)].append(x[r])
while np.array_equal(s,y) == False:
    m = [[] for v in range(len(y))]
    mem(x,y)
    s = y.copy()
    for i in range(k):
        y[i] = np.mean(m[i],axis=0)
plt.scatter(x[:,0],x[:,1],marker='.',s=10)
plt.scatter(y[:,0],y[:,1],color='orange')
