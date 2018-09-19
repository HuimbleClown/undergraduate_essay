f=open('a.txt')
for line in f:
    numarray=[float(value) for value in line.split()]
    amax=max(numarray)
    index=numarray.index(amax)
    print(index)
