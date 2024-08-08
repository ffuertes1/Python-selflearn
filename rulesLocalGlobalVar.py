# This exampples declares that the global stattement
#for the variable eggs in the spam function will
#convert all global and will print the one inside this spam() function

def spam():
    global eggs
    eggs= 'spam ' # this is the global

def bacon():
    eggs='bacon ' # this is local
    
def ham():
    print (eggs)# this is the global
    
eggs=42 # this is the global
spam()
print (eggs)


#In the spam() function, eggs is the global eggs variable, because there’s 
# a global statement for eggs at the beginning of the function. In bacon(),
# eggs is a local variable, because there’s an assignment statement for it in
# that function. In ham(), eggs is the global variable, because there is no
# assignment statement or global statement for it in that function. 
# 