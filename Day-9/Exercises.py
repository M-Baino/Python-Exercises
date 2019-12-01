import statistics as st 
x = [3,1.5,4.5,6.75,2.25,5.75,2.25]

print("_________Question1__________")

print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))


print("_________Question2__________")
import random

print(random.random())
print(random.randrange(10))
print(random.choice(["Ali","Khalid","Hussam"]))
print(random.sample(range(1000),10))
print(random.choice("Orange Academy"))

y = [1,5,8,9,2,4]
random.shuffle(y)
print(y)

print(random.randint(10,20))
print(random.randrange(1000,2111,5))
print(random.randint(10,20))
print(random.uniform(10000,11000))


print("_________Question3__________")
import math

print (math.pi)
print(math.cos(200))
print(math.sin(200))
print(math.tan(200))
print(math.floor(10.8))
print(math.ceil(10.8))


print("_________Question4__________")
from PIL import Image , ImageFilter, ImageDraw

download = Image.open("download.jpg")
download2 = Image.open ("download2.jpg")
print(download.format, download.size , download.mode)

mohamamd_flip = download.transpose(Image.FLIP_TOP_BOTTOM)
mohamamd_flip.show()

download_grey = download.convert("L")
download_grey.show()

download_cropped = download.crop((0,0,50,50))
download_cropped.show()

download_draw = Image.open("download.jpg")
draw = ImageDraw.Draw(download_draw)
draw.line((0,0) + download_draw.size , fill = (255,255,255))
draw.line((0, download_draw.size[1], download_draw.size[0], 0 ) , fill = (255,255,255))
draw.text((download_draw.size[0]/2 - download_draw.size[0]/2 , download_draw.size[1]/2 + 20) , "download",
          fill=(255,255,0))
download_draw.show()


download_enhaced = download.filter(ImageFilter.EDGE_ENHANCE)
download_enhaced.show()


download_find = download.filter(ImageFilter.FIND_EDGES)
download_find.show()



download_smooth = download.filter(ImageFilter.SMOOTH)
download_smooth.show()

download_sharpen = download.filter(ImageFilter.SHARPEN)
download_sharpen.show()

alpha = 0.5
download2 = Image.open("download2.jpg").resize(download.size)

Image.blend(download , download2 , alpha).save(
        "download_blend.jpg".format(alpha))

download_blend = Image.open("download_blend.jpg")
download_blend.show()

download_blur = download.filter(ImageFilter.BLUR)
download_blur.show()


size = (128,128)
saved = ("download_thumbnail.jpg")
download_thumbnail = Image.open("download.jpg")
download_thumbnail.thumbnail(size)
download_thumbnail.save(saved)
download_thumbnail.show()

download_rot_90 = download.rotate(90)
download_rot_90.show()




download2 = Image.open("download2.jpg").resize(download.size)
mask = Image.open("mask.jpg")
mask = mask.resize(download.size)

Image.composite(download,download2,mask).save(
        "download_mask.jpg")

download_mask = Image.open("download_mask.jpg")
download_mask.show()