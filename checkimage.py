from PIL import Image, ImageDraw, ImageFont

f = open('new_training.txt','r')

i=0
for l in f:
	if i > 10:
		break
	i+=1
	l = l.strip()
	l = l.split()
	if len(l) < 10:
		break
	add = l[0]
	x = list(map(float,l[1:6]))
	y = list(map(float,l[6:11]))
	img = Image.open(add).convert('RGBA')
	zipped = list(zip(x,y))
	
	new = Image.new('RGBA', img.size, (255,255,255,0))
	imgd = ImageDraw.Draw(new)

	imgd.point(zipped,fill='red')

	out = Image.alpha_composite(img, new)
	out = out.resize((400,400))
	out.show()


	
