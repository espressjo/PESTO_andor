#client TCL files to initialize Andor

package require dp

set ip [lindex $argv 0]

set expt [lindex $argv 1]
set nbimages [lindex $argv 2]
set increment [lindex $argv 3]
set basename [lindex $argv 4]
set  path [lindex $argv 5]



set server [dp_MakeRPCClient $ip 5002 ]
#set the conventional mode of the andor 888

dp_RPC $server console::affiche_resultat "Starting acquisition"

set return [ dp_RPC $server acquisition $nbimages $increment $expt $path $basename ]



close $server
puts $return