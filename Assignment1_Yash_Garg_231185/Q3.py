import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
arr1=np.arange(-100,101)
arr2=arr1**2
plt.title("Plot of X-Y")
plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.plot(arr1,arr2)
plt.grid()
plt.show()
