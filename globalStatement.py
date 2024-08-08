#Example of a global statement 
#If we have a line such as 'global "variable"' at top of a function 
#it will read like: in this function this variable is global, so dont create a local variable with this name


def spam():
    global eggs
    eggs='spam'
    
eggs='global'
spam()
print(eggs)