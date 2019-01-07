duiyou = {'"', "'s", '-', '.', '(', 'a', 'and', 'any', 'at', 'after', 'an', 'al', 'be', 'by', 'before',
          'country', 'call', 'come', 'during', 'day', 'david', 'discuss', 'for', 'first', 'from', 'general', 'million',
          'minister', 'make',
          'have', 'house', 'he', 'hold', 'his', 'in', 'its', 'of', 'on', 'power',
          'say', 'some', 'state', 'least', 'last', 'year', 'that', 'the', 'thursday', 'troop', 'this', 'to', 'their',
          'with', 'would', 'who', 'u.s.', 'up', 'urib', 'not', 'new', 'next', 'since', '0', '-docstart-'}

a=[('should', 5), ('1980', 5), ('league', 5), ('praise', 5), ('paul', 5), ('act', 5), ('endorse', 5), ('iraqis', 5), ('christian', 5), ('delay', 5), ('parliamentary', 5), ('truce', 5), ('opponent', 5), ('finally', 5), ('summer', 5), ('return', 5), ('remove', 5), ('figure', 5), ('yushchenko', 5),('leadership', 5), ('expel', 5), ('alliance', 5), ('credit', 5), ('research', 5), ('easily', 5), ('pass', 5), ('speak', 5), ('old', 5), ('mainland', 5), ('interim', 5), ('reuters', 5), ('pursue', 5), ('crisis', 5), ('market', 5), ('attend', 5), ('special', 5), ('put', 5), ('well', 5), ('path', 5), ('strain', 5), ('trial', 5), ('refuse', 5), ('donald', 5), ('name', 5), ('letter', 5), ('candidate', 5), ('taliban', 5), ('contract', 5), ('block', 5), ('positive', 5), ('behind', 5), ('accept', 5), ('information', 5), ('rumsfeld', 5), ('200', 5), ('body', 5), ('cast', 5), ('hollywood', 5), ('300', 5), ('abu', 5), ('lebanon', 5), ('press', 5), ('open', 5), ('give', 5), ('terrorist', 5), ('widely', 5), ('maoist', 5), ('church', 5), ('controversial', 5), ('benefit', 5), ('far', 5), ('islam', 5), ('director', 5), ('kilometer', 5), ('ballot', 5), ('hospital', 5), ('newly', 5), ('involve', 5), ('cite', 5), ('respond', 5), ('corp', 5), ('comment', 5), ('dutch', 5), ('seize', 5), ('june', 5), ('hungary', 5), ('negotiator', 5), ('stock', 5), ('croat', 5), ('allegedly', 5), ('pull', 5), ('music', 5), ('jewish', 5), ('bali', 5), ('announce', 5), ('powerful', 5)]


b=[('alliance', 5), ('terrorist', 5), ('act', 5), ('rumsfeld', 5), ('mainland', 5), ('abu', 5), ('old', 5), ('special', 5), ('finally', 5), ('press', 5), ('hospital', 5), ('open', 5), ('hollywood', 5), ('trial', 5), ('jewish', 5), ('paul', 5), ('crisis', 5), ('put', 5), ('letter', 5), ('benefit', 5), ('delay', 5), ('remove', 5), ('lebanon', 5), ('positive', 5), ('maoist', 5), ('pursue', 5), ('block', 5), ('donald', 5), ('give', 5), ('reuters', 5), ('june', 5), ('market', 5), ('respond', 5), ('information', 5), ('bali', 5), ('expel', 5), ('involve', 5), ('truce', 5), ('dutch', 5), ('corp', 5), ('taliban', 5), ('kilometer', 5), ('strain', 5), ('leadership', 5), ('announce', 5), ('yushchenko', 5), ('seize', 5), ('endorse', 5), ('newly', 5), ('cite', 5), ('200', 5), ('parliamentary', 5), ('refuse', 5), ('music', 5), ('iraqis', 5), ('well', 5), ('cast', 5), ('path', 5), ('croat', 5), ('speak', 5), ('church', 5), ('praise', 5), ('islam', 5), ('director', 5), ('negotiator', 5), ('credit', 5), ('figure', 5), ('attend', 5), ('easily', 5), ('contract', 5), ('interim', 5), ('1980', 5), ('allegedly', 5), ('300', 5), ('controversial', 5), ('candidate', 5), ('christian', 5), ('comment', 5), ('opponent', 5), ('stock', 5), ('ballot', 5), ('should', 5), ('accept', 5), ('return', 5), ('pull', 5), ('far', 5), ('widely', 5), ('body', 5), ('behind', 5), ('summer', 5), ('pass', 5), ('research', 5), ('hungary', 5), ('powerful', 5), ('league', 5), ('name', 5)]

a_s=[]
for i in range(len(a)):
    a_s.append(a[i][0])
# print(a_s)

b_s=[]
for i in b:
    b_s.append(i[0])

print(sorted(a_s))
print(sorted(b_s))