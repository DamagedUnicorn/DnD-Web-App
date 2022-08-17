#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 23:36:57 2022

@author: thorknudsen
"""

import numpy as np

def roll(amount, dice):
	if dice not in [4, 6, 8, 10, 12, 20, 100]:
		raise ValueError("invalid dice!")

	arr = np.random.randint(low=1, high=dice+1, size=amount)

	return (arr, arr.sum())
