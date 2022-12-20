import face_recognition as fr

def process_frame(im):
    face_locations = fr.facelocations(im)