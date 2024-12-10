import numpy as np
import matplotlib as mt
import matplotlib.pyplot as plt
plt.hist(np.random.randn(100), bins = 20)
plt.grid()
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of Random Values")
plt.show()