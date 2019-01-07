from sklearn import svm

x=[[0,0],[1,1]]
y=[0,1]
clf=svm.SVC()
a1=clf.fit(x,y)
print(a1)
a2=clf.predict([[-1,-1]])
print(a2)
# a3=clf.support_vectors_
# print(a3)
# a4=clf.support_
# print(a4)
# a5=clf.n_support_
# print(a5)
# x=[[0],[1],[2],[3]]
# y=[0,1,2,3]
# clf=svm.SVC(decision_function_shape='ovo')
# clf.fit(x,y)