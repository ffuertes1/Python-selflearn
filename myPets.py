myPets=['Sophie','Pooka,''Fat-tail']
print('Enter a name for a pet :')
name=input()
if name not in myPets:
    print('I dont have a pet name like that  '  + name)
else:
    print(name +' is my pet.')
    
    