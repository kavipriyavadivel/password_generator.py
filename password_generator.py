import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','W','Z']
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$','%','*','(',')',',','.']
password=""
passwords=""
print("Welcome to password generator")
no_letter=int(input("How many letters do you want? "))
no_number=int(input("How many numbers do you want? "))
no_symbol=int(input("How many symbols do you want? "))
for i in range(no_letter):
  char=random.choice(letters)
  password=password+' '+char
for i in range(no_number):
  char=random.choice(number)
  password=password+' '+char
for i in range(no_symbol):
  char=random.choice(symbol)
  password=password+' '+char
change_password=password.split(' ')
random.shuffle(change_password)
for i in change_password:
  passwords=passwords+i
print(f"Your password is: {passwords}")