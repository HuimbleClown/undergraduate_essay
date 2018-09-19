from numpy import vstack
from scipy.cluster.vq import kmeans,vq
import os
from os import path
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# list1=[88.0,64.0,96.0,85.0]
# list2=[92.0,99.0,95.0,94.0]
# list3=[91.0,87.0,99.0,95.0]
# list4=[78.0,99.0,97.0,81.0]
# list5=[88.0,78.0,98.0,84.0]
# list6=[100.0,95.0,100.0,92.0]       #六位同学的成绩

# list1=[0.00745582,0.000337162,0.303598,0.00335684,0.000339416,0.000857451]
# list2=[0.00211277,0.0120908,0.236464,0.000760969,3.21146e-07,1.09857e-05]
# list3=[0.00937246,0.0190569,0.273947,0.00282483,4.07671e-05,0.000687217]
# list4=[0.00670009,0.00293428,0.110264,0.00846742,1.46826e-05,0.0399336]
# list5=[0.0207798,0.00995024,0.157331,0.0176193,0.000402534,0.049079]
# list6=[0.0177039,0.0438319,0.383074,0.0022127,2.34049e-06,0.0101559]
#
# dat = (list1,list2,list3,list4,list5,list6)
# print(dat)

test = []
with open("k300.txt") as f:
    for line in f:
        tmp = line.strip().split(" ")
        tmp = list(map(float, tmp))
        test.append(tmp)
# test = list(map(int,test))
test = tuple(test)
print(test)
print(type(test))


'''vstack:堆积成绩数据'''
#data = vstack((list1,list2,list3,list4,list5,list6))
data = vstack(test)
centroids,_ = kmeans(data,9)    #kmeans函数返回的centroids就是聚类中心；2表示分类的类别数目
result,_ = vq(data,centroids)      #vq函数用来获取每一位同学所属的类

#print(result)
print(type(result.tolist()))
with open("result.txt","w") as f:
    for i in result.tolist():
        f.write(str(i)+"\n")


