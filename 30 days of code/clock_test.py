def timeCompare(t1, t2):
    l=list(t1)
    l1=list(t2)
    if l[-2] > l1[-2]:
        print('Second')
    elif l[-2] < l1[-2]:
        print('First')
    else:
        if l[0]!=l1[0]:
            if l[0]>l1[0]:
                print('Second')
            else:
                print('First')
        elif l[1]!=l1[1]:
            if l[1]>l1[1]:
                print('Second')
            else:
                print('First')
        elif l[3] != l1[3]:
            if l[3]>l1[3]:
                print('Second')
            else:
                print('First')
        elif l[4] != l1[4]:
            if l[4]>l1[4]:
                print('Second')
            else:
                print('First')
        else:
            print('They are the same')






timeCompare('10:19PM','02:49AM');