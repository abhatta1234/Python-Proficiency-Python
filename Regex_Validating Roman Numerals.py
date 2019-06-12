
# Given a string S, Validate if it is Roman Numeral between 1-3999.


import re
string = input()


collection = re.search(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',string)

if collection:
    print(True)

else:
    print(False)






