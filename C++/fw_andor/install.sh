echo "compiling..."
g++ -c fwandor.cpp main.cpp socket.cpp 
g++ *.o -o fwandor
echo "cleaning"
rm *.o
mv fwandor /usr/local/bin/

