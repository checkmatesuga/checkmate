#define UNLOADED_FILE
#include <idc.idc>
static main (void) {
  auto fpt, ydargaa;
  fpt=fopen("laitai.csv", "w");
  auto ea,func,ref;
  ea = ScreenEA();
  for(func=SegStart(ea); func != BADADDR && func < SegEnd(ea); func=NextFunction(func)) 
{
    if(GetFunctionFlags(func) != -1)
    {
        ydargaa= GetFunctionName(func);
        fprintf(fpt,"%s",ydargaa);
        Message("%s\n", GetFunctionName(func));
}
}
fclose(fpt);
}