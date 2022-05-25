from re import I
from django.shortcuts import render
import json

# dictionary to store the urls and its respective numbers
global stories 
stories={}

#home page 
def homepage(request):
    file=open('media/web-stories/title-description.json')
    data=json.load(file)
    context={}
    i=1
    for d in data:
        stories[d['url']]=i
        i+=1     
    context['titles']=data
    return render(request,'home.html',context)

#web stories
def webstories(request,story):
    context={}
    webno=stories[story]
    file=open('media/web-stories/webstory-'+str(webno)+"/webstory-"+str(webno)+".json")
    data=json.load(file)
    context['data']=data
    context['webno']=webno
    file=open('media/web-stories/title-description.json')
    data=json.load(file)
    context['titles']=data[webno-1]
    return render(request,'webstory.html',context)