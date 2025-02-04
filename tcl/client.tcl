#client.tcl
lappend auto_path "/usr/local/dp42/"
package require dp
# --- Cree un client connecte au port 5000 de la machine 132.204.61.49
global rpcid
set rpcid(client) [dp_MakeRPCClient 132.204.61.46 5002]
# --- Envoi un message de connexion a afficher sur la console du serveur
dp_RPC $rpcid(client) console::affiche_resultat "client bien  connecte\n"
# --- Fonction pour envoyer des messages a executer par le serveur

proc send { arg } {
global rpcid
dp_RPC $rpcid(client) console::affiche_resultat "Execute : $arg \n"
set message "dp_RPC $rpcid(client) eval_client \{ $arg \}"
eval $message
}
# --- Fonction d'analyse du message de retour eventuel du serveur
proc eval_serveur { arg } {
	uplevel $arg
}
# --- Cree un port serveur numero 5001 pour permettre au serveur
# --- de renvoyer des ordres au client
set rpcid(serveur) [dp_MakeRPCServer 5003]


# --- Demande au serveur de se connecter au "serveur" du client
send {set rpcid(client) [dp_MakeRPCClient 132.204.61.46 5003]}

