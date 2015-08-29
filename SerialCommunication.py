import serial
import sys
from _curses import ERR

class SerialCommunication:
    
    # Static Variables
    SERIAL_COMMUNICATION_DEFAULT_SERIAL_BAUD_RATE   = 115200    
    SERIAL_COMMUNICATION_DEFAULT_SERIAL_TIMEOUT     = 10.0
    
    SERIAL_COMMUNICATION_OPEN_CONNECTION_OK         = 0
    SERIAL_COMMUNICATION_COULD_NOT_OPEN_CONNECTION  = -1
    SERIAL_COMMUNICATION_DEVICE_DID_NOT_ANSWER      = -2
    SERIAL_COMMUNICATION_COULD_NOT_SEND_DATA        = -3
    
    def __init__ (self, port, baudrate = SERIAL_COMMUNICATION_DEFAULT_SERIAL_BAUD_RATE, timeout = SERIAL_COMMUNICATION_DEFAULT_SERIAL_TIMEOUT):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        
    def getPort(self):
        return self.port
    
    def getBaudrate(self):
        return self.baudrate
    
    def getTimeout(self):
        return self.timeout
    
    def createConnection(self):
        
        serial_connection = None
        error_msg = ''
        
        print "Opening serial connection"
        print "Port: ",     self.port
        print "Baudrate: ", self.baudrate
        print "Timeout: ",  self.timeout
        
        try:
            serial_connection = serial.Serial(self.port,self.baudrate)
        
        except serial.SerialException, msg:
            
            #Print serial error
            error_msg = "Device was not found. Connection status: " + msg[1]
            print >> sys.stderr, error_msg
            serial_connection = None
                    
        finally:            
            return serial_connection, error_msg
    
    
    def sendSerialData(self, serial_connection, data):
        
        error_code = self.SERIAL_COMMUNICATION_OPEN_CONNECTION_OK
        error_msg = ''
        
        if serial_connection is None:
            error_msg = 'sendSerialData Error: Could not open serial connection'
            print error_msg
            error_code = self.SERIAL_COMMUNICATION_COULD_NOT_OPEN_CONNECTION
            return error_code, error_msg
        
        try:
            print 'Command to send: ',
            
            print '[ ',            
            for k in command:
                print hex(ord(k)),
        
            print ' ]'
            
            serial_connection.write(data.decode('hex'))
            
            
                    
        
    
    
    
    
    
    
    
    