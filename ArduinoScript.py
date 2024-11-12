import threading

from ArduinoHelper import SetUp
from Paint2D import Draw, Test

def PythonCommandThread(SerialInstance):
    while True:
        command = input("Python is listening and awaiting commands: ")

        SerialInstance.write(command.encode('utf-8'))

        if(command == "EXIT"):
            return 0

if __name__ == "__main__":
    # Do port Setup and communication
    SerialInstance, PortToUse = SetUp()

    SerialInstance.baudrate = 9600
    SerialInstance.port = PortToUse
    SerialInstance.open()

    MasterThread  = threading.Thread(target=PythonCommandThread, args=(SerialInstance,))
    ArduinoThread = threading.Thread(target=Draw, args=(SerialInstance, ))

    MasterThread.start()
    ArduinoThread.start()

    MasterThread.join()
    ArduinoThread.join()

    SerialInstance.close()
    print("Serial Connection has closed")




