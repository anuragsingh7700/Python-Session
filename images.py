import requests
import os
#Create images folder if not there 
if not os.path.exists('images'):
    os.makedirs('images')

#Read links from images.txt file
with open('images.txt','r') as fp:
    for idx,line in enumerate(fp):
        url = line.strip()
        print('Starting Download for Image', idx+1)
        image = requests.get(url)
        open('images/img'+str(idx+1)+'.png', 'wb').write(image.content)
        print('Image',idx+1, 'downloaded')
        
os.remove('images.py')
