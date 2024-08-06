while True:
    print('Who are you bro?')
    name=input()
    if name !='Joe':
        continue
    print('Hello, Joe.You know you password? (Its a fish.)')
    password=input()
    if password=="swordfish":
        break
print('Access granted.')