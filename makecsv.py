import csv
import hashlib
import os
import random
import sys
import hashlib
# Define folder where the log files are located
source_folder = 'drebin/samples/'
dest_folder = 'drebin'

# List of all the files
# dataset = [x for x in os.listdir(source_folder) if x.endswith(".apk")]
def rnd_mal_ben():
    if(random.random()>0.5):
        return "mal"
    return "ben"

def makeCsv(l,folder,csvname):
    f = open(f'{folder}/{csvname}', 'w',newline='')
    writer = csv.writer(f)
    print(l)
    writer.writerows(l)
    print(writer)
    f.close()

def csvnames(csvname):
    l = []
    l.append(['sha256','family'])
    data= [x for x in os.listdir("drebin/feature_vectors")]
    print(data)
    for x in data:
        l.append([x,'Plankton'])

    makeCsv(l,dest_folder,csvname)


if __name__ == '__main__':

    csvnames('sha256_family.csv')
    print(f"csvsaved.")