import cv2 as cv

def image_convert(r , g , b , w = 1280 , h = 720):
    
    img = cv.merge((r,g,b))
    #final_frame = cv.hconcat((img, map))

    #saves the merged image to a file
    #cv.imwrite("/test/Output/rgb.jpg",img)

    im_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    im_rgb=cv.resize(im_rgb,dsize=(w, h))

    #cv.imwrite('ImageSet/final_image.jpg', im_rgb)
    
    return im_rgb