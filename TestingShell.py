import sys
import time
import serial

#from TCP_Socket import TCP_Socket
from Log_File import Log_File
from SerialCommands import SerialCommands
#from TestingNetwork import TestingNetwork
#from MeterEnergyHighLevel import MeterEnergyHighLevel
#from TCP_Commands import TCP_Commands
#from FormatUtils import bin2hex
#from DetalleEstadoVariable import DetalleEstadoVariable
#from MeterMonitoringAlerts import MeterMonitoringAlerts
#from WorkingRangeAlerts import WorkingRangeAlerts

class TestingShell:
    
    TESTING_SHELL_TCP_HELP_INDEX = 0    
    TESTING_SHELL_TCP_HELP_TEXT = """     
    Shell AMI toolbox help:                   
    syntaxis
    COMMAND     : amiToolBox.py [-mode command]  [-port /dev/tty] [-b baudrate] [-command ppp] [-Logfile logfile]
    TEST        : amiToolBox.py [-mode test]    [-port /dev/tty] [-b baudrate] [-testcase ppp] [-Logfile logfile] 
    """
    TESTING_SHELL_SYNTAXIS_ERROR = 'Syntaxis ERROR'
    serial_conn = None
    port = None
    baud = None
    
    def shell(self):
                
        dict = self.parseCommandLine()
        
        if self.shellCommandProcess(dict) == 0:
            print self.TESTING_SHELL_SYNTAXIS_ERROR


    def shellCommandProcess(self, dict):
        
        error_code = 0
        timer_seconds_delay = 10
                        
        # Testing mode
                        
        # Connection
        self.port = dict.get('-port')
        self.baud = dict.get('-b')
        
        
        
        
        if dict.get('-mode') == 'command':
            
                    
            command = dict.get('-command')
                        
            if command:
                
                serialCommand = SerialCommands().buildSerialCommand(command)
                self.sendCommandSerial(serialCommand.decode('hex'), command)
                
                error_code = 1
                    
        elif dict.get('-mode') == 'testcase':
            
            while(True):
                command = '--turnon'
                serialCommand = SerialCommands().buildSerialCommand(command)
                self.sendCommandSerial(serialCommand.decode('hex'), command)
                
                            
                command = '--turnoff'
                
                serialCommand = SerialCommands().buildSerialCommand(command)
                self.sendCommandSerial(serialCommand.decode('hex'), command)
                #data = dict.get('-data')
                #mult= dict.get('-c',1)
                #if data :
                #    d = (str(data)*int(mult))
                #    print 'String to send :', d
                #    data = bin2hex(d)
                #    tcpCommand = TCP_Commands().buildTCPCommand(command, data)
                #else:
                #    tcpCommand = TCP_Commands().buildTCPCommand(command)
                    
                #tcp_socket.sendCommandSocket(tcpCommand, command)   
                
        else:
            self.help(self.TESTING_SHELL_TCP_HELP_INDEX)
            error_code = 1
            
        return error_code
        
        
        
    def parseCommandLine(self):
        dict = {} 
        args = sys.argv[1:]  
        while len(args) >= 2:
            dict[args[0]] = args[1]
            args = args[2:]
        return dict
    
    
    def help(self, index):
        if index == self.TESTING_SHELL_TCP_HELP_INDEX:
            print self.TESTING_SHELL_TCP_HELP_TEXT
        return
    
    
    def sendCommandSerial(self, command, commandName):        
        
        try:
            
            self.serial_conn = serial.Serial(self.port, self.baud)
        
        except:            
            #serial_conn.close()
            self.help(self.TESTING_SHELL_TCP_HELP_INDEX)
            error_code = 1
            return error_code
        
        print "Sending a Serial Command: ", commandName  
        
        print '[ ',
        for k in command:
            print hex(ord(k)),
        print ' ]'
                   
        self.serial_conn.write(command)
        time.sleep(3)     
        self.serial_conn.close()
        
        
        
        
        
        
      