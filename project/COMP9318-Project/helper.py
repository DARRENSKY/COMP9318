from sklearn import svm

## Please do not change these functions...
class countcalls(object):
    __instances = {}
    def __init__(self, f):
        self.__f = f
        self.__numcalls = 0
        countcalls.__instances[f] = self
    def __call__(self, *args, **kwargs):
        self.__numcalls += 1
        return self.__f(*args, **kwargs)
    @staticmethod
    def count(f):
        return countcalls.__instances[f].__numcalls
    @staticmethod
    def counts():
        res = sum(countcalls.count(f) for f in countcalls.__instances)
        for f in countcalls.__instances:
            countcalls.__instances[f].__numcalls = 0
        return res
    
## Strategy() class provided to facilitate the implementation.
class strategy:
    ## Read in the required training data...
    def __init__(self):
        with open('class-0.txt','r') as class0:
            class_0=[line.strip().split(' ') for line in class0]
        with open('class-1.txt','r') as class1:
            class_1=[line.strip().split(' ') for line in class1]
        self.class0=class_0
        self.class1=class_1

    @countcalls
    def train_svm(parameters, x_train, y_train):
        ## Populate the parameters...
        gamma=parameters['gamma']
        C=parameters['C']
        kernel=parameters['kernel']
        degree=parameters['degree']
        coef0=parameters['coef0']
        
        ## Train the classifier...
        clf = svm.SVC(kernel=kernel, C=C, gamma=gamma, degree=degree, coef0=coef0)
        assert x_train.shape[0] <=541 and x_train.shape[1] <= 5720
        clf.fit(x_train, y_train)
        return clf
    
    ## Function to check the Modification Limits...(Modify EXACTLY 20- DISTINCT TOKENS)
    def check_data(self, original_file, modified_file):
        with open(original_file, 'r') as infile:
            data=[line.strip().split(' ') for line in infile]
        Original={}
        for idx in range(len(data)):
            Original[idx] = data[idx]

        with open(modified_file, 'r') as infile:
            data=[line.strip().split(' ') for line in infile]
        Modified={}
        for idx in range(len(data)):
            Modified[idx] = data[idx]

        for k in sorted(Original.keys()):
            record=set(Original[k])
            sample=set(Modified[k])
            assert len((set(record)-set(sample)) | (set(sample)-set(record)))==20
        return True


strategy_instance=strategy()
print(strategy_instance)