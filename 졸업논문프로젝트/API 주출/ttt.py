import csv
import pefile

pe = pefile.PE("C:/Windows/System32/kernel32.dll", fast_load=True)
pe1 = pefile.PE("C:/Windows/System32/user32.dll", fast_load=True)

pe.parse_data_directories()
pe1.parse_data_directories()

temp = []

for entry in pe.DIRECTORY_ENTRY_IMPORT:
    # print(entry.dll)    
    for imp in entry.imports:
        temp.append([imp.name])
        # print('\t', hex(imp.address), imp.name)
    
for entry in pe1.DIRECTORY_ENTRY_IMPORT:
    # print(entry.dll)    
    for imp in entry.imports:
        temp.append([imp.name])
        # print('\t', hex(imp.address), imp.name)
    
print("success")

with open("white.csv",'w+', newline="") as f: 
    write = csv.writer(f) 
    write.writerows(temp) 

# for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
#     print(hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal)
