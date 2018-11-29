import csv
from operator import itemgetter
import math
import random

class knn(object):

    def __init__(self, x1, x2, x3, x4, x5, y):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.y = y

data_set = []

# EXTRACT FILE CSV, BAGI MENJADI DATA TRAIN DAN DATA TEST

with open('DataTrain_Tugas3_AI.csv') as data:
    reader = csv.DictReader(data)
    i = 1
    for row in reader:
        data_set.append(knn(float(row['X1']), float(row['X2']), float(row['X3']), float(row['X4']), float(row['X5']), float(row['Y'])))

random.shuffle(data_set)

bestAccu = 0

for k in range(1, 301):
    
    totalAccu = 0

    for fold in range(10):

        data_train = []
        data_test = []
        n = 0

        #PEMBAGIAN DATA TRAIN DAN TEST DENGAN CROSS VALIDATION
        for i in range(len(data_set)):
            if (n < 80) and (i >= fold*80):
                data_test.append(data_set[i])
                n += 1
            else:
                data_train.append(data_set[i])
        # print(len(data_test))
        # print(len(data_train))

        correct = 0

        for test in data_test:

            neighbour = []
            tempy = 0

            for train in data_train:

                # HITUNG JARAK EUCLIDEAN
                euclid = math.sqrt( ((test.x1-train.x1)**2) + ((test.x2-train.x2)**2) + ((test.x3-train.x3)**2) + ((test.x4-train.x4)**2) + ((test.x5-train.x5)**2) )
                kelas = train.y

                # MENGELOMPOKKAN JARAK EUCLIDEAN NYA KEMUDIAN DI URUTKAN BERDASARKAN JARAK TERKECIL
                neighbour.append([euclid, kelas])
                
            neighbour.sort(key=itemgetter(0))
            
            count0 = 0
            count1 = 0
            count2 = 0
            count3 = 0

            #MENGHITUNG JUMLAH MASING-MASING KELAS YANG TERMASUK K-NEIGHBOUR
            for i in range(k):
                if (neighbour[i][1] == 0):
                    count0 += 1
                elif (neighbour[i][1] == 1):
                    count1 += 1
                elif (neighbour[i][1] == 2):
                    count2 += 1
                elif (neighbour[i][1] == 3):
                    count3 += 1

            # MENENTUKAN KELAS UNTUK DATA TESTING
            if max(count0,count1,count2,count3)==count0:
                tempy = 0
            elif max(count0,count1,count2,count3)==count1:
                tempy = 1
            elif max(count0,count1,count2,count3)==count2:
                tempy = 2
            elif max(count0,count1,count2,count3)==count3:
                tempy = 3

            # print(tempy,test.y)

            if tempy==test.y:
                correct += 1

        # print(correct)
        accuracy = correct/len(data_test)*100
        totalAccu += accuracy

    avgAccu = totalAccu/10
    if avgAccu >= bestAccu:
        bestAccu = avgAccu
        bestK = k

print(bestK)
print(bestAccu)