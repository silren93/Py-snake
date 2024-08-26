import calendar
tup_day='Hai','Ba','Tư','Năm','Sáu','Bảy','Chủ nhật' 
str_date=input('Nhập vào ngày cần kiểm tra theo dd/mm/yyyy: ')
lst_date=str_date.split('/')
d,m,y=int(lst_date[0]),int(lst_date[1]),int(lst_date[2])
_index=calendar.weekday(y,m,d)
_day=tup_day[_index]
print(str_date,'là ngày thứ: ',_day)
