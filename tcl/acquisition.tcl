proc acqui {nbImage inc_start expt fld racine} {
#this function while acquire N images and save them in the a specific folder
	#nbImage:	number of images
	#inc_start:	start increment. image with the same name will be deleted
	#expt:		exposure time
	#fld:		folder where to save the images 
	#racine:	file prefix 
#a few display message
console::affiche_erreur "setting exposure time to : $expt s"
console::affiche_erreur "nbImage: $nbImage\n"
console::affiche_erreur "increment de depart: $inc_start\n"

#set the exposure time
cam1 exptime $expt

#set the start and stop increment
set start $inc_start
set stop [ expr {$inc_start + $nbImage } ]

#check if the folder exist, if not create it
file mkdir "Z:$fld"
#main acquisition loop
global stop_acq
set stop_acq 0
for {set k $start} {$k<$stop} {incr k} {

	global stop_acq
	if {$stop_acq == 1} {
		break
	}
console::affiche_erreur "image $racine\_$k.fits saved\n"
cam1 acq -blocking
set inc  [format %2.10d $k]
saveima "Z:$fld$racine\_$inc.fits"
}
global stop_acq
set stop_acq 0
}
