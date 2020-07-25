import re
from collections import Counter
import csv

def reader(filename):
    with open(filename) as f:
        log = f.read()
        #regedex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        regedex = r'\w+\.\w+\.\w+'
        hostnamelist = re.findall(regedex, log)
        return hostnamelist

def count(hostnamelist):
    return Counter(hostnamelist)

def write_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for item in counter:
            writer.writerow((item, counter[item]))

if __name__ == '__main__':
    write_csv(count(reader('hostname.txt')))