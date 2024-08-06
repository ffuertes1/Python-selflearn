#Now we start using modules in our programs
import random
for i in range(5):
    print(random.randint(1,10))

#Since randint() is in the random
#module, you must first type random. in front of the function name to tell
#Python to look for this function inside the random module. 