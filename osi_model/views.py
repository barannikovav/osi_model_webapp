'''Django base views for osi model webapp'''
from django.shortcuts import render

def index(request):
    '''Main page'''
    return render(request, "osi_model/index.html")
