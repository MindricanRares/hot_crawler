import matplotlib.pyplot as plt
import numpy as np
from time import time
number_of_posts = []


t=time()
with open('output.txt', 'r') as f:
    number_of_posts=f.readlines()
x = np.array([0, 1, 2, 3,4,5,6])
y = np.array(number_of_posts)
my_xticks = ['python', 'java', 'sql', 'dotnet','php','android','other']
plt.xticks(x, my_xticks)
plt.plot(x, y)
timestr=str(t)+'.png'
plt.savefig(timestr)
