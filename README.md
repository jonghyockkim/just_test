import sys
#min = 100
#max = 150
#sys.argv = ["first_10.csv", 100, 150]
file_name = sys.argv[0]
min = sys.argv[1]
max = sys.argv[2]
file_name = 'first_10.csv'
f = open(file_name)
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(',')
    price = int(columns[9])
    if price >= int(min) and price <= int(max):
        print(line)