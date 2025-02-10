A make file is already provided to install
tclsh8.5. That should go well

You also need to install dp42.
Start by creating some symbolic link;
cd /opt/tclsh8.5/bin/
ln -s tclsh8.5 tclsh
cd /opt/tclsh8.5/lib
ln -s libtcl8.5.so libtcl.so
ln -s libtclstub8.5.a libtclstub.a
Untar the tcldp package. 
cd ./tcldp-4.2.0

first you will need to

modify CMakeList.txt to make sure "set(TCL_HOME /opt/tclsh8.5)" shows
where tclsh8.5 has been installed. If the line does not exist, add it!!!!

cmake -DCMAKE_INSTALL_PREFIX=/opt/tcldp .
make
make install

Then, find /opt -name pkgIndex.tcl
add the line lappend auto_path /opt/tcldp # this will load dp when tclsh is opened.

then export LD_LIBRARY_PATH=/opt/tclsh8.5/lib 

/opt/tclsh8.5/bin/tclsh #to start tclsh
