# Imports
# import cv2 as cv
from django.shortcuts import render
from editorApp.utils.EditorSection.brightness import brightness
from editorApp.utils.EditorSection.contrast import contrast
from editorApp.utils.EditorSection.resize import resize
from editorApp.utils.EditorSection.sharpness import sharp
# from editorApp.utils.imageConverter.image_converter import image_convert



# EndPoint For the uploads page
def upload(request):

    # GET Files from Client Server
    # R_images = request.GET('red_ing')   #<-  Red image
    # B_images = request.GET('blue_img')   #<-  Green image
    # G_images = request.GET('green_img')   #<-  Blue image

    # Convert the image from grayscale to RGB
    # ConvertImage = image_convert(R_images, G_images, B_images)

    # cv.imwrite('img/finalOutput/final_converted_image.jpg', ConvertImage)

    return render(request, 'uploads.html')


# EndPoint for the preview Page
def preview(request):

    output_img = 'img/finalOutput/final_converted_image.jpg'

    return render(request, 'preview.html', {'finalOutput': output_img})


# EndPoint for the editor page
def editor(request):

    # GET Values from the Client Side
    brightnessValue = int(request.GET('brightnessValue'))
    contrastValue   = int(request.GET('contrastValue'))
    sharpnessValue  = int(request.GET('sharpnessValue'))
    resizeValue     = int(request.GET('resizeValue'))

    # # Image Path
    output_img = 'img/finalOutput/final_converted_image.jpg'

    bright_img = brightness(output_img , brightnessValue)
    contrast_img = contrast(output_img , contrastValue)
    sharpnessValue_img = sharp(output_img , sharpnessValue)
    resizeValue_img = resize(output_img , resizeValue)

    # render output
    return render(request, 'editorPage.html', {'finalImage': output_img})

# EndPoint For the downLoads
def download(request):
    return render(request, 'uploads.html')




