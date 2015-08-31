from FormatUtils import *

class SerialCommands:   
    
    DEFAULT_SERIAL_COMMANDS = {'--sync'     : '504eb4701d85',
                               '--version'  : '40',
                               '--status'   : '90',
                               '--mensure'  : '1036333830323030303030303030303030',
                               '--turnon'   : '1236333830323030303030303030303030',
                               '--turnoff'  : '1136333830323030303030303030303030' }
    
    DEFAULT_SERIAL_STX = '55CC'
    DEFAULT_SERIAL_EOT = '33CC'
    DEFAULT_SERIAL_MAC = '790809010AB6DA24'
    
    def findSerialCommand(self, command):                
        return self.DEFAULT_SERIAL_COMMANDS.get(command, command)
    
    def makeSerialCommand(self, command, hexBuffer):
        
        #command = dec2hex(command,1,True)
        dataSize = len(self.DEFAULT_SERIAL_MAC + command + hexBuffer) /2 
        #dataSize = dec2hex(dataSize, 4, True)
    
        
        dataSerialBuffer = (self.DEFAULT_SERIAL_MAC  +  command + hexBuffer)
        buffer = dataSerialBuffer.decode('hex')
                
        crc_value = self.calculateSerialCRC(buffer, 0xFFFF)        
        crc_value = dec2hex(crc_value, 4, True)
        
        dataSize = dec2hex(dataSize, 4, True)
        
        dataSerialBuffer = (self.DEFAULT_SERIAL_STX + dataSize + dataSerialBuffer + crc_value + self.DEFAULT_SERIAL_EOT)
        
        print "\n\t*** Building Serial Command ***\n"
        print "STX: ", self.DEFAULT_SERIAL_STX
        print "Data size (hex): ", dataSize 
        print "MAC (hex)", little2digendian(self.DEFAULT_SERIAL_MAC)
        print "Command to Send (hex): ", command       
        print "Hex Buffer: ", hexBuffer        
        print "CRC (hex)" , crc_value
        print "EOF: ", self.DEFAULT_SERIAL_EOT
        print "\n"    
        
        print "Output DataSerialBuffer ", dataSerialBuffer
        
        print "\n\n"   
        
        return dataSerialBuffer
        
    def buildSerialCommand(self, command, command_parameters=''):        
        return self.makeSerialCommand(self.findSerialCommand(command), command_parameters)
    
    
    def calculateSerialCRC(self, data, data_base):
        
        for index in data :
            index = ord(index) & 0x00FF
            data_base ^= index
            
            for k in range(0,8):
                flag = data_base & 1
                data_base >>= 1
                
                if(flag):
                    data_base ^= 0xA001
        
        return data_base