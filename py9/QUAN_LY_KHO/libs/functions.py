import csv
from datetime
def read_file(_path):
    f=open(_path,'r',encoding='utf-8')
    content=[]
    for row in csv.reader(f):
        content.append(row)
    f.close()
    return content
def print_content(content):
    for row in content:
        print('{:20}{:20}{:15}{:15}{:20}{:20}{:15}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
def update_file(_path,content):
    f=open(_path,'w',encoding='utf-8',newline='')
    csv.writer(f).writerows(content)
    f.close()
def 
