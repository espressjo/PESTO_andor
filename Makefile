BASE = /opt/andor.22.04
folders:
	@mkdir -f $(BASE)/
	@mkdir -f $(BASE)/bin/
	@mkdir -f $(BASE)/config/
	@mkdir -f $(BASE)/data/
	@mkdir -f $(BASE)/python/

all:
	@cd ./C++/ && make all
clean:
	@cd ./C++/ && make clean
install: folders
	@cp ./C++/filterwheel/src/fwandor $(BASE)/bin/ #copy binary filterwheel
	@cp ./python/*.py $(BASE)/python/

install-tclsh85:
	@cd dependencies && make install
