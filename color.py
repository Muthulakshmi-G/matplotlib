import numpy as np
import matplotlib.pyplot as plt
n=100
r=2*np.random.rand(n)

theta=2*np.pi*np.random.rand(n)

area=200*r**2*np.random.rand(n)

colors=theta


c2=plt.scatter(theta,r,c=colors,s=area,cmap=plt.cm.RdGy)


plt.show(c2)
