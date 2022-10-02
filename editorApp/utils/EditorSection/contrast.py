from PIL import Image, ImageEnhance

def contrast(imgURL , factor = 1):

    # open image
    im = Image.open(imgURL)

    #image brightness enhancer
    enhancer = ImageEnhance.Contrast(im)

    im_output = enhancer.enhance(factor)
    #im_output.save('ImageSet/contra.jpg')

    return im_output


#read the image
# im = Image.open("ImageSet/JNCE_2022272_45C00088_V01-blue.png")
# contrast(im , 1.5)
#1-20 value
