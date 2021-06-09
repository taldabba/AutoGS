import time
import threading


class timerThread:
    def __init__(self,seconds,state):
        self.threadState = state
        self.seconds = seconds
        self.t = threading.Thread(target = self.threadTimer,args=(self.seconds,))

    def checkIfAlive(self):
        t = self.t
        if t.is_alive():
            return True
        else:
            return False
        
    def threadTimer(self,seconds):
        
        time.sleep(seconds)
        print("Abdo Abdo")
        
    def startThread(self):
        t= self.t
        t.start()

# myT = timerThread(0,False)

# while True:

#     if not myT.checkIfAlive():    
#         x = int(input("how long timer?: "))
#         myT = timerThread(x,False)
#         myT.startThread()
##    break
##def tTimer(seconds):
##    time.sleep(seconds)
####def checkThreadStatus(t)
##
##t= threading.Thread()


class sensorQueue:
    def __init__(self):
        self.que = []
        self.latestValue = 0
    def add(self,newValue):
        self.que.clear()
        self.que.append(newValue)
        self.latestValue = newValue
    def get(self):
        if not self.que:
            return self.latestValue
        value = self.que.pop()
        return value


bruh = sensorQueue()


print(len(bruh.que))
