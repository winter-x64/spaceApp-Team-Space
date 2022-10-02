# Imports
from django.shortcuts import render
from editorApp.utils.imageConverter.image_converter import image_convert

# EndPoint For the uploads page
def upload(request):

    # GET Files from Client Server
    R_images = request.GET('warmthValue')   #<-  Red image
    B_images = request.GET('warmthValue')   #<-  Green image
    G_images = request.GET('warmthValue')   #<-  Blue image

    # Convert the image from grayscale to RGB
    ConvertImage = image_convert(R_images, G_images, B_images)

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
    warmthValue     = int(request.GET('warmthValue'))

    # render output
    return render(request, 'editorPage.html')

# EndPoint For the downLoads
def download(request):
    return render(request, 'uploads.html')