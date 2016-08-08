import os
import nester

target = ["danile", "michael", ["aj","dk"]]
#print(target)
nester.print_lol(target, True, 3)

print(os.getcwd())

###
data = open("sketch.txt")
for each_line in data:
    try:
        (role, line_spoken) = each_line.split(":")
        #print(each_line, end="")
        print(role, end="")
        print(" said: ", end="")
        print(line_spoken, end="")
    except:
        pass
    
data.close()