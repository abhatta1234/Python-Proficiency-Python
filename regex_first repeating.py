
# Use regex to print the first repeating alphanumeric character in the given string
# Print -1 if there is no repeating characters

import re

inp = input()

result = re.search(r'([a-zA-Z0-9])\1+',inp)

if result:
    print(result.group(1))
else:
    print(-1)