from ProtocolCommands import ProtocolCommandsEnum

class FunctionalCommandsTest():
    
    FUNCTIONAL_COMMANDS_SEQUENCE_TURN_ON_RELAY_PROCESS = ((ProtocolCommandsEnum.PROTOCOL_COMMANDS_READMODE_STATUS_LOCAL, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_IDLE_STATE),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_CON_MTR_REM, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_CON_MTR_REM),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_READMODE_STATUS_LOCAL, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_SUCCESS_CMD),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_READ_MTR_REM, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_READ_MTR_REM),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_READMODE_STATUS_LOCAL, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_FRAGDATA_ARRIVED),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_BUFFERMODE_READ_TEMPORAL_BUFFER, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_BUFFERMODE_READ_TEMPORAL_BUFFER)) 
    
    FUNCTIONAL_COMMANDS_SEQUENCE_TURN_OFF_RELAY_PROCESS = ((ProtocolCommandsEnum.PROTOCOL_COMMANDS_READMODE_STATUS_LOCAL, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_IDLE_STATE),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_DIS_MTR_REM, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_DIS_MTR_REM),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_READMODE_STATUS_LOCAL, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_SUCCESS_CMD),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_READ_MTR_REM, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_READ_MTR_REM),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_READMODE_STATUS_LOCAL, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_READMODE_STATUS_LOCAL_FRAGDATA_ARRIVED),
                                                          (ProtocolCommandsEnum.PROTOCOL_COMMANDS_BUFFERMODE_READ_TEMPORAL_BUFFER, 
                                                           ProtocolCommandsEnum.PROTOCOL_COMMANDS_REPLY_BUFFERMODE_READ_TEMPORAL_BUFFER))