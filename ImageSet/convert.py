import cv2 as cv
import matplotlib.pyplot as plt


def image_convert(r , g , b):
    
    img = cv.merge((r,g,b))
    #final_frame = cv.hconcat((img, map))

    #saves the merged image to a file
    #cv.imwrite("/test/Output/rgb.jpg",img)

    im_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    #im_rgb=cv.resize(im_rgb,dsize=(550,435))

    cv.imwrite('ImageSet/final_image.jpg', im_rgb)
    
    return im_rgb

# Grayscale image containing red values
red = cv.imread("ImageSet/JNCE_2022272_45C00088_V01-red.png",0)

# Grayscale image containing Blue values
blue = cv.imread("ImageSet/JNCE_2022272_45C00088_V01-blue.png",0)

# Grayscale image containing Green values
green = cv.imread("ImageSet/JNCE_2022272_45C00088_V01-green.png",0)

#Calling the Funcation as argument
image_convert(red , green , blue)