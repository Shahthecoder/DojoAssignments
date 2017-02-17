from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'first_app/index.html')

def all_ninjas(request):

    return render(request, 'first_app/ninjas.html')

def one_ninja(request, color):

    if color == 'red':
        img = 'raph.jpg'
    elif color == 'blue':
        img = 'leo.jpg'
    elif color == 'orange':
        img = 'mike.jpg'
    elif color == 'purple':
        img = 'don.jpg'
    else:
        img = 'fox.jpg'

    context = {'img': img}

    return render(request, 'first_app/ninja.html', context)
