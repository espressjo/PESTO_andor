global a 
set a 1
puts "a out: $a"
proc test args {
       global a
       puts "a in : $a"
       puts "set a = 2"
       set a 2
       
       puts "a in: $a"
 }

test  1 
puts "a out: $a"
