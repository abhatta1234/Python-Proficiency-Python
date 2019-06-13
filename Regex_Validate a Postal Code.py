
# Validate a Postal Code(P)
# P must be between 100000 and 999999
# The number must not contain more than one alternating repetitive digit pair.

import re
P = input()

regex_integer_in_range = r"^[1-9][0-9]{5}$"

regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)