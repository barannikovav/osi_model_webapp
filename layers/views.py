from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "layers/index.html")

def detail(request, layer_id):
    return HttpResponse("You're looking at layer %s." % layer_id)

def test(request, layer_id):
    return HttpResponse("You're taking a test on the layer %s." % layer_id)
    