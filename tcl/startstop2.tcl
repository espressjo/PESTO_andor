lappend auto_path "/usr/local/dp42/"
package require dp
global rpcid_stop

set rpcid_stop [dp_MakeRPCClient 132.204.61.46 5004]

proc start args {
	global rpcid_stop
	dp_RPC $rpcid_stop set stop_acq 0
}
proc stop args {
	global rpcid_stop
	dp_RPC $rpcid_stop set stop_acq 1
}
