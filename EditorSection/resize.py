from PIL import Image

def resize(im , w =1280 , h = 1080):
    #image size
    size=(w , h)
#resize image
    out = im.resize(size)
#save resized image
    out.save('ImageSet/resized.jpg')

#read the image
im = Image.open("ImageSet/JNCE_2022272_45C00088_V01-mapprojected.png")
resize(im , 1280 , 1080)