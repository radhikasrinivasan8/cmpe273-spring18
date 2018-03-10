#!/usr/local/bin/python3
import zmq
import sys

def pull_msgs():
    context = zmq.Context()
    sock = context.socket(zmq.PULL)
    sock.bind("tcp://127.0.0.1:2224")
    
    mock = context.socket(zmq.PUB)
    mock.bind("tcp://127.0.0.1:5680")
    while True:
        message_pulled = sock.recv_string()
        #print(message_pulled)   
        mock.send_string(message_pulled)
        
if __name__ == '__main__':    
    pull_msgs()
    
