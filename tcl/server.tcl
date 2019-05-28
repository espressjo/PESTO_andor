#fichier : serveur.tcl

global rpcid
global stop_acq
set stop_acq 0
#lappend auto_path "/usr/local/dp42/"
package require dp

#on crée le port
set rpcid(serveur) [dp_MakeRPCServer 5002]
set rpcid_stop [dp_MakeRPCServer 5004]

#quelque fonction
proc eval_client { arg } {
uplevel $arg
}

proc send { arg } {
global rpcid
dp_RPC $rpcid(client) console::affiche_resultat "Execute: $arg \n"
set message "dp_RPC $rpcid(client) eval_serveur \{ $arg \}"
eval $message

}



