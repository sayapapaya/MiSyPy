from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def index(request):
    #template = loader.get_template("index.html")
    #return HttpResponse(template.render())
    return render_to_response('index.html')