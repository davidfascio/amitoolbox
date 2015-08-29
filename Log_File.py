import time

class Log_File:
    
    DEFAULT_LOG_FILE_NAME = 'logFile.log'
    
    def __init__(self, logFileName=DEFAULT_LOG_FILE_NAME):              
        self.logFileName = logFileName
        
    def getLogFileName(self):
        return self.logFileName
    
    def createLogFile(self):        
        log_file = open(self.getLogFileName(), 'w')        
        log_file.write('===================== Start Logging File on ' + self.getActualTime() + ' =====================\n\n')
        log_file.close()
    
    def writeLogFile(self, textToLogFile):        
        log_file = open(self.getLogFileName(), 'a')    
        log_file.write(self.getActualTime() + ' ' + textToLogFile + '\n')        
        log_file.close()    
    
    def getActualTime(self):
        return time.ctime()