from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "brochure/index.html")

def pj(request):
    return render(request, "brochure/class11/physics.html")

def cj(request):
    return render(request, 'brochure/class11/chemistry.html')

def mj(request):
    return render(request, 'brochure/class11/maths.html')

def ps(request):
    return render(request, 'brochure/class12/physics.html')

def cs(request):
    return render(request, 'brochure/class12/chemistry.html')

def ms(request):
    return render(request, 'brochure/class12/maths.html')