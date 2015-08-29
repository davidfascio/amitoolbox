from struct import unpack , pack
import sys

def setFloat(dato):
    bufferf = pack('f', float(dato))[::-1]
    return bufferf

def setByte(dato):
    bufferB = pack('B', int(dato))
    return bufferB

def setUint_32(dato):
    bufferf = pack('L', (dato))[::-1]
    return bufferf

def setUint(dato):
    bufferI = pack('I', (dato))[::-1]
    return bufferI

def getUint_32 (dato):        
    buffer32 = dato[0:4]
    dato = dato[4::]
    return unpack('L', buffer32[::-1])[0] , dato

def getUint(dato):    
    bufferui = dato[0:4]
    dato = dato[4::]
    return unpack('I', bufferui[::-1])[0] , dato

def getInt(dato):    
    bufferi = dato[0:4]
    dato = dato[4::]
    return unpack('I', bufferi[::-1])[0] , dato    

def getFLoat(dato):    
    bufferF = dato[0:4] 
    dato = dato[4::]
    return unpack('f', bufferF[::-1])[0] , dato        

def bin2hex(dato):
    bufferhex = ''
    for k in dato:       
        bufferhex = bufferhex + dec2hex(ord(k), 2)
    
    return bufferhex

def debugPause():
    try:
        input("Press any key to finish")
    finally:   
        sys.exit()
    
def dec2hex(decCommand, format, big_endian_enable = False):    
    temp = hex(decCommand).split('x')[1]    
    for k in range(0, format - len(temp)): 
        temp = '0' + temp
    
    if big_endian_enable:
        temp = little2digendian(temp)    
              
    return temp     

def dec2bin(decimal, format):
    temp = bin(decimal)[2:]
    
    for k in range(0, format - len(temp)): 
        temp = '0' + temp
                 
    return temp 

def little2digendian(temp):
    return "".join(reversed([temp[i:i+2] for i in range(0, len(temp), 2)]))