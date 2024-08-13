import pprint
message= 'It was a bright cold day in April, and the clocks were striking thirteen.'
count={}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
    
print(pprint.pformat(count))

#The setdefault() method is a nice 
# shortcut to ensure that a key exists.
# Here is a short program that counts the 
# number of occurrences of each letter in a string.