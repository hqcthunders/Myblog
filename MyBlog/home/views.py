from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import magic
import os
# Create your views here.


def index(request):
    return render(request, 'pages/home.html')


def errors(request):
    return render(request)


def check_file(request):
    if request.method == 'POST' and request.FILES['myfiles']:
        myfile = request.FILES['myfiles']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        type_file = magic.from_file(uploaded_file_url[1:])
        os.remove(uploaded_file_url[1:])
        return render(request, 'pages/checkfile.html', {
            'uploaded_file_url': type_file
        })
    return render(request, 'pages/checkfile.html')
