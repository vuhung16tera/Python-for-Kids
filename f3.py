# function and graph with multiple if conditions

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([-20, -10, 0, 10, 20])

if xpoints < 0:
  ypoints = -np.array(2*xpoints)

# https://researchdatapod.com/python-valueerror-the-truth-value-of-an-array-with-more-than-one-element-is-ambiguous-use-a-any-or-a-all/
if xpoints == 0:
    ypoints = np.array(0)

if xpoints > 0:
    ypoints = np.array(3)

plt.plot(xpoints, ypoints)
plt.show()

