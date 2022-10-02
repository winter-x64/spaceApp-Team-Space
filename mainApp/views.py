from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def landingPage(request):
    return render(request, 'landingPage.html', {'title': 'Hello'})

def aboutPage(request):
    return render(request, 'aboutUs.html')