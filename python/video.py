import matplotlib.animation as animation
import matplotlib.pyplot as plt
from last_fits import flf
from astropy.io import fits
from astropy.visualization import (ImageNormalize,LinearStretch,ZScaleInterval)
from sys import argv

if len(argv)<2:
    print("Must provid a path.")
    exit(0)
path = argv[1]


fig = plt.figure()
plt.title('Pine Nuts Video V 2.0')
ax1 = plt.subplot2grid((5,5), (0,0), colspan=4,rowspan=4)
ax2 = plt.subplot2grid((5,5), (0,4), rowspan=4,sharey=ax1)
ax3 = plt.subplot2grid((5,5), (4, 0), colspan=4,sharex=ax1)
ax1.set(aspect=1)
plt.tight_layout()

previous_file = " "

def animate(i):
    cf = flf(path)
    global previous_file
    if cf==previous_file or cf==-1:
        i=i
    else:
        try:
            print(cf)           
            hdulist = fits.open(cf)
            data = hdulist[0].data
            norm = ImageNormalize(data,interval=ZScaleInterval(),stretch=LinearStretch())
            hdulist.close()
            ax1.clear()
            ax1.imshow(data,cmap='Greys_r',origin='lower',norm=norm)
        except:
            print("unable to read file ") 
    previous_file = cf

ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
