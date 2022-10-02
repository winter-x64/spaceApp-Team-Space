from PIL import ImageEnhance


def brightness(im , factor = 1):
    #image brightness enhancer
    enhancer = ImageEnhance.Brightness(im)

    im_output = enhancer.enhance(factor)
    #im_output.save('ImageSet/bright.jpg')
    return im_output


#read the image
# im = Image.open("ImageSet/JNCE_2022272_45C00088_V01-mapprojected.png")
# brightness(im , 1.5)
#1-10 value