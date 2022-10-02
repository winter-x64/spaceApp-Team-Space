from PIL import Image, ImageEnhance


def sharp(imgPath , factor = 1):

    im = Image.open(imgPath)

    enhancer = ImageEnhance.Sharpness(im)

    im_s_1 = enhancer.enhance(factor)
    #im_s_1.save('ImageSet/sharpened.jpg');
    return im_s_1


#read the image
# im = Image.open("ImageSet/JNCE_2022272_45C00088_V01-mapprojected.png")
# sharp(im , 1.5)
#1-200 value