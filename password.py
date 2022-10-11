from random import choice, shuffle
password = []
alphamin = 'a', 'e', 'i', 'o', 'u', 'y', 'w', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'
num = '0','1','2','3','4','5','6','7','8','9'
special = '@','#','$','*'

for abc in range(0,4):
    password.append(choice(alphamin))
for n in range(0,3):
    password.append(choice(num))
for s in range(0, 1):
    password.append(choice(special))


Maius = password[0]
password.remove(Maius)
shuffle(password)
Maius = Maius.upper()
password.insert(0,Maius)


senha = ''

path = 'secret.txt'
for a in (password):
    senha += a

a = open(path, 'at')
a.write(f'\nSenha ---- {senha}') 
a.close()
