TARGET = fwandor

CFLAGS = -std=c++11
INCL = -I./
CC = g++

%.o: %.cpp
	$(CC) $(CFLAGS) $(INCL) -c $< -o $@
OBJS = main.o \
			 socket.o \
			 fwandor.o 

#echo "compiling..."
all: $(OBJS)
	$(CC) $(CFLAGS) $(INCL) $(OBJS) -o $(TARGET)
clean:
	@rm -f $(OBJS) $(TARGET)
install:
	@cp $(TARGET) /usr/local/bin/ 

