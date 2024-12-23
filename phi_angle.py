# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:12:15 2021

@author: lorenzmath92
"""

import numpy as np


def phi_angle(inp_angle):
    phi = -2*np.arctan((-4*L2*e + 2*L2*f + np.sqrt(-Bx**4 + 2*Bx**2*L1**2 + 2*Bx**2*L2**2 - 2*Bx**2*e**2 + 4*Bx**2*e*f - 2*Bx**2*f**2 - L1**4 + 2*L1**2*L2**2 + 2*L1**2*e**2 - 4*L1**2*e*f + 2*L1**2*f**2 - L2**4 + 2*L2**2*e**2 - 4*L2**2*e*f + 2*L2**2*f**2 - e**4 + 4*e**3*f - 6*e**2*f**2 + 4*e*f**3 - f**4))/(Bx**2 + 2*Bx*L2 - L1**2 + L2**2 + e**2 - 2*e*f + f**2)), 2*np.arctan((4*L2*e - 2*L2*f + np.sqrt(-Bx**4 + 2*Bx**2*L1**2 + 2*Bx**2*L2**2 - 2*Bx**2*e**2 + 4*Bx**2*e*f - 2*Bx**2*f**2 - L1**4 + 2*L1**2*L2**2 + 2*L1**2*e**2 - 4*L1**2*e*f + 2*L1**2*f**2 - L2**4 + 2*L2**2*e**2 - 4*L2**2*e*f + 2*L2**2*f**2 - e**4 + 4*e**3*f - 6*e**2*f**2 + 4*e*f**3 - f**4))/(Bx**2 + 2*Bx*L2 - L1**2 + L2**2 + e**2 - 2*e*f + f**2))
    return phi[1]


