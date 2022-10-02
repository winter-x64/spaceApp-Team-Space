from PIL import Image, ImageEnhance


def sharp(im , factor = 1):
    enhancer = ImageEnhance.Sharpness(im)

    im_s_1 = enhancer.enhance(factor)
    im_s_1.save('ImageSet/sharpened.jpg');
    
    
#read the image
im = Image.open("ImageSet/JNCE_2022272_45C00088_V01-mapprojected.png")
sharp(im , 1.5)
