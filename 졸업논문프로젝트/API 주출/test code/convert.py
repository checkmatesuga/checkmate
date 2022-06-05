from idautils import * 
from idaapi import * 
from idc import * 
ea =BeginEA() 
for funcAddr in Functions( SegStart(ea) , SegEnd( ea ) ) :
    funcName = GetFunctionName(funcAddr)
    if get_func_flags(funcAddr) != -1 :
        funcName = find_text(funcAddr+2,3,0,0,"call")
        print "%s" % (get_func_name(funcName))