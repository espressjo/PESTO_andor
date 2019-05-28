# --- fichier testcli.tcl : connecte un client RPC
# --- loading the dp module for Audela
llappend auto_path "/usr/local/dp42/"
package require dp
# --- Create a client to connect at the port 5000 of the machine 127.0.0.1
set rpcid [dp_MakeRPCClient 132.204.61.49 5000]
# --- Indique que la console est un serveur :
# --- Send commands to the server
dp_RPC $rpcid console::affiche_erreur "client bien connecte\n"
dp_RPC $rpcid expr \$a+4
