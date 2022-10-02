from django.shortcuts import render

# ? Create your views here.
# EndPoint for the editor page
def editor(request):
    return render(request, 'editorPage.html')

# EndPoint for the preview Page
def preview(request):
    return render(request, 'preview.html')

# EndPoint For the uploads page
def upload(request):
    return render(request, 'uploads.html')

# EndPoint For the uploads page
def download(request):
    return render(request, 'uploads.html')