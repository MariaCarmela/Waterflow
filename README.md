# Waterflow
Visualization of snapshot of water flowing through a channel

Here how to visualize a snapshot of water flowing through a channel. Winds acting upon the (open) surface of the water create turbulences inside the water. Movements of
water particles (caused by winds) were calculated by students in the first supercomputing class by Prof. Lloyd
Fosdick, University of Colorado, 1992. File “field2.irreg” contains data describing the particle movement in a 2d
slide perpendicular to the length of the channel. Data is given for a regular 82x82 grid in the following format:
starting position (x,y,z) and relative movement (u,v,w).

# Installation
Please install needed packages like this:

pip install numpy
pip install matplotlib

# How to run the project
You can run project in this way:

python waterflow.py

# Output
The output should show up as a window and save as water_flow.png

# Demo
In the folder there's  demo water_flow.png that shows the visualization of data.
