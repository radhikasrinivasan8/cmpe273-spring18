#!/usr/local/bin/python3
import zmq
import time
import sys
from threading import Thread

context = zmq.Context()

def push_msgs():
    global context
    sock = context.socket(zmq.PUSH)
    sock.connect("tcp://127.0.0.1:2224")
    name = sys.argv[1]
    client_first_connect = True
    if client_first_connect is True:
        print("User[{}] connected to the chat server".format(name))
        client_first_connect = False
    while True:
        msg_pushed = input("[{}]>".format(name))
        sock.send_string('['+ name +']>' + msg_pushed)
        
def sub_msgs():
    global context
    mock = context.socket(zmq.SUB)
    mock.setsockopt_string(zmq.SUBSCRIBE, '')
    mock.connect("tcp://127.0.0.1:5680")
    while True:
        msg_from_server = mock.recv_string()
        print('\n'  + msg_from_server)


if __name__ == '__main__':    
    t1 = Thread(target=push_msgs).start()
    t2 = Thread(target=sub_msgs).start()
    
    
    




    
    
    
    
    
    
    
    
    
