import helper
import numpy as np
def fool_classifier(): ## Please do not change the function defination...
    ## Read the test data file, i.e., 'test_data.txt' from Present Working Directory...
    with open('test_data.txt', 'r') as test_data:
        test_data = [line.strip().split(' ') for line in test_data]

    ## You are supposed to use pre-defined class: 'strategy()' in the file `helper.py` for model training (if any),
    #  and modifications limit checking
    strategy_instance=helper.strategy() 
    parameters={}

    parameters['kernel'] = 'poly'
    parameters['gamma'] = 'auto'
    parameters['C'] = 1
    parameters['degree'] = 100
    parameters['coef0'] = 0

    ###class0 360 lists(line)
    class0_content = helper.strategy().class0
    ###class1 180 lists(line)
    class1_content = helper.strategy().class1

    class0_length = len(class0_content)
    class1_length = len(class1_content)

    word=[]

    ##add class 0 all word
    for i in class0_content:
        for j in i:
            word.append(j)
    ##add class 1 all word
    for i in class1_content:
        for j in i:
            word.append(j)

    ##the number of unique word(class0+class1)
    word_unique = list(set(word))

    train_xdata = []
    train_ydata = []
    for line0 in class0_content:
        ###generate length=5718 value=0 list
        temp_list=[]
        for i in range(len(word_unique)):
            temp_list.append(0)
        ##genenrate one line including num of words according to index
        for wd in word_unique:
            if wd in line0:
                ##the number of word in line
                num_wd=line0.count(wd)
                ##find the index of the word
                wd_index=word_unique.index(wd)
                temp_list[wd_index] = num_wd
        train_xdata.append(temp_list)

    for line1 in class1_content:
        ###generate length=5718 value=0 list
        temp_list=[]
        for i in range(len(word_unique)):
            temp_list.append(0)
        ##genenrate one line including num of words according to index
        for wd in word_unique:
            if wd in line1:
                ##the number of word in line
                num_wd=line1.count(wd)
                ##find the index of the word
                wd_index=word_unique.index(wd)
                temp_list[wd_index] = num_wd
        train_xdata.append(temp_list)
    ##convert list to numpy array
    train_x=np.array(train_xdata)

    ##find the value of class0 and class1 and store them in train_ydata
    for i in range(class0_length):
        train_ydata.append(0)
    for i in range(class1_length):
        train_ydata.append(1)
    train_y = train_ydata

    clf_class = helper.strategy()
    clf_triained = clf_class.train_svm(parameters, train_x, train_y)
    '''
    svm_test_data = []
    for line0 in test_data:
        ###generate length=5718 value=0 list
        temp_list = []
        for i in range(len(word_unique)):
            temp_list.append(0)
        ##genenrate one line including num of words according to index
        for wd in word_unique:
            if wd in line0:
                ##the number of word in line
                num_wd = line0.count(wd)
                ##find the index of the word
                wd_index = word_unique.index(wd)
                temp_list[wd_index] = num_wd
        svm_test_data.append(temp_list)

    correct_rate = clf_triained.predict(svm_test_data)
    success_number=0
    for i in correct_rate:
        if i==0:
            success_number+=1

    length_test=len(correct_rate)
    print(length_test)
    success_rate=success_number/length_test
    print(correct_rate)
    print(success_rate)
    '''



    ##process class-0.txt
    class0_dict_unsorted={}
    for i in word_unique:
        class0_dict_unsorted[i]=0
    for line0 in class0_content:
        for line0_every_wd in line0:
            if line0_every_wd in class0_dict_unsorted:
                class0_dict_unsorted[line0_every_wd]+=1

    # print(sorted(class0_dict_unsorted.items(), key=lambda d: d[1], reverse=True))


    ##process class-1.txt

    class1_dict_unsorted = {}
    for i in word_unique:
        class1_dict_unsorted[i] = 0
    for line1 in class1_content:
        for line1_every_wd in line1:
            if line1_every_wd in class1_dict_unsorted:
                class1_dict_unsorted[line1_every_wd] += 1

    # print("class1: ",sorted(class1_dict_unsorted.items(), key=lambda d: d[1], reverse=True))
    # print("class0: ",sorted(class0_dict_unsorted.items(), key=lambda d: d[1], reverse=True))



    rubbish_words={}

    rate_0_1=class0_length/class1_length
    rate_1_0=class1_length/class0_length


    for i in word_unique:
        word_rate_class1_0=((class1_dict_unsorted[i]+1) *rate_0_1)/(class0_dict_unsorted[i]+1)
        if  1<word_rate_class1_0<1.25:
            rubbish_words[i]=0
    # print(rubbish_words)

    for i in word_unique:
        word_rate_class0_1=((class0_dict_unsorted[i]+1) *rate_1_0)/(class1_dict_unsorted[i]+1)
        if  1<word_rate_class0_1<1.25:
            rubbish_words[i]=0

    # print("nonsense words: ",rubbish_words)
    # if "government" in rubbish_words:
    #     print("not correct")

    class0_minus_class1 = {}
    for i in word_unique:
        class0_minus_class1[i] = 0

    class1_minus_class0={}
    for i in word_unique:
        class1_minus_class0[i]=0

    for wd in word_unique:
        for word0 in class0_dict_unsorted:
            if word0==wd:
                frequents0=class0_dict_unsorted[word0]
        for word1 in class1_dict_unsorted:
            if word1==wd:
                frequents1=class1_dict_unsorted[word1]

        class0_minus_class1[wd] = int(frequents0 - (frequents1 * rate_0_1))
        class1_minus_class0[wd] = int((frequents1*rate_0_1)-frequents0)

    # print(class1_minus_class0)

    for nosense_wd in rubbish_words:
        if nosense_wd in class1_minus_class0:
            class1_minus_class0[nosense_wd]=0
        if nosense_wd in class0_minus_class1:
            class0_minus_class1[nosense_wd]=0

    # print("class1: ",sorted(class1_minus_class0.items(), key=lambda d: d[1], reverse=True))

    # print("class0: ",sorted(class0_minus_class1.items(), key=lambda d: d[1], reverse=True))

    # return
    class0_prefered=sorted(class0_minus_class1.items(), key=lambda d: d[1], reverse=True)
    # class1_prefered=sorted(class1_minus_class0.items(), key=lambda d: d[1], reverse=True)
    modified_content=[]
    for test_line in test_data:
        select_words={}
        for test_word in test_line:
            select_words[test_word]=0
        for select_wd in select_words:
            if select_wd not in class1_minus_class0:
                select_words[select_wd]=float("-inf")
            else:
                select_words[select_wd]=class1_minus_class0[select_wd]
        select_words_sorted=sorted(select_words.items(), key=lambda d: d[1], reverse=True)
        # print(select_words_sorted)

        replace_words={}
        select_index=0
        for select_wd in select_words_sorted:
            if select_index>9:
                break
            else:
                replace_words[select_wd[0]]=0
                select_index+=1
        # print(replace_words)

        # return
        replace_already={}
        class0_used={}
        modified_list=[]
        for reday_word in test_line:
            replace_flag=0
            if reday_word in replace_words:
                replace_flag=1
            if replace_flag:
                for class0_top_wd in class0_prefered:
                    # if class0_top_wd[0]!=reday_word and class0_top_wd[0] not in class0_used:
                    if class0_top_wd[0] != reday_word :
                        if reday_word not in replace_already:
                            if class0_top_wd[0] not in class0_used:
                                if class0_top_wd[0] not in test_line:
                                    modified_list.append(class0_top_wd[0])
                                    replace_already[reday_word]=class0_top_wd[0]
                                    class0_used[class0_top_wd[0]]=0
                                    break
                        else:
                            add_word=replace_already[reday_word]
                            modified_list.append(add_word)
                            break
            else:
                modified_list.append(reday_word)
        # print("##############################################################################")
        # print(replace_words)
        # print(replace_already)
        # print(class0_used)
        # return
        modified_content.append(modified_list)

    modified_file="modified_data.txt"
    with open(modified_file,"w") as f:
        for every_line in modified_content:
            output=''
            space=" "
            length_thisline=len(every_line)
            for modified_wd_index in range(length_thisline-1):
                output+=every_line[modified_wd_index]+space

            next_line="\n"
            output+=every_line[length_thisline-1] + next_line
            f.write(output)

    svm_test_data=[]
    for line0 in modified_content:
        ###generate length=5718 value=0 list
        temp_list=[]
        for i in range(len(word_unique)):
            temp_list.append(0)
        ##genenrate one line including num of words according to index
        for wd in word_unique:
            if wd in line0:
                ##the number of word in line
                num_wd=line0.count(wd)
                ##find the index of the word
                wd_index=word_unique.index(wd)
                temp_list[wd_index] = num_wd
        svm_test_data.append(temp_list)

    correct_rate=clf_triained.predict(svm_test_data)

    success_number = 0
    for i in correct_rate:
        if i == 0:
            success_number += 1

    length_test = len(correct_rate)
    # print(length_test)
    success_rate = success_number / length_test
    # print(correct_rate)
    # print(success_rate)



    ## Write out the modified file, i.e., 'modified_data.txt' in Present Working Directory...
    
    test_data='./test_data.txt'
    ## You can check that the modified text is within the modification limits.
    modified_data='./modified_data.txt'
    assert strategy_instance.check_data(test_data, modified_data)
    return clf_class ## NOTE: You are required to return the instance of this class.

# fool_classifier()
