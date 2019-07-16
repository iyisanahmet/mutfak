from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'customer/index.html')


def manager(request):
    if 2==2:
        return render(request,'manager/index.html')
    else:
        return HttpResponse('Unauthorized for Manager Module')
