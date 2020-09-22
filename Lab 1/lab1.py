import numpy as np
import matplotlib.pyplot as plt
import copy as cp

dots = 100000
b = 25
d_list = 20

normal_list = []
for i in range(0, dots):
    l = np.random.uniform(-b, b, d_list)
    normal_list.append(np.sum(l) / 2)

triangular_list = []
for i in range(0, dots):
    l = np.random.uniform(-b, b, 2)
    triangular_list.append((6**.5) / 2 * (np.sum(l)))

bin1 = []
for i in range(-100, 100, 1):
    bin1.append(i)

bin2 = []
for i in range(-75, 75, 1):
    bin2.append(i)


plt.hist(normal_list, bins=bin1)
plt.savefig("Gauss_20.jpg")
plt.show()
plt.clf()
plt.hist(triangular_list, bins=bin2)
plt.savefig("Triangle-100k.jpg")
plt.show()
