import csv
import pefile

pe = pefile.PE("C:/Users/Zoloo/Desktop/araiboldogfail/virus1", fast_load=True)
pe1 = pefile.PE("C:/WINDOWS/system32/Notepad.exe", fast_load=True)

pe.parse_data_directories()
pe1.parse_data_directories()

temp = []
temp1 = []
counter = 0

for entry in pe.DIRECTORY_ENTRY_IMPORT:
    for imp in entry.imports:
        for entry1 in pe.DIRECTORY_ENTRY_IMPORT:
            for imp1 in entry1.imports:
                if imp.name == imp1.name :
                    counter = counter + 1
        if counter == 0 : 
            temp.append([imp.name])
            counter = 0
    
print("success")

with open("compare.csv",'w+', newline="") as f: 
    write = csv.writer(f) 
    write.writerows(temp) 

# for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
#     print(hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal)
