import idc
import idaapi
import idautils
import ida_xref

ea = get_screen_ea()
funcea = get_first_seg()
ref = get_first_cref_to(funcea)

while ref != BADADDR:
    print ("  called from", get_func_name(ref))
    ref = get_next_cref_to(BADADDR, ref)
