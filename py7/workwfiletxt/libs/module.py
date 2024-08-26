def read_file(_path):
    f=open(_path,'r',encoding='utf-8')
    content=f.read()
    f.close()
    return content
