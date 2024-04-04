import socket
import threading

pseudo = input("Pseudo ? : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# première connexion, on envoie le pseudo
client.send(pseudo.encode('utf-8'))

def envoyer(message):
    client.send(message.encode('utf-8'))

def ecrire():
    while True: # faire tourner la demande a l'infinie
        message = ... # demander a l'utilisateur son message
        ... # envoyer le message