from PIL import Image, ImageDraw, ImageFont
import numpy as np

f = open('new_training_frontal.txt','r')
pred=np.load('output.npy')
a=np.ndarray.tolist(pred)
i=0
for l in f:
	if i >= 2500 and i<4000:
        l = l.strip()
        l = l.split()
        add = l[0]
        x = list(map(float,a[i-2500][0:5]))
        y = list(map(float,a[i-2500][5:10]))
        img = Image.open(add).convert('RGBA')
        zipped = list(zip(x,y))

        new = Image.new('RGBA', img.size, (255,255,255,0))
        imgd = ImageDraw.Draw(new)

        imgd.point(zipped,fill='red')

        out = Image.alpha_composite(img, new)
        out = out.resize((400,400))
        out.show()
    i+=1
f.close()
	
