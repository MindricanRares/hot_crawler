import matplotlib.pyplot as plt
import numpy as np
from time import time
import os
import json
from textwrap import wrap
from collections import OrderedDict

pics_folder_name = 'hot_graphs'
t = time()
with open('output.json', 'r') as f:
    data = json.load(f)
data = OrderedDict(sorted(data.items(), key=lambda kv: kv[1], reverse=True))
sum = 0;
for val in data.values()[10:]:
    sum += val
keys = ['\n'.join(wrap(l, 20)) for l in data.keys()]
x = np.array(range(0, 11))
my_xticks = keys[0:10]
my_xticks.append('other')
plt.xticks(x, my_xticks)
y_values = data.values()[0:10]
y_values.append(sum)
y = np.array(y_values)
plt.plot(x, y)
if not os.path.exists(pics_folder_name):
    os.makedirs(pics_folder_name)
timestr = pics_folder_name + '/' + str(t) + '.png'
plt.savefig(timestr)
