s = "i am in banglore"
v = ('a', 'e', 'i', 'o,u')
d={}
for i in s:
    if i in v:
        s1 = s.count(i)
        d[i] = s1

print(d)
