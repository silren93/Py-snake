sentence=input('Nhập mộ câu để xử lý: ')
lst_word=sentence.split()
set_word=set(lst_word)
set_word_sort=sorted(set_word)
print('Các từ đã sắp xếp và loại bỏ trùng lặp: ',set_word_sort)
num_word=len(set_word_sort)
num_char=0
for word in set_word_sort:
    num_char+=len(word)
print('Số từ: ',num_word)
print('Số kí tự: ',num_char)