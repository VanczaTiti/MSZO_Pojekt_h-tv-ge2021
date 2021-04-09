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
    #print(sList)
    pozY=float(sList[0]) # [m]
    pozX=float(sList[1])
    velY=float(sList[2]) # [m/s]
    velX=float(sList[3])
    rot=float(sList[4]) # [deg]
    angVel=float(sList[5]) # [deg/s]
    ###########################################################################
    
    

  
  
    
 
    
 
    
 
    
 
    
    trustTarget=1600       #[kN]
    engineAngleTarget=0   # [deg] A rakéta testéhez viszonyítva
    wingAngleTarget=90    # [deg] 0-> maxra kinyitva, 90-> teljesen rásimul a testre
    ##########################################################################
    sendStr=str(trustTarget) +";"+ str(engineAngleTarget/180*3.14)+";"+str(wingAngleTarget/180*3.14)
    print(sendStr)
    socket.send(str.encode(sendStr))
    
