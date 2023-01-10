import os
import sys
import re
import collections
from contextlib import redirect_stdout

z = collections.defaultdict(list)
d = []
dic = {}
for i in os.listdir(r'C:\Users\ashray\Desktop\New folder'):  # workspace path

    result = os.path.splitext(i)[0]
    # print(" ===",result)
    d.append(result)
# print(d)

my_str = ','.join(d)

# print(my_str)
l = my_str.split(',')
# print(l)

for keyAndValue in l:
    record = keyAndValue.split('#')
    if record[0] in dic:
        dic[record[0]].append(record[1])
    else:
        dic[record[0]] = [record[1]]
print(dic)


ans = []
for key in dic:
    sortedVals = sorted(dic[key], reverse=True)
    ans.append([key,sortedVals[0]])
    print(key, sortedVals[0])
# print(ans)
f = open('demo.txt','w')
print(ans, file=f) # Python 3.x


import boto3
s3 = boto3.resource('s3')
s3.Bucket('timothy12').upload_file('C:/Users/ashray/Desktop/bototests/demo.txt','demo.txt')






