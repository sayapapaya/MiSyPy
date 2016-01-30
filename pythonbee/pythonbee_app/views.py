from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def index(request):
    #template = loader.get_template("index.html")
     #C:\Python27\lib\site-packages\django\contrib\admin\templates\templates\index.html
    #return HttpResponse("Hello, world. You're now at the pythonbee index.")
    #return HttpResponse(template.render())
    print ("\pythonbee_app\test")
    #return render_to_response("\\pythonbee_app\\template\\index.html")
    #return render_to_response("C:/Users/Saya/Documents/MiSyPy/MiSyPy/pythonbee/pythonbee_app/templates/index.html")
    return render_to_response('index.html')