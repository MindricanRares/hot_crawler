import imageio
import numpy as np
import os
import time
import subprocess

files = []
folders = []
for (path, dirnames, filenames) in os.walk('hot_graphs'):
    folders.extend(os.path.join(path, name) for name in dirnames)
    files.extend(os.path.join(path, name) for name in filenames)

images=[]

for filename in files:
    images.append(imageio.imread(filename))
imageio.mimsave('test.gif',np.array(images),)