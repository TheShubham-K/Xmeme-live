from django.core.files.base import ContentFile
from django.http import response
from rest_framework import status
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from .forms import memesForm
import json
from .models import memes

# Create your views here.

# memes list 
def memes_List(request):
    context = {'memes_List' : memes.objects.all().order_by('-id') }
    return render(request, "Xmeme/memes_List.html",context)

# memes forms
def memes_form(request, id=0):
    try:
        if request.method == 'GET':
            if id==0:
                form = memesForm()
            else:
                meme = memes.objects.get(pk=id)
                form = memesForm(instance=meme)    
            return render(request, "Xmeme/memes_form.html", {'form': form})
        else:
            if id == 0:
                form = memesForm(request.POST)
            else:
                meme = memes.objects.get(pk=id)
                form = memesForm(request.POST,instance=meme)
            if form.is_valid():
                form.save()
            return redirect('/')
    except memes.DoesNotExist:
        raise Http404('Page not found')

# memes delete options
def memes_delete(request, id):
    meme = memes.objects.get(pk=id)
    meme.delete()
    return redirect('/')

# memes json for particular id
def memes_json(request, id):
    try:
        obj = memes.objects.filter(pk=id)
        if obj != None:
            data = serialize("json", obj, fields=('id', 'name', 'captions', 'url'))
            return HttpResponse(data, content_type="application/json")
    except memes.DoesNotExist:
        raise Http404('page not found')
    

    

# memes json for all id
def memes_json_all(request):
    # context = {
    #     'meme_list': memes.objects.all(),
    # }
    # return render(request, "Xmeme/memes_json_all.html", context)
    obj = memes.objects.all()
    data = serialize("json", obj, fields=('id', 'name', 'captions', 'url'))
    return HttpResponse(data, content_type="application/json")