import csv
import pefile

pe = pefile.PE("C:/WINDOWS/system32/Notepad.exe", fast_load=True)

pe.parse_data_directories()
 
temp = []

for entry in pe.DIRECTORY_ENTRY_IMPORT:
    for imp in entry.imports:
        temp.append([entry.dll,hex(imp.address),imp.name])

print("success")

with open("note.csv",'w+', newline="") as f: 
    write = csv.writer(f) 
    write.writerows(temp) 
