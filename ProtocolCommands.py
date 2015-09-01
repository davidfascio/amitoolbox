from FormatUtils import *
from enum import Enum

# Default Values
WRITE_MODE_UPDATE_TIME_DATE_DEFAULT_VALUE   = '4eb4701d85' # Default Time
NO_COMMAND_ID                               = ''
NO_COMMAND_STATUS                           = '' 
NO_PARAMETERS                               = ''
DEFAULT_FIRMWARE_VERSION                    = 'a814'  # 5.5.8
DEFAULT_NUMBER_METER                        = '36333830323030303030303030303030'
DEFAULT_SERIAL_STX                          = '55CC'
DEFAULT_SERIAL_EOT                          = '33CC'
DEFAULT_SERIAL_MAC                          = '790809010AB6DA24'

DEFAULT_CRC_BASE                            = 0xFFFF

# Local Read Command Types
SYNC_REQUEST                                = '28'
READMODE_VERSION_COOR_LOCAL                 = '40'
READMODE_STATUS_LOCAL                       = '90'
BUFFERMODE_READ_TEMPORAL_BUFFER             = '33'
# Local Write command Types
WRITE_MODE_UPDATE_TIME_DATE                 = '50'

# Status Command Types
SUCCESS_CMD                                 = '01'
FRAGDATA_ARRIVED                            = '03'
B_IDLE_STATE                                = '05'
COOR_BUSY                                   = '08'
MALFORMED_FRAME                             =' 82'
CAB_NO_RESPOND                              = '84'
CAB_WITHOUT_METERS                          = '8C'


#Remote MTR Command Type
READ_MTR_REM                                = '10'
DIS_MTR_REM                                 = '11'
CON_MTR_REM                                 = '12'


# Enummeration Class
class ProtocolCommandsEnum(Enum):   
    
    ############################################################################################################
    #
    #     COMMAND ENUMERATION LIST
    #
    
    # Sync Process Commands
    PROTOCOL_COMMANDS_REPLY_MODE_SYNC_REQUEST                   = (SYNC_REQUEST, SUCCESS_CMD, NO_PARAMETERS, '--reply_sync')
    
    # Time Update Process Commands
    PROTOCOL_COMMANDS_WRITE_MODE_UPDATE_TIME_DATE               = (WRITE_MODE_UPDATE_TIME_DATE, NO_COMMAND_STATUS, WRITE_MODE_UPDATE_TIME_DATE_DEFAULT_VALUE, '--update_time')
    PROTOCOL_COMMANDS_REPLY_MODE_UPDATE_TIME_DATE_SUCCESS_CMD   = (WRITE_MODE_UPDATE_TIME_DATE, SUCCESS_CMD )
     
    # Version Process Commands
    PROTOCOL_COMMANDS_READ_MODE_VERSION_COOR_LOCAL              = (READMODE_VERSION_COOR_LOCAL, NO_COMMAND_STATUS, NO_PARAMETERS, '--read_version' )
    PROTOCOL_COMMANDS_REPLY_MODE_VERSION_COOR_LOCAL_SUCCESS_CMD = (READMODE_VERSION_COOR_LOCAL, SUCCESS_CMD, DEFAULT_FIRMWARE_VERSION)
     
    # Turn on meter relay
    PROTOCOL_COMMANDS_CON_MTR_REM                               = (CON_MTR_REM, NO_COMMAND_STATUS, DEFAULT_NUMBER_METER, '--connect_mtr')
    PROTOCOL_COMMANDS_REPLY_CON_MTR_REM                         = (CON_MTR_REM, SUCCESS_CMD, SUCCESS_CMD)
    
    #Turn off meter relay
    PROTOCOL_COMMANDS_DIS_MTR_REM                               = (DIS_MTR_REM, NO_COMMAND_STATUS, DEFAULT_NUMBER_METER, '--disconnect_mtr')
    PROTOCOL_COMMANDS_REPLY_DIS_MTR_REM                         = (DIS_MTR_REM, SUCCESS_CMD)     
    
    # Read meter
    PROTOCOL_COMMANDS_READ_MTR_REM                              = (READ_MTR_REM, NO_COMMAND_STATUS, DEFAULT_NUMBER_METER, '--read_mtr')
    PROTOCOL_COMMANDS_REPLY_READ_MTR_REM                        = (READ_MTR_REM, SUCCESS_CMD, SUCCESS_CMD)
     
    # Request Status
    PROTOCOL_COMMANDS_READMODE_STATUS_LOCAL                             = (READMODE_STATUS_LOCAL, NO_COMMAND_STATUS, NO_PARAMETERS, '--read_status')
    PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_SUCCESS_CMD           = (READMODE_STATUS_LOCAL, SUCCESS_CMD)
    PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_IDLE_STATE            = (READMODE_STATUS_LOCAL, B_IDLE_STATE)
    PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_CAB_NO_RESPOND        = (READMODE_STATUS_LOCAL, CAB_NO_RESPOND )
    PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_CAB_WITHOUT_METERS    = (READMODE_STATUS_LOCAL, CAB_WITHOUT_METERS)
    PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_COOR_BUSY             = (READMODE_STATUS_LOCAL, COOR_BUSY)
    PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_MALFORMED_FRAME       = (READMODE_STATUS_LOCAL, MALFORMED_FRAME)
    PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_FRAGDATA_ARRIVED      = (READMODE_STATUS_LOCAL, FRAGDATA_ARRIVED)
       
    # Read local buffer
    PROTOCOL_COMMANDS_BUFFERMODE_READ_TEMPORAL_BUFFER                   = (BUFFERMODE_READ_TEMPORAL_BUFFER, NO_COMMAND_STATUS, NO_PARAMETERS, '--read_tmp_buffer' )
    PROTOCOL_COMMANDS_REPLY_BUFFERMODE_READ_TEMPORAL_BUFFER             = (BUFFERMODE_READ_TEMPORAL_BUFFER, SUCCESS_CMD )
    
    # None custom reply
    
    PROTOCOL_COMMANDS_NONE_CUSTOM_REPLY                                 = (NO_COMMAND_ID)
        
    # Attributes
    #command_size = ''
    #command_mac_address = ''
    #command_id = ''
    #command_status = ''
    #command_parameters = ''
    #command_name = ''
    #command_crc = ''
    #command_buffer = ''
    
          
    def __init__(self, command_id, command_status = '', command_parameters = '', command_name = '', command_mac_address = DEFAULT_SERIAL_MAC):
        
        self.command_size = ''
        self.command_mac_address = command_mac_address
        self.command_id = command_id
        self.command_status = command_status
        self.command_parameters = command_parameters
        self.command_name = command_name
        self.command_crc = ''
        self.command_buffer = ''
        
    def get_command_name(self):
        return self.command_name
        
    def get_command(self):
        
        data_buffer_str = (self.command_mac_address + self.command_id + self.command_status + self.command_parameters)
        self.command_size = dec2hex(len(data_buffer_str) / 2, 4, True)
        
        data_buffer_hex = data_buffer_str.decode('hex')
        self.command_crc = dec2hex (self.calculate_crc(data_buffer_hex, DEFAULT_CRC_BASE), 4, True)
        
        self.command_buffer = (DEFAULT_SERIAL_STX + self.command_size + data_buffer_str + self.command_crc + DEFAULT_SERIAL_EOT)
        
        self.print_command()
        
        return self.command_buffer
    
    def print_command(self):
        
        print "\n[BUILDING_PROTOCOL_COMMAND]:"
        print "Command Name: ", self.command_name
        print "STX: ", DEFAULT_SERIAL_STX
        print "Data size (hex): ", self.command_size 
        print "MAC (hex)", little2digendian(DEFAULT_SERIAL_MAC)
        print "Command to Send (hex): ", self.command_id       
        print "Command Status (hex): ",   self.command_status
        print "Command Parameters (hex): " , self.command_parameters
        print "CRC (hex)" , self.command_crc
        print "EOF: ", DEFAULT_SERIAL_EOT       
        print "Output Buffer ", self.command_buffer        
        #print "\n"     
    
    
    def calculate_crc(self, data, data_base):
        
        for index in data :
            index = ord(index) & 0x00FF
            data_base ^= index
            
            for k in range(0,8):
                flag = data_base & 1
                data_base >>= 1
                
                if(flag):
                    data_base ^= 0xA001
        
        return data_base