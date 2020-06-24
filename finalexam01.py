def m(i):
    pi=0;
    for k in range(1,i+1):
        pi=pi +pow(-1,k+1)/(2*k-1)
    pi=4*pi
    return pi



if __name__ == "__main__":
    print('i                 m(i)')
    for i in range(1,1000,100):
        print('{0:<3d}             {1:f}'.format(i,m(i)))
