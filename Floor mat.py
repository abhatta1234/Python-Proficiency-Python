

# Design a Floor Mat
# Mat size : N X M, where N is a natural odd number and M is 3 times N
# Should Have "WELCOME" written in the center
# Design pattern should only use "|",".", and "-" characters.


inp = list(map(int,input().split()))
nr = inp[0]//2
nc = inp[1]
for i in range(0,nr):
    string = ".|."*(2*i+1)
    print(string.center(nc,"-"))
print("Welcome".center(nc,"-"))
for i in range(nr,0,-1):
    string = ".|."*(2*i-1)
    print(string.center(nc,"-"))