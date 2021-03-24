a = 'led=on&motor=off&switch=off'
ii = []
jj = {}
ii = a.split("&")

for s in ii:
    a, b= (s.split("="))
    jj[a] = b

print(jj)