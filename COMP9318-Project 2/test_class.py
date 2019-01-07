

def test():
    a=[1,2,3,4,5]
    for i in a:
        if i!=1:
            if i%2==0:
                break
            else:
                print(i)

test()