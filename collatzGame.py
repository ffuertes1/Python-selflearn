print('Enter a positive integer number: ')
number=input()
number=int(number)

def collatz(number):
    if number>0 and number%2==0:
        result= (number//2)
    elif number>0 and number%2!=0:
        result= (3*number+1)
    else:
        print('Number it invalid')
        return number
    print(result)
    return result

while number!=1:
    number=collatz(number)
        
    
        
            
            
    

    