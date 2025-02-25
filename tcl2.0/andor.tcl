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
global increment
set increment 1
global night 
set night ""

proc get_night {} {
    global night
    return $night
}
proc set_night {n} {
    global night
    set night $n
    return $night
}
proc set_increment {inc} {

    global increment
    set increment $inc
    return $increment
}
proc get_increment {} {
    global increment
    return $increment
}



proc set_abort_flag {} {
    global stop_acq
    set stop_acq 1
    return "abort triggered"
}

proc acquisition {nbImage expt fld racine} {
#this function while acquire N images and save them in the a specific folder
	#nbImage:	number of images
	#inc_start:	start increment. image with the same name will be deleted
	#expt:		exposure time
	#fld:		folder where to save the images 
	#racine:	file prefix 
#a few display message
global increment
console::affiche_resultat "setting exposure time to : $expt s"
console::affiche_resultat "nbImage: $nbImage\n"
console::affiche_resultat "increment de depart: $increment\n"

#set the exposure time
cam1 exptime $expt

#set the start and stop increment
set start $increment
set stop [ expr {$start + $nbImage } ]

#check if the folder exist, if not create it
file mkdir "Y:$fld"
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
    set increment [ expr {$increment + 1} ]
    set inc  [format %2.10d $increment]
    console::affiche_resultat "Saving:  Y:$fld$racine\_$inc.fits"
    saveima "Y:$fld$racine\_$inc.fits"
}

global stop_acq
set stop_acq 0
return 0
}


proc addHeader { KW VALUE TYPE COMMENT} {

    if {$TYPE eq "string"} {
        buf1 setkwd [list $KW $VALUE string $COMMENT ""]
    } elseif {$TYPE eq "float"} {
        buf1 setkwd [list $KW $VALUE float $COMMENT ""]
    } elseif {$TYPE eq "int"} {
        buf1 setkwd [list $KW $VALUE int $COMMENT ""]
    }

}
proc test {test} {


    return $test
}




console::affiche_resultat "Server is running on port 5002 & 5003..."
dp_MakeRPCServer 5002
dp_MakeRPCServer 5003
