## import modules here 
import pandas as pd
import numpy as np


################# Question 1 #################

# helper functions
def project_data(df, d):
    # Return only the d-th column of INPUT
    return df.iloc[:, d]

def select_data(df, d, val):
    # SELECT * FROM INPUT WHERE input.d = val
    col_name = df.columns[d]
    return df[df[col_name] == val]

def remove_first_dim(df):
    # Remove the first dim of the input
    return df.iloc[:, 1:]

def slice_data_dim0(df, v):
    # syntactic sugar to get R_{ALL} in a less verbose way
    df_temp = select_data(df, 0, v)
    return remove_first_dim(df_temp)

def fcopy(before_L):
    after_L=[]
    for i in before_L:
        after_L.append(i)
    return after_L

def oneDim(input_data):
    loc_dvalue = input_data.loc[0]
    dvalues = list(loc_dvalue)
    newL = []
    exculde_last = dvalues[:-1]
    newL.append(exculde_last)
    copyL1=[]
    copyL1.append(exculde_last)
    for i, dvalue in enumerate(newL):
        templist=fcopy(dvalue)
        for j,jvalue in enumerate(templist):
            if jvalue!='ALL':
                anotherlist=fcopy(templist)
                anotherlist[j]='ALL'
                if anotherlist not in newL:
                    newL.append(anotherlist)
            # if dvalue != 'ALL':
            #     copyL2 = fcopy(copyL1)
            #     copyL2[i] = 'ALL'
            #     newL.append(copyL2)
    # all_list = []
    # for i in exculde_last:
    #     all_list.append('ALL')
    # newL.append(all_list)
    for i in newL:
        i.append(dvalues[-1])
    title_name = list(input_data)
    newList = pd.DataFrame(newL, columns=title_name)
    return newList
def buc_rec_optimized(df):# do not change the heading of the function
    input_data=df
    dimension=input_data.shape[0]
    if dimension==1:
        out=oneDim(input_data)
    if dimension!=1:
        title=list(input_data)
        out=pd.DataFrame(columns=title)
        list1=[]
        list2=[]
        buc(input_data,list1,list2)
        for i in list2:
            out.loc[len(out)]=i
    return out
def buc(input_data,list1,list2):
    dims=input_data.shape[1]
    if dims==1:
        input_sum=sum(project_data(input_data,0))
        list1.append(input_sum)
        list2.append(list1)
    else:
        dimension0_values=set(project_data(input_data,0).values)
        l1=fcopy(list1)
        for dimension0_val in dimension0_values:
            l2=fcopy(l1)
            l2.append(dimension0_val)
            branch_data=slice_data_dim0(input_data,dimension0_val)
            buc(branch_data,l2,list2)
        branch_data=remove_first_dim(input_data)
        l2=fcopy(l1)
        l2.append('ALL')
        buc(branch_data,l2,list2)    

################# Question 2 #################
def sse(arr):
    if len(arr) == 0: # deal with arr == []
        return 0.0

    avg = np.average(arr)
    val = sum( [(x-avg)*(x-avg) for x in arr] )
    return val
def v_opt_dp(x, num_bins):# do not change the heading of the function
    matrix=[]
    for i in range(num_bins):
        L=[]
        for j in range(len(x)):
            L.append(-1)
        matrix.append(L)
    index=[]
    for i in range(num_bins):
        L=[]
        for j in range(len(x)):
            L.append(-1)
        index.append(L)
    for i in range(num_bins):
        for j in range(len(x)):
            if (num_bins-i-j)>=2:
                continue
            if len(x)-j<=i:
                continue
            if i==0:
                matrix[i][j]=sse(x[j:])
            if i!=0:
                list1=[]
                for k in range(j,len(x)):
                    temp1=sse(x[j:k+1])
                    if (k+1)<=len(x)-1:
                        temp2=temp1+matrix[i-1][k+1]
                    list1.append(temp2)
                min_1=min(list1)
                matrix[i][j]=min_1
                tempnum=j+1
                for q in list1:
                    if q==min_1:
                        index[i][j]=tempnum
                        break
                    tempnum += 1


                # temp1=[]
                # r1=x[j]
                # r2=x[j+1]
                # temp1.append(r1)
                # temp1.append(r2)
                # newerror=sse(temp1)
                # c1=0+matrix[i-1][j+1]
                # c2=0
                # if (j+2) <len(x):
                #     c2=newerror+matrix[i-1][j+2]
                # matrix[i][j]=min(c1,c2)
                # if i>0:
                #     if c1==min(c1,c2):
                #         index[i][j]=j+1
                #     if c2==min(c1,c2):
                #         if (j+2)>len(x)-1:
                #             index[i][j]=len(x)-1
                #         else:
                #             index[i][j]=j+2
    print(index)
    begin=index[-1][0]
    res=[]
    before=begin
    res.append(x[0:begin])

    for i in range(len(index) - 2, 0, -1):
        temp=index[i][begin]
        begin=temp
        # begin= index[i][begin]
        res.append(x[before:begin])
        before = begin
    res.append(x[before:])
    bins=res

    return matrix,bins