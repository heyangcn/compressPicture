import os
from PIL import Image
import re

startPath = '/var/www/html/pic/'
list = os.listdir(startPath)

count = 0

for pic in list:

    print("modify pic %s %s "%(pic,count))
    print(os.path.splitext(pic)[-1].lower())
    if(os.path.splitext(pic)[-1].lower() in ['.png' ,'.jpg','png']):
        path = startPath+pic
        im = Image.open(path)
        w,h = im.size
        w = w/2
        h = h/2
        out = im.resize((int(w),int(h)),Image.ANTIALIAS)
        newPic = re.sub(pic[:pic.rfind('.')],pic[:pic.rfind('.')]+'_new',pic)
        newPath = startPath+newPic
        out.save(newPath)
        count = count+1
    else:
        continue

print( 'end')
print( 'all translate pic is '+str(count))
