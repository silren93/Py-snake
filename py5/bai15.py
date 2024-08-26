can='Canh','Tân','Nhâm','Quý','Giáp','Ất','Bính','Đinh','Mậu','Kỷ'
chi='Thân','Dậu','Tuất','Hợi','Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi'
while True:
    nam_duong_lich=int(input('Nhap nam duong lich de kiem tra: '))
    if nam_duong_lich>=0:
        break
nam_am_lich=can[nam_duong_lich%10]+' '+ chi[nam_duong_lich%12]
print(nam_duong_lich,'là năm ',nam_am_lich)