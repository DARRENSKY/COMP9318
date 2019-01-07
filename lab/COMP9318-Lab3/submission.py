## import modules here

################# Question 1 #################
def tokenize(sms):
    return sms.split(' ')

def get_freq_of_tokens(sms):
    tokens={}
    for token in tokenize(sms):
        if token not in tokens:
            tokens[token]=1
        else:
            tokens[token]+=1
    return tokens

def multinomial_nb(training_data, sms):

    class_ham = 0
    class_spam = 0
    for i in training_data:
        if i[1] == "ham":
            class_ham += 1
        if i[1] == "spam":
            class_spam += 1
    class_all = class_ham + class_spam
    dic_ham = {}
    dic_spam = {}
    dic_all = {}
    for i in training_data:
        if i[1] == "ham":
            for j in i[0]:
                dic_ham[j] = 0
                dic_all[j] = 0
        if i[1] == "spam":
            for j in i[0]:
                dic_spam[j] = 0
                dic_all[j] = 0
    for i in training_data:
        if i[1] == "ham":
            for j in i[0]:
                dic_ham[j] += i[0][j]
        if i[1] == "spam":
            for j in i[0]:
                dic_spam[j] += i[0][j]

    num_ham = 0
    num_spam = 0
    for i in dic_ham:
        num_ham += dic_ham[i]
    for i in dic_spam:
        num_spam += dic_spam[i]
    vocabulary = len(dic_all)
    p_ham = class_ham / class_all
    p_spam = class_spam / class_all
    word={}
    for i in sms:
        word[i]=0
    for i in sms:
        word[i]+=1
    # print(word)
    result_ham = 1
    result_spam = 1
    k=0
    for i in word:
        if i in dic_all:
            if i in dic_ham:
                result_ham *= ((dic_ham[i] + 1) / (num_ham + vocabulary)) ** word[i]
            else:
                result_ham *= (1 / (num_ham + vocabulary)) ** word[i]
            if i in dic_spam:
                result_spam *= ((dic_spam[i] + 1) / (num_spam + vocabulary)) ** word[i]
            else:
                result_spam *=(1 / (num_spam + vocabulary)) ** word[i]
            k+=1
    if k==0:
        return p_spam/p_ham
    result_ham = result_ham * p_ham
    result_spam = result_spam * p_spam
    result = result_spam / result_ham
    return result


