def spam():
    eggs='spam local'
    print (eggs) # print local
    
def bacon():
    eggs='bacon local' #bacon local
    print(eggs)
    spam()
    print(eggs) # bacon local
    
eggs='global'
bacon()
print(eggs)# prints goblal