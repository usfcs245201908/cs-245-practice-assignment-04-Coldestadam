#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:08:39 2019

@author: adam
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000,
              450000, 500000])

insertion = np.array([230, 859, 1937, 3698, 5581, 8466, 11079, 14820,
                      20856, 22245])
bubble = np.array([3875, 15868, 32204, 60686, 103116, 128705, 172854,
                   225130, 287447, 351336])
selection = np.array([589, 2316, 5646, 9805, 15247, 21094, 29674, 40114,
                      47585, 57826])

plt.plot(x, insertion, label='insertion')
plt.plot(x, bubble, label='bubble')
plt.plot(x, selection, label='selection')
plt.axis([0, 500000, 0, 400000])
plt.xlabel('Size of the Array')
plt.ylabel('Time(ms)')
plt.legend()
plt.savefig("graph.pdf", format='pdf')
plt.show()
