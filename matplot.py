import matplotlib.pyplot as plt

import numpy as np

x=np.linspace(-4,4,50)
y=3*x+4
y1=x**2
plt.figure(num=1,figsize=(7,6))
plt.plot(x,y)
plt.plot(x,y1,color='red',linewidth=3.0,linestyle='--')


plt.figure(num=2)
plt.plot(x,y1)

plt.show()