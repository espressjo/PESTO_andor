#client TCL files to initialize Andor

package require dp

set arg1 [lindex $argv 0]

set server [dp_MakeRPCClient $arg1 5002 ]
#set the conventional mode of the andor 888

dp_RPC $server console::affiche_resultat "Setting camera in conventional mode"
set return [ dp_RPC $server cam1 electronic 1 0 1 2 0 1]

close $server
puts $return