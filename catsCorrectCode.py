catsName=[] # creating the list
while True:
    print ('Enter the name of cat ' + str(len(catsName)+1)+'(Or enter nothing to stop)')
    name=input()
    if name=='':
        break
    catsName=catsName+[name] #List concadenation    
print('The cat names are: ')
for name in catsName:
    print('  '+name)