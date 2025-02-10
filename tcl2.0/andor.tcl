#this is the main server file,
#this should be launched by Audela terminal
#This script shouldl be visible from Audela
#once the remote (linux) folder is mounted
#on the window machine.


package require dp
global exit_flag
set exit_flag 0
global stop_acq
set stop_acq 0

proc set_abort_flag {} {
    global stop_acq
    set stop_acq 1
    return "abort triggered"
}

proc acquisition {nbImage inc_start expt fld racine} {
#this function while acquire N images and save them in the a specific folder
	#nbImage:	number of images
	#inc_start:	start increment. image with the same name will be deleted
	#expt:		exposure time
	#fld:		folder where to save the images 
	#racine:	file prefix 
#a few display message
console::affiche_resultat "setting exposure time to : $expt s"
console::affiche_resultat "nbImage: $nbImage\n"
console::affiche_resultat "increment de depart: $inc_start\n"

#set the exposure time
cam1 exptime $expt

#set the start and stop increment
set start $inc_start
set stop [ expr {$inc_start + $nbImage } ]

#check if the folder exist, if not create it
file mkdir "Z:$fld"
#main acquisition loop


for {set k $start} {$k<$stop} {incr k} {
    global status_cam1
	global stop_acq
    global exit_flag
	if {$stop_acq == 1} {
		break
	}
    console::affiche_resultat "Starting sequence\n"
    
    cam1 acq 
    after 500 ;
    while {1} {
        console::affiche_resultat "Integrating ...\n"
        after 200  ;# Prevents excessive CPU usage (1-second delay)
        if {$stop_acq ==1 } {
            cam1 stop
            set exit_flag 1

        }
        if {$status_cam1 eq "stand"} {
            console::affiche_resultat "done ..."
            break
        }
    }
    if {$exit_flag eq 1 } {
        break
    }
    
    set inc  [format %2.10d $k]
    console::affiche_resultat "Saving:  Z:$fld$racine\_$inc.fits"
    saveima "Z:$fld$racine\_$inc.fits"
}

global stop_acq
set stop_acq 0
return 0
}



console::affiche_resultat "Server is running on port 5002 & 5003..."
dp_MakeRPCServer 5002
dp_MakeRPCServer 5003
