from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Room,room_code_generator,ClientFaces,Matches
from .forms import ImagesForm
from .album import get_encodings
from .recognize import recognize
from imutils import paths
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def Host(request): 
    images = Room.objects.all()
    context = {'images': images}
    return render(request, "host.html", context)

def fileupload(request):
    form = ImagesForm(request.POST, request.FILES)
    if request.method == 'POST':
        images = request.FILES.getlist('pic')
        cd = room_code_generator()
        for image in images:
            image_ins = Room(code=cd,pic = image)
            image_ins.save()
        files = Room.objects.all()
        context = {'images':files,'code':cd}            
        return render(request, "host.html", context)
    context = {'form': form}
    return render(request, "upload.html", context)


def faceupload(request):
    form = ImagesForm(request.POST, request.FILES)
    roomcode = request.GET.get('roomcode',None)
    if request.method == 'POST':
        images = request.FILES.getlist('pic')
        cd = room_code_generator()
        for image in images:
            image_ins = ClientFaces(code=cd,pic = image)
            image_ins.save()
        images = ClientFaces.objects.all()
        context = {'form':form,'images':images,'code':cd,'roomcode':roomcode}
        return render(request, "facefinder.html", context)
    context = {'form': form,'roomcode':roomcode}
    return render(request, "facefinder.html", context)

def roomcode(request):
    rmcode = Room.objects.values_list('code')
    pathtoinputdata = settings.MEDIA_ROOT
    codellist = list(rmcode)
    cwdcode = codellist[-1][0]
    pathtoinputdata += '/'
    pathtoinputdata += cwdcode
    datapaths = list(paths.list_images(pathtoinputdata))
    get_encodings(datapaths,cwdcode)
    context = {'code': cwdcode}
    return render(request,'roomcode.html',context)

@csrf_protect
def findfaces(request):
    if(request.method == 'POST'):
        code = request.POST.get('code',None)
        rmcode = request.POST.get('roomcode',None)
        recognize(code,rmcode)
        matches = Matches.objects.all()
        context = {'code':code,'images':matches}
        return render(request,'matches.html',context)
    
    


def Home(request):
    return render(request,"index.html") 

def Client(request):
    if(request.method == 'POST'):
        room = request.POST.get('code',None)
        images = Room.objects.all()
        context = {'room': room,'images':images}
        return render(request,'room.html',context)
    return render(request,'client.html')

    
        
