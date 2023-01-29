from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=="POST":
        tn=request.POST["topic"]
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse("Topic inserted sucessfully!!!!!")
    return render(request,"insert_topic.html")

def insert_webpages(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=="POST":
        topic=request.POST["topic"]
        n=request.POST["name"]
        u=request.POST["url"]
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        N=Webpage.objects.get_or_create(topic_name=T,name=n,url=u)[0]
        N.save()
        return HttpResponse("Web page data add sucessfully!!!!")
    return render(request,"insert_webpages.html",d)


def insert_accessrecords(request):
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    if request.method=="POST":
        n=request.POST["name"]
        da=request.POST["date"]
        T=Webpage.objects.get_or_create(name=n)[0]
        T.save()
        N=Acessrecords.objects.get_or_create(name=T,date=da)[0]
        N.save()
        return HttpResponse("access records sucessfully!!!!")
    
    return render(request,"insert_accessrecords.html",d)
