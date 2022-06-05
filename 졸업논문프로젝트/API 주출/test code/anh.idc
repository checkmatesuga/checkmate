#include <idc.idc>
static main (void) {
  auto offset,count;
  count = 1;
  offset= MinEA();
  while(offset != BADADDR) {
    offset = FindText(offset+2,3,0,0,"call");
    Message(
    "%03d %08x %s %s %s\n",
    count++,
    offset,
    GetMnem(offset),
    GetOpnd(offset,0),
    Name(Dfirst(offset))
    );
  }
}