b=['t','a',2,'c',[0,10],'t','t']
a=['a',2,'b',[0,10,[4,'z']],'a','a']

b.append(67)
b.insert(1,'z')
a.extend(b)
print(b.count('t'))
print(b)
print(a)
print(a.count('a'))