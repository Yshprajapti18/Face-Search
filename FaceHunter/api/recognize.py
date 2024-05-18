import os
import cv2 
import pickle
import face_recognition
import argparse
from .models import Matches
from django.conf import settings
from .forms import ImagesForm
from django.core.files import File


def recognize(code,roomcode):
# Load the reference encodings created in the script album.py
    path_to_pickle = str(settings.BASE_DIR) + '/' + str(roomcode) + '.pickle'
    data = pickle.loads(open(path_to_pickle, "rb").read())
    print(path_to_pickle)
    # Make the argument parser and parse the arguments
    # ap = argparse.ArgumentParser()

    # Provide a path to the directory containing test images and 
    # a path to the directory where you would like to save your output data
    
    
    test_dir = os.path.join(settings.MEDIA_ROOT,roomcode)
    # output_dir = 
    print(test_dir)
    # Loop over all the images in the test directory
    for count, image in enumerate(os.listdir(test_dir)):
    
        imagepath = os.path.join(test_dir, image)
        filename = imagepath.split(os.path.sep)[-1]

        # Load the image
        testimage = cv2.imread(imagepath)

        # Extract the position of bounding box of the face and their corresponding face encodings
        bboxes = face_recognition.face_locations(testimage, model='hog')
        encodings = face_recognition.face_encodings(testimage, bboxes)
        print(f"Image path: {imagepath}")
        # Check if any face is matched
        if any(face_recognition.compare_faces(data["encodings"], encoding)[0] for encoding in encodings): 
            print(imagepath)
            with open(imagepath,'rb') as img_file:
                match = Matches(code=code)
                match.pic.save(imagepath.split('/')[-1], img_file, save=True)
            
            
            
            
            
            
      
