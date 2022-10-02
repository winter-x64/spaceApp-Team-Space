from PIL import Image

def rotate(im , angle = 0):
    #rotate image
    out = im.rotate(angle, expand=True)
    out.save('ImageSet/rotated.jpg')

#read the image
im = Image.open("ImageSet/JNCE_2022272_45C00088_V01-mapprojected.png")
rotate(im , 180)