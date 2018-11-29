import csv
from operator import itemgetter
import math

class knn(object):

    def __init__(self, x1, x2, x3, x4, x5, y):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.y = y

def hitungEuclid(a1 ,a2 ,b1 ,b2 ,c1 ,c2 ,d1 ,d2 ,e1 ,e2):
    return math.sqrt( ((a1-a2)**2) + ((b1-b2)**2) + ((c1-c2)**2) + ((d1-d2)**2) + ((e1-e2)**2) )

data_train = []
data_test = []

# EXTRACT FILE CSV, BAGI MENJADI DATA TRAIN DAN DATA TEST

with open('DataTrain_Tugas3_AI.csv') as data:
    reader = csv.DictReader(data)
    for row in reader:
        data_train.append(knn(float(row['X1']), float(row['X2']), float(row['X3']), float(row['X4']), float(row['X5']), float(row['Y'])))

with open('DataTest_Tugas3_AI.csv') as data:
    reader = csv.DictReader(data)
    for row in reader:
        data_test.append(knn(float(row['X1']), float(row['X2']), float(row['X3']), float(row['X4']), float(row['X5']), None))

# TENTUKAN PARAMETER K DI SINI
k = 13

for test in data_test:

    neighbour = []

    for train in data_train:

        # HITUNG JARAK EUCLIDEAN
        euclid = hitungEuclid(test.x1 ,train.x1 ,test.x2 ,train.x2 ,test.x3 ,train.x3 ,test.x4 ,train.x4 ,test.x5 ,train.x5)
        kelas = train.y

        # MENGELOMPOKKAN JARAK EUCLIDEAN
        neighbour.append([euclid, kelas])

    # MENGURUTKAN BERDASARKAN JARAK EUCLIDEAN TERKECIL
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

    #MENENTUKAN KELAS UNTUK DATA TESTING
    if max(count0,count1,count2,count3)==count0:
        test.y = 0
    elif max(count0,count1,count2,count3)==count1:
        test.y = 1
    elif max(count0,count1,count2,count3)==count2:
        test.y = 2
    elif max(count0,count1,count2,count3)==count3:
        test.y = 3

    # print(test.y)

with open('TebakanTugas3.csv', 'w', newline='') as csvfile:
    fieldnames = ['Y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(data_test)):
        writer.writerow({'Y': data_test[i].y})