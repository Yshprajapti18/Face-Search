import os, sys
import cv2 
from imutils import paths
import pickle
import face_recognition


def get_encodings(datapaths,code):
    """
    Input: List of all image paths of your friends pictures
    This function loops over all the image paths, detects their face positions in the image, 
    constructs the face encodings and stores them and their corresponding names in a pickled file
    for further use.
    """
    print('this fuction was called')    
    friendsEncodings = []
    friendsNames = []

    # loop over all the images and extract the face encodings
    for count, imagepath in enumerate(datapaths):

        # get the friend's name from the image path
        name = imagepath.split(os.path.sep)[-2]

        # read the image and convert to RGB scale
        image = cv2.imread(imagepath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # get the bounding box location of the face using HOG (Histogram of Oriented Gradients)
        Bboxes = face_recognition.face_locations(image, model='hog')

        # construct the encoding of the face within the bounding box
        encodings = face_recognition.face_encodings(image, Bboxes)

        # store the face encoding and their respective name to the lists of encodings and names respectively,
        for encoding in encodings:

            friendsEncodings.append(encoding)
            friendsNames.append(name)
        
        
    # make a dictionary that stores all the encodings and their corresponding names
    data = {"encodings": friendsEncodings,
             "names": friendsNames}

    # save the dictionary locally in a pickle file to be used later for the recognition part
    with open(f'{code}.pickle', "wb") as fe:
        fe.write(pickle.dumps(data))
        
    return data

