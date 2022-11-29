def index(starcount = 3 ):
    phone = input("enter your phone number: ")
    inputphone = phone 
    if len(str(inputphone)) != 11 :
        print("your number is wrong ")
        inputphone = input(f'enter the correct one: ')

    elif len(phone) == 11:
          prefix = phone [0:4] 
          suffix  = phone [-4::1]
          starForm =  f'{prefix}{starcount * "*"}{suffix}'
          return starForm

    return inputphone 

print(index())

