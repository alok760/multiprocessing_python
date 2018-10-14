import csv
from collections import defaultdict
import numpy as np
import multiprocessing
def fcount(a, b):
    b = np.bincount(a)
    ii = np.nonzero(b)[0]
    arr = str(list(zip(ii,b[ii])))
    print(arr)


if __name__ == '__main__':

    columns = defaultdict(list) # each value in each column is appended to a list

    with open('lymphography.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value
                columns[k].append(v) # append the value into the appropriate list
                                     # based on column name k

    p1=multiprocessing.Process(target=fcount, args=(columns['B'],'B'))
    p2=multiprocessing.Process(target=fcount, args=(columns['C'],'C'))
    p3=multiprocessing.Process(target=fcount, args=(columns['D'],'D'))
    p4=multiprocessing.Process(target=fcount, args=(columns['E'],'E'))
    p5=multiprocessing.Process(target=fcount, args=(columns['F'],'F'))
    p6=multiprocessing.Process(target=fcount, args=(columns['G'],'G'))
    p7=multiprocessing.Process(target=fcount, args=(columns['H'],'H'))
    p8=multiprocessing.Process(target=fcount, args=(columns['I'],'I'))
    p9=multiprocessing.Process(target=fcount, args=(columns['K'],'K'))
    p10=multiprocessing.Process(target=fcount, args=(columns['L'],'L'))
    p11=multiprocessing.Process(target=fcount, args=(columns['M'],'M'))
    p12=multiprocessing.Process(target=fcount, args=(columns['N'],'N'))
    p13=multiprocessing.Process(target=fcount, args=(columns['O'],'O'))
    p14=multiprocessing.Process(target=fcount, args=(columns['P'],'P'))
    p15=multiprocessing.Process(target=fcount, args=(columns['Q'],'Q'))
    p16=multiprocessing.Process(target=fcount, args=(columns['R'],'R'))
    p17=multiprocessing.Process(target=fcount, args=(columns['S'],'S'))
    p18=multiprocessing.Process(target=fcount, args=(columns['J'],'J'))


    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()
    p17.start()
    p18.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()
    p13.join()
    p14.join()
    p15.join()
    p16.join()
    p17.join()
    p18.join()
    print("done")
