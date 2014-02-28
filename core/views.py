from django.shortcuts import render

from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext

def index(request):
    return render_to_response('home/home.html',context_instance = RequestContext(request))
