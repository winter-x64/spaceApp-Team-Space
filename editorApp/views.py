# Imports
import cv2 as cv
from django.shortcuts import render
from editorApp.utils.EditorSection.brightness import brightness
from editorApp.utils.EditorSection.contrast import contrast
from editorApp.utils.EditorSection.resize import resize
from editorApp.utils.EditorSection.sharpness import sharp
from editorApp.utils.imageConverter.image_converter import image_convert

 

# EndPoint For the uploads page
def upload(request):

    # GET Files from Client Server
    R_images = request.GET('red_ing')   #<-  Red image
    B_images = request.GET('blue_img')   #<-  Green image
    G_images = request.GET('green_img')   #<-  Blue image

    # Convert the image from grayscale to RGB
    ConvertImage = image_convert(R_images, G_images, B_images)
    cv.imwrite('static/img/final_output', ConvertImage)

    return render(request, 'uploads.html', {'final_image' : ConvertImage})

# EndPoint for the preview Page
def preview(request):

    return render(request, 'preview.html')

# EndPoint for the editor page
def editor(request):

    # GET Values from the Client Side
    brightnessValue = int(request.GET('brightnessValue'))
    contrastValue   = int(request.GET('contrastValue'))
    saturationValue = int(request.GET('saturationValue'))
    resizeValue     = int(request.GET('resizeValue'))
    bright_img = brightness('static/img/final_output/bright.img' , brightnessValue)
    # render output
    return render(request, 'editorPage.html')

# EndPoint For the downLoads
def download(request):
    return render(request, 'uploads.html')




