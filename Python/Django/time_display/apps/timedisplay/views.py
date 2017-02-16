from django.shortcuts import render
import time
  # CONTROLLER!!!
  # Create your views here.
def index(request):
    context = {'time': time.strftime("%H:%M:%S"),
                'date': time.strftime("%m/%d/%Y")}
    return render(request, 'timedisplay/index.html', context)
