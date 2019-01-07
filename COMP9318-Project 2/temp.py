import helper


class0 = helper.strategy().class0
class1 = helper.strategy().class1

feather_list = []
for i in class0:
    for m in i:
        feather_list.append(m)

for i in class1:
    for m in i:
        feather_list.append(m)

feather_list = list(set(feather_list))

with open('test_data.txt','r') as test_data:
    test_data = [line.strip().split(' ') for line in test_data]


test = []
for i in test_data:
    indexlist = [0 for i in range(len(feather_list))]
    for j in feather_list:
        if j in i:
            count = i.count(j)
            indexlist[feather_list.index(j)] += count
    test.append(indexlist)








listclass1 = []
dictclass1 = {}

for i in class1:
    for j in i:
        flag = 0
        for m in class0:
            if j in m:
                flag = 1
        if flag == 0:
            listclass1.append(j)

listclass1 = list(set(listclass1))

for i in listclass1:
    dictclass1[i] = 0
for i in dictclass1:
    for m in class1:
        for n in m:
            if i == n:
                dictclass1[i] += 1


print(sorted(dictclass1.items(), key = lambda d:d[1], reverse=True))


listclass0 = []
dictclass0 = {}

for i in class0:
    for j in i:
        flag = 0
        for m in class1:
            if j in m:
                flag = 1
        if flag == 0:
            listclass0.append(j)

listclass0 = list(set(listclass0))

for i in listclass0:
    dictclass0[i] = 0
for i in dictclass0:
    for m in class0:
        for n in m:
            if i == n:
                dictclass0[i] += 1


print(sorted(dictclass0.items(), key = lambda d:d[1], reverse=True))


lastdict0 = {}
for i in feather_list:
    lastdict0[i] = 0
for i in lastdict0:
    for j in class0:
        for m in j:
            if i == m:
                lastdict0[i] += 1

lastdict1 = {}
for i in feather_list:
    lastdict1[i] = 0
for i in lastdict1:
    for j in class1:
        for m in j:
            if i == m:
                lastdict1[i] += 1

print(lastdict0)
print(lastdict1)
print(len(lastdict1))


allclass = []
allclassdict = {}

for i in class0:
    for j in i:
        flag = 0
        for m in class1:
            if j in m:
                flag = 1

        if flag == 1:
            allclass.append(j)

for i in class1:
    for j in i:
        flag = 0
        for m in class0:
            if j in m:
                flag = 1
        if flag == 1:
            allclass.append(j)

allclass = list(set(allclass))
print(allclass)




temp = {}

for i in allclass:
    temp[i] = 0

for i in temp:
    for m in lastdict0:
        if i == m:
            data0 = lastdict0[i] /len(class0)
    for n in lastdict1:
        if i == n:
            data1 = lastdict1[i] /len(class1)


    temp[i] = 0.001 * data1/data0

print(temp)



for i in allclass:
    allclassdict[i] = 0

for i in allclassdict:
    for m in lastdict0:
        if i == m:
            data0 = lastdict0[i] /len(class0)
    for n in lastdict1:
        if i == n:
            data1 = lastdict1[i] /len(class1)


    allclassdict[i] = 0.001 * data1/data0

allclassdict = sorted(allclassdict.items(), key = lambda d:d[1], reverse=True)
print(allclassdict)


answer = []


for i in test_data:
    print(i)
    list = []
    list1 = []
    fudict = {}
    for j in i:
        fudict[j] = 0
    for j in fudict:
        if j in dictclass1:
            fudict[j] = 1
        elif j in dictclass0:
            fudict[j] = 0
        else:
            if j not in temp:
                fudict[j] = 0
            else:
                fudict[j] = temp[j]

    fudict1 = copy.deepcopy(fudict)
    fudict = sorted(fudict.items(), key=lambda d: d[1], reverse=True)

    print(fudict1)
    print(fudict)

    for m in range(10):
        list1.append(fudict[m][0])
    print(list1)
    for n in i:
        for p in list1:
            if n == p:
                i[i.index(n)] = 'kashmir'


print(test_data)

file = open('modified_data.txt', 'w')

for i in test_data:
    write = ''
    for j in range(len(i) - 1):
        write = write + i[j] + ' '

    write = write + i[len(i) - 1] + '\n'
    print(write)
    file.write(write)

file.close()








