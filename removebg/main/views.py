from django.shortcuts import render

# Create your views here.


def upload_pg(request):
    return render(request,'upload.html')

def result_pg(request):
    return render(request,'result.html')