from idautils import * 
from idaapi import * 
from idc import * 
ea =BeginEA() 
for funcAddr in Functions( SegStart(ea) , SegEnd( ea ) ) : 
    funcName = GetFunctionName(funcAddr) 
    if funcName.find("main") > 0 or funcName.find("Main") > 0 or funcName.find("Start") > 0 or funcName.find("start") : 
        print "Function %s is at 0x%x" % ( funcName, funcAddr )