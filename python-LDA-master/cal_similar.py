import numpy as np
import math

def Cosine(vec1, vec2):
    npvec1, npvec2 = np.array(vec1), np.array(vec2)
    return npvec1.dot(npvec2)/(math.sqrt((npvec1**2).sum()) * math.sqrt((npvec2**2).sum()))


k = 9

data = np.loadtxt("k%d.txt" % k)
print(type(data))
print(data.shape)

#print(Cosine(data[1],data[4]))

# corre = 0
# for i in range(0, k):
#     for j in range(i+1,k):
#         corre = corre + Cosine(data[i],data[j])
#
# print(corre/k/(k-1)*2)

# file = open("data1.txt","w")
# for i in range(0, 50):
#     for j in range(i+1,50):
#         corre = Cosine(data[i],data[j])
#         if corre > 0.4:
#             file.write(str(i)+" "+str(j)+" "+str(corre)+" ")
#     file.write("\n")
# file.close()



file = open("data2.txt","w")
for i in range(0, 50):
    for j in range(0,50):
        corre = Cosine(data[i],data[j])
        file.write(str(corre)+" ")
    file.write("\n")
file.close()




