#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

#import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    #print("Received request: %s" % message)
    sting=message.decode("utf-8")
    sList=sting.replace(',','.').split(";")
    print(sList)
    pozY=float(sList[0]) # [m]
    pozX=float(sList[1])
    velY=float(sList[2]) # [m/s]
    velX=float(sList[3])
    rot=float(sList[4]) # [deg]
    angVel=float(sList[5]) # [deg/s]
    ###########################################################################

    
    cY=6000
    pY=-60
    pYabsX=1
    dY=-500

    pX=0.05
    dX=0.2
    
    
    targetRot=pX*pozX+dX*velX 
    
    trustTarget=cY+pY*pozY+dY*velY+pYabsX*abs(pozX) #[kN]
    engineAngleTarget=(targetRot-rot/50) # [rad] A rakéta testéhez viszonyítva
    #trustTarget=0
    #engineAngleTarget=0
    ##########################################################################
    sendStr=str(1600) +";"+ str(-angVel/60)+";"+str(0)#str((rot+115)/30)
    print(sendStr)
    socket.send(str.encode(sendStr))