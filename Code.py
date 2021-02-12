import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

xposition = range(0, 21)
data = (7.866, 8.366, 9.166, 9.233, 8.433, 8.6, 8.2, 8.633, 8.1, 8.066, 8.133, 8.266, 8.4, 7.33, 8.033, 7.7, 7.83, 6.96, 7.667)

Histo = pd.DataFrame({'heigh_f': xposition, 'height_m': data})

plt.hists(Histo)
plt.plot(Histo)
plt.show()
