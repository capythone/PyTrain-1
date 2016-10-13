# try:
#    f = open("tests.txt",encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()

# Alternate way is
with open("test.txt",encoding = 'utf-8') as f:
   print(f.read(100))