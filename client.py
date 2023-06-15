import socket
from _thread import *
import pickle
from ignore import HOST, PORT

def sockctConn():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print ('>> Connect Server')
    return client_socket

        

def client(client_socket):
    
    data = client_socket.recv(1024)
    
    received = pickle.loads(data)
    
    return received
