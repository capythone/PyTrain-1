# string = "hello"
#
# print(string.__hash__())
# print("123455".__hash__())
# num = 2344
# print(num.__hash__())
# num = 23.44
# print(num.__hash__())


dict = {}
dict['one'] = "This is one"
dict['two'] = "This is one"
dict['three'] = "This is one"
dict[2] = "This is two"
dict[4.5] = "This is two"
dict[1+4.5j] = "This is two"


#
# for k,v in dict.items():
#     print("Hash value of key ", k, " is ", k.__hash__())
#     print("Hash table index of key ", k, " is ", k.__hash__() & 64)


for k,v in dict: #.items():
    print("Hash value of key ", k, " is ", hash(k))
    print("Hash table index of key ", k, " is ", hash(k) & 31)
