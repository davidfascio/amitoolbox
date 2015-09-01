import serial
import sys
from SerialCommands import SerialCommands
import time
from ProtocolCommands import *


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
            return serial_connection
    
    
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
            for k in data.decode('hex'):
                print hex(ord(k)),
        
            print ' ]'
            
            serial_connection.write(data.decode('hex'))
        
        except serial.SerialException, msg:
            
            error_msg = "Send command to device error. Connection status: " + msg[1]
            print >> sys.stderr, error_msg
            error_code = self.SERIAL_COMMUNICATION_COULD_NOT_SEND_DATA
            serial_connection.close()
        
        finally:
            return error_code, error_msg
            
            
    
    def receiveSerialData(self, serial_connection):
        
        error_code = self.SERIAL_COMMUNICATION_OPEN_CONNECTION_OK
        error_msg = ''
        data = ''
                        
        if serial_connection is None:
            error_msg = 'sendSerialData Error: Could not open serial connection'
            print error_msg
            error_code = self.SERIAL_COMMUNICATION_COULD_NOT_OPEN_CONNECTION
            return error_code, error_msg
        
        
        
        try:
            while True:            
                data += serial_connection.read(serial_connection.inWaiting())
                
                if SerialCommands.DEFAULT_SERIAL_EOT.decode('hex') in data:
                    break 
            
            #print "Data Received: ", data
            
            if not data:
                error_msg = "Device didnt answer. Connection status: Device connection is down"
                print >> sys.stderr, error_msg
                error_code = self.SERIAL_COMMUNICATION_DEVICE_DID_NOT_ANSWER                
            else:
                print 'Data reading: ',
                print '[ ',            
                
                for k in data:
                    print hex(ord(k)),
        
                print ' ]'
                
                
        except Exception, msg:
            
            error_msg = "Device didnt answer. Connection status: " + str(msg)
            print >> sys.stderr, error_msg
            error_code = self.SERIAL_COMMUNICATION_DEVICE_DID_NOT_ANSWER        
        
        
        
            
        finally:        
            #serial_connection.close()
            return data
    
    def sendSerialDataWaitAnswer(self, serial_connection, data_to_send, data_expected, retries):
        
        retry = 0
        answered = False
        
        while (True):
            self.sendSerialData(serial_connection, data_to_send)
            data_received = self.receiveSerialData(serial_connection)   
            retry += 1        
            
            #print "Data received: ", data_received
            #print "Data expected: ", data_expected.decode('hex')
            
            #if (data_expected == ProtocolCommandsEnum.PROTOCOL_COMMANDS_NONE_CUSTOM_REPLY.get_command()):
            #    answered = True
            #    break
            time.sleep(1)
            
            if (data_expected.decode('hex') == data_received):
                answered = True
                break
                
                
            if(retries <= retry):
                break
            
            
                       
        
        return answered
                
            
                                                              
        
    
    
    
    
    