from random import choice, shuffle


password = []
# Listas com caracteres para senha (todas STRINGS!)
alphamin = 'a', 'e', 'i', 'o', 'u', 'y', 'w', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'
num = '0','1','2','3','4','5','6','7','8','9'
special = '@','#','$','*'

for abc in range(0, 4):
    password.append(choice(alphamin)) #Adiciona 4 letras na variável password
for n in range(0, 3):
    password.append(choice(num)) #Adiciona 3 números (str) na variável password
for s in range(0, 1):
    password.append(choice(special)) #Adiciona 1 caractere especial na variável password

Maius = password[0]
password.remove(Maius) #Remove o primeiro caractere
shuffle(password) #Mistura a lista
password.insert(0,Maius.upper()) #Adiciona o primeiro caractere só que em maiúsculo.

senha = ''
for a in (password): #Laço para adicionar os caracteres na variável sem aspas
    senha += a 

path = 'secret.txt'
a = open(path, 'at')
a.write(f'\nSenha ---- {senha}') 
a.close()
