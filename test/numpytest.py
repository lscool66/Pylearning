import numpy as np
import cv
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x ** 2)

plt.plot(x,y,label = r"$sin(x)$", color="red")
plt.plot(x,z,"b--",label=r"$cos(x^2)$")
plt.title("Pyplot Example")

plt.show()