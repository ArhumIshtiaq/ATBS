import sys
n = sys.argv[1]
l = len(n)
for i in range(l):
    print("*"*int(i)+n[i]+"*"*int(l-1-i))