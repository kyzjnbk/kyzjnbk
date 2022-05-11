# %%
'''
a useful head file for plot
used by "from head_for_plot.py import *"
'''

import h5py as h5
import lsqfit as lsf
import gvar as gv
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

fig_width = 6.75 # in inches, 2x as wide as APS column
gr        = 1.618034333 # golden ratio
fig_size  = (fig_width, fig_width / gr)
plt_axes = [0.1,0.12,0.85,0.8]
errorp = {"markersize": 5, "mfc": "none", "linestyle": "none"} # circle
errorb = {"markersize": 5, "mfc": "none", "linestyle": "none", "capsize": 3, "elinewidth": 1} # circle
errorl = {"markersize": 5, "mfc": "none", "capsize": 3, "elinewidth": 1} # circle with line
fs_p = {"fontsize": 13} # font size of text, label, ticks
ls_p = {"labelsize": 13}

grey = "#808080" 
red = "#FF6F6F" 
peach = "#FF9E6F" 
orange = "#FFBC6F" 
sunkist = "#FFDF6F"
yellow = "#FFEE6F"
lime = "#CBF169"
green = "#5CD25C" 
turquoise = "#4AAB89"
blue = "#508EAD" 
grape = "#635BB1"
violet = "#7C5AB8" 
fuschia = "#C3559F"

color_list = ['orange','dodgerblue','blueviolet','deeppink','indigo','rosybrown','greenyellow','cyan','fuchsia','royalblue', 'red','green','orange','dodgerblue','blueviolet','deeppink','indigo','rosybrown','greenyellow','cyan','fuchsia','royalblue', 'red','green']
fmt_ls = ['o', 'D', 's', '^', 'x', '.']