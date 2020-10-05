from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'allpages/index.html',{'title': 'HOME'})

def about_view(request):
    return render(request, 'allpages/about.html',{'title': 'ABOUT US'})

def privacy_view(request):
    return render(request, 'allpages/privacy.html',{'title': 'PRIVACY POLICY'})