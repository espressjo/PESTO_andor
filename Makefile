BASE = /opt/andor.22.04
folders:
	@mkdir -p $(BASE)/
	@mkdir -p $(BASE)/bin/
	@mkdir -p $(BASE)/config/
	@mkdir -p $(BASE)/data/
	@mkdir -p $(BASE)/python/

all:
	@cd ./C++/ && make all
clean:
	@cd ./C++/ && make clean
install: folders
	@cp ./C++/filterwheel/fwandor $(BASE)/bin/ #copy binary filterwheel
	@cp ./tcl2.0/*.py $(BASE)/python/
	@cp ./tcl2.0/andor.tcl /home/andor/

install-tclsh85:
	@cd dependencies && make install
