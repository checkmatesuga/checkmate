from idaapi import *
	danger_funcs = ["strcpy","sprintf","strncpy"]
	for func in danger_funcs:
		addr = LocByName( func )
 		if addr != BADADDR:
 # Grab the cross-references to this addressIDAPython—Scripting IDA Pro 159
		cross_refs = CodeRefsTo( addr, 0 )
 		print "Cross References to %s" % func
 		print "-------------------------------"
 		for ref in cross_refs:
 			print "%08x" % ref
 			# Color the call RED
 			SetColor( ref, CIC_ITEM, 0x0000ff)
