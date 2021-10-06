import os

with open('websites.txt','r') as fp:
    for line in fp:
        website = line.strip().split()[0]
        os.system('ping '+ website +' -c 1')


