from django.urls import path
from .views import Host,Home,Client,fileupload,roomcode,faceupload,findfaces

urlpatterns = [
    path('host/',Host),
    path('home/',Home),
    path('client/',Client),
    path('host/upload',fileupload, name = "File_Uploads"),
    path('host/roomcode',roomcode,name='roomcode'),
    path('client/facefinder/',faceupload),
    path('client/facefinder/findfaces',findfaces)
]
