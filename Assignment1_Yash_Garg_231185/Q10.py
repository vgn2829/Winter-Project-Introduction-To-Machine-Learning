import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mt
np.random.seed(42)
x = np.random.randint(0,50,10)   
y = np.random.randint(0,500,10) 
plt.scatter(x, y, color='purple', marker='*')

# Adding titles and labels
plt.title("Scatter Plot of Two Numerical Variables")
plt.xlabel("Variable X")
plt.ylabel("Variable Y")

# Display the plot
plt.grid()
plt.show()
