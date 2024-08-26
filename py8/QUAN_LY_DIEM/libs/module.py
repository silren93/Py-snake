import csv
from datetime import datetime
def read_file(_path):
    f=open(_path,'r',encoding='utf-8')
    content=[]
    for row in csv.reader(f):
        content.append(row)
    f.close()
    return content
def print_content(content):
    for row in content:
        print('{:15}{:30}{:15}{:30}{:10}{:15}'.format(row[0],row[1],row[2],row[3],row[4],row[5]))
def update_file(_path,content):
    f=open(_path,'w',encoding='utf-8',newline='')
    csv.writer(f).writerows(content)
    f.close()
def thong_ke_rot_mon(content):
    ten_mon=input('Nhap ten mon hoc: ')
    ket_qua=[]
    tieu_de=content.pop(0)
    ket_qua.append(tieu_de)
    for row in content:
        if ten_mon==row[3] and float(row[4])<5:
            ket_qua.append(row)
    return ket_qua
def tinh_diem_trung_binh(ma_mon,content):
    so_luong=0
    tong_diem=0
    for row in content:
        if ma_mon==row[2]:
            so_luong+=1
            tong_diem+=float(row[4])
    print('{:15}{:15}{:15}',format(ma_mon,str(so_luong),str(tong_diem/so_luong)))