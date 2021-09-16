from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl

#define the figure that will be displaied at the end
flowFigure = plt.figure()

#define and plot the x and y axes 
plotAxes = plt.axes()

#use 'jet' as colormap
colors = plt.get_cmap('jet')
  
#normalize colors between 0 and 1
norm = mpl.colors.Normalize(vmin=0, vmax=1) 

#define the colormap to use in the colorbar
sm = mpl.cm.ScalarMappable(cmap='jet', norm=norm)  

#input file
filepath = 'field2.irreg'

# The intuition behind this idea is to read the one line at time and to plot the data line by line until the end. This allows 
# a more scalable solution in the case of large dataset. The idea of saving each line in a  matrix and then plotting that matrix could be
# useful and faster if the dataset is small,like in our case, but could be very memory expensive in case of large dataset.  

# I use the try-except routine in order to consider the dataset with a different header's length
try:
	with open(filepath) as fp:    
	   
	   #read the header
	   N1 = fp.readline() 
	   N2 = fp.readline()
	   dim_X = fp.readline()
	   dim_Y = fp.readline()
	   dim_Z = fp.readline()
	   N3 = fp.readline()
	   line = fp.readline()
	   while line: 
	   
			# split when there is a blank space  
		   ListSplit = line.split(" ")
		   #convert list in array of float value
		   dataArrayFromList = np.asarray(ListSplit, dtype=np.float)
			#compute velocity value
		   length= np.hypot(dataArrayFromList[3] , dataArrayFromList[4]) 
			#plot arrows
		   plotAxes.arrow(dataArrayFromList[0] , dataArrayFromList[1] ,   
					   dataArrayFromList[3] , dataArrayFromList[4] ,
					   fc =colors(norm(length)),clip_on = 1, 
					   head_length=0.009,
					   head_width=0.009,linewidth = 0.01)
			   
		   line = fp.readline()    
	fp.close()
except IOError as err:
    print("I/O error: {0}".format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

	
plt.title("Water Flow")
plt.grid()

#create a colorbar
cb=plt.colorbar(sm)
cb.set_label('Movement(velocity)')
cb.set_ticks([0, 0.5, 1])
cb.set_ticklabels(["0. - slow", "0.5", "1. - quick"])

# save and show the result
flowFigure.savefig('water_flow.png', dpi=500)
plt.show()

