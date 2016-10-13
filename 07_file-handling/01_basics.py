f = open("~/test.txt", 'r+t')

f1 = open("test.txt")      # equivalent to 'r' or 'rt'
f2 = open("test.txt",'w')  # write in text mode
f3 = open("img.bmp",'r+b') # read and write in binary mode

f.close()
f1.close()
f2.close()
f3.close()


f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
f = open("test.txt",mode = 'r',encoding = 'utf-8')

