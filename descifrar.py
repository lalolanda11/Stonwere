from cryptography.fernet import Fernet
import os
#Se carga la llave para desencriptar los archivos
def cargar_key():
    return open('key.key', 'rb').read()

def decrypt(items, key):
    f = Fernet(key)
    #for item in items:
    for a,b,c in os.walk(items):
        for s in c:

            with open(a+'/'+s, 'rb') as file:
                file_data = file.read()
            decrypted_data = f.decrypt(file_data)
            with open(a+'/'+s, 'wb') as file:
                file.write(decrypted_data)

if __name__=='__main__':
    ruta = input('Ruta : ')#"/home/kali/Desktop/Ataque/spam_box" 
#'C:\\Users\\'
    items = os.listdir(ruta)
    key = cargar_key()
    decrypt(ruta,key)
