#include <idc.idc>
static main() { auto ea, func, ref;

// Get current ea
ea = ScreenEA();

// Loop from start to end in the current segment
for (func=SegStart(ea); 
        func != BADADDR && func < SegEnd(ea); 
        func=NextFunction(func)) 
{
    // If the current address is function process it
    if (GetFunctionFlags(func) != -1)
    {
        Message("Function %s at 0x%x\n", GetFunctionFlags(func), func);

        //

    }
}
}