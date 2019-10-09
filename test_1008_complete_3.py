import sys
file_name = 'complete.csv'
f = open(file_name, encoding="utf-8") 
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(',')
    try:  
        price = int(columns[9])
    except:
        print("Parsing ERROR: ",line)
        sys.exit(1)  # this stops the program
    if price >= 100 and price <= 150:
        print(line)