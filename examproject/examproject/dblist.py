import csv


f = open('c:/Users/kyuripark/likelion/class_list.csv')
rr = csv.reader(f)
for line in rr:
    print(line)

f.close()