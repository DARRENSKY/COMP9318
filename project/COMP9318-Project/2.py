with open('class-0.txt', 'r') as class0:
    class_0 = [line.strip().split(' ') for line in class0]

with open('class-1.txt', 'r') as class0:
    class_1 = [line.strip().split(' ') for line in class0]

dic0={}
length_class0=len(class_0)

for i in class_0:
    for j in i:
        dic0[j]=0
for i in class_0:
    for j in i:
        dic0[j]+=1


print (sorted(dic0.items(), key=lambda d: d[1],reverse=True))

dic1={}
length_class1=len(class_1)

for i in class_1:
    for j in i:
        dic1[j]=0
for i in class_1:
    for j in i:
        dic1[j]+=1

rate=length_class0/length_class1
for i in dic1:
    dic1[i]*=rate
print (sorted(dic1.items(), key=lambda d: d[1],reverse=True))

dic2={}
tokens={'the','.','"','.','-','in','of','be','a','to','of','and','say','have',"'s",'for','on','that','at',",","from","he","with","for","by","it","its","this"}
for i in tokens:
    if i in dic0:
        dic0.pop(i)

for i in tokens:
    if i in dic1:
        dic1.pop(i)
diconly0={}
diconly1={}
for i in dic0:
    if i not in dic1:
        diconly0[i]=dic0[i]
for i in dic1:
    if i not in dic0:
        diconly1[i]=dic1[i]
# print (sorted(diconly0.items(), key=lambda d: d[1],reverse=True))
# print (sorted(diconly1.items(), key=lambda d: d[1],reverse=True))
for i in dic0:
    for j in dic1:
        if i==j:
            dic2[i]=dic0[i]-dic1[i]
print (sorted(dic0.items(), key=lambda d: d[1],reverse=True))
print (sorted(dic1.items(), key=lambda d: d[1],reverse=True))
print (sorted(dic2.items(), key=lambda d: d[1],reverse=True))

('iraq', 45.0)
('city', 34.0)
('nuclear', 28.0)
('force', 24.0)
('bomb', 21.0)
('oil', 20.0)
('government', 19.0)
('fail', 19.0)
('international', 18.0)
('region', 18.0)
('attack', 18.0)
('official', 18.0)
('war', 18.0)

####
('president', -126.0)
('mr.', -111.0)
('bush', -29.0)
('minister', -24.0)
('russian', -23.0)
('spokesman', -21.0)
('beat', -20.0)
('afghan', -14.0)
('military', -16.0)
('secretary', -16.0)