import PIL
from PIL import Image

def flip(im , dir):
    
    if dir == 'H':     #Flip to vertical direction
        #flip image
        out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        out.save('ImageSet/flipped.jpg')

    elif dir == 'V':    #Flip to horizontal direction
        #flip image
        out = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        out.save('ImageSet/flipped.jpg')

#read the image
im = Image.open("ImageSet/JNCE_2022272_45C00088_V01-mapprojected.png")
flip(im , 'H')