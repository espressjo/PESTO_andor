# --- fichier testser.tcl : installe un serveur RPC
# --- loading the dp module for Audela
package require dp
# --- Create a Server for the port 5000
set rpcid [dp_MakeRPCServer 5000]
# --- Indique que la console est un serveur :

# --- Initialize the a variable
set a 5
