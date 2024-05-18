from django.db import models
import random,string
max_code_length = 8
filenamecode = 1

def upload_to_path(instance,filename):
    code = instance.code
    s = ''
    s += str(code)
    s+= '/'
    s += f'{filenamecode}.png'
    return s

def folder_name_generator():
    folder = "".join(random.choices(string.ascii_uppercase,k=max_code_length))
    return folder

def upload_to_path_face(instance,filename):
    code = instance.code   
    s = 'face to found/'
    s += str(code)
    s+= '/'
    s += f'{filenamecode}.png'
    return s
def upload_to_matched_face(instance,filename):
    s = f'matches/{instance.code}/{filename}'
    return s
# Create your models here.


class Room(models.Model):
    code = models.CharField(max_length=max_code_length,default="")
    def getcode(self):
        return self.code
    pic = models.FileField(upload_to=upload_to_path)
    created_at = models.DateTimeField(auto_now_add=True)
    

class ClientFaces(models.Model):
    code = models.CharField(max_length=max_code_length,default="")
    pic = models.FileField(upload_to=upload_to_path_face)
    
    
class Matches(models.Model):
    code = models.CharField(max_length=max_code_length,default="")
    pic = models.ImageField(upload_to=upload_to_matched_face)
    
def room_code_generator():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase,k=max_code_length))
        if Room.objects.filter(code=code).count() == 0:
            break 
    return code       
    
def value_from_object(obj,Room=Room):
    value = Room.value_from_object(obj)
    return Room.get_prep_value(value)