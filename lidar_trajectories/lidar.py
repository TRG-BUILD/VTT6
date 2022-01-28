import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import helpers

# 1) read the config file, create variables from dict entries 
#  if necessary

###---YOUR SOLUTION HERE-----------------------------------

###--------------------------------------------------------

# 2) read the ortophoto and plot it with correct boundaries,
#  add title and labels for x and y axes

###---YOUR SOLUTION HERE-----------------------------------

###--------------------------------------------------------

# 3) use helpers.det_region_to_utm to transform the detection
# region from sensor coordinates to UTM coordinates. Plot the
# sensor location and the detected region location on top of the
# ortophoto. Put the labels into plotting functions and
# add the legend too

###---YOUR SOLUTION HERE-----------------------------------

###--------------------------------------------------------

# 4) read the data file with per frame objects detected. Implement
#   and use helpers.data_to_tracks to convert the data to tracks,
#   a track is a dictionary with

###---YOUR SOLUTION HERE-----------------------------------

###--------------------------------------------------------

# this line will display all plots you defined above
plt.tight_layout()
plt.show()