import serial.tools.list_ports
    
def SetUp():
    ports = serial.tools.list_ports.comports()
    SerialInstance = serial.Serial()

    Ports = []

    for one in ports:
        Ports.append(str(one))
        print(str(one))

    CommunicationPort = input("Select Com Port for Arduino #: ")

    PortToUse = None
    for i in range(len(Ports)):
        if Ports[i].startswith("COM" + str(CommunicationPort)):
            PortToUse = "COM" + str(CommunicationPort)
            print(PortToUse)
    
    return SerialInstance, PortToUse