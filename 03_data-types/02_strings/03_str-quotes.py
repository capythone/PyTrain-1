#!/usr/bin/python3

"""this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

dobuleQuotes = "This is venu" \
               "How r you folks"

print (para_str)
print (dobuleQuotes)

#Raw strings
print ('C:\\nowhere')
print ('C:\Sowhere')

print (r'C:\\nowhere\t\n')