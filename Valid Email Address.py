
# Given integer N followed by N email address
# Task: Print only valid email address in lexicographic order
# The username can only contain letters,digits,dashes and underscores
# The website can only have letters and digits
# The maximum length of the extension is 3


num = int(input())
collection = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-')
a = []
for i in range(num):
    em = input()
    try:
        user,other = em.split("@")
        serv,ext = other.split(".")
        if set(user).issubset(collection) and len(user) != 0:
            if serv.isalnum():
                if len(ext) <= 3:
                    a.append(em)
    except ValueError:
        a = a

print(sorted(a))

