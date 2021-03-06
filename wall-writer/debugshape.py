#!/usr/bin/env python
# Takes the points from the svg() function in svgparser.py and plots it in matplot lib to see what's going on 

import numpy as np
import pylab as pl
from matplotlib import collections  as mc

#lines = [[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]
lines = [
[(-24, -14), (24, -14)],
[(24, -14), (0, 28)],
[(0, 28), (-24, -14)],
[(-24, 14), (24, 14)],
[(24, 14), (0, -28)],
[(0, -28), (-24, 14)]
]
c = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])

lc = mc.LineCollection(lines, colors=c, linewidths=2)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
pl.show()
