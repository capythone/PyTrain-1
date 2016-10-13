# num = input('Enter a number: ')
# print(num)


def testfun(test1,
            test2,
            test3):
    print("test smaple function with params", test1,test2,test3)
    return test2+test3, "multi return"


summation, msg = testfun("hello", 100, 3.147)
# print(summation,msg)

def foo():
    print("hello from inside of foo")
    print(summation, msg)
    # summation = 100
    return 1

print(summation,msg)


if __name__ == '__main__':
    print("going to call foo")
    x = foo()
    print("called foo")
    print("foo returned " + str(x))