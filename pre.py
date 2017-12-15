from utils import get_meta
import cv2
import os

full_path, dob, gender, photo_taken, face_score, second_face_score, age = get_meta("imdb_crop/imdb.mat", "imdb")



# preprocess for gender classification 

def preprocess_for_gen():
    print str(full_path.shape[0]) + " images found"

    countf = 0
    countm = 0
    countnan = 0

    for i in range(full_path.shape[0]):
        head,tail = os.path.split(full_path[i][0])

        if gender[i] == 0.0 and countf <=5000:
            newtail = "FF/"+tail
            _path = "imdb_crop/"+str(full_path[i][0])
            t = cv2.imread(_path)
            tru = cv2.imwrite(newtail,t)                                                                                                                                                                           
            if tru:
                countf += 1

        elif gender[i] == 1.0 and countm <=5000:
            newtail = "MM/"+tail
            _path = "imdb_crop/"+str(full_path[i][0])
            t = cv2.imread(_path)
            tru = cv2.imwrite(newtail,t)                                                                                                                                                                           
            if tru:
                countm += 1
            
        else:
            countnan += 1


    print countf,countm,countnan


# preprocess for age classification data based on classes below
# "0-10", "10-20","20-30", "30-40", "40-55", "55-65", "65-90"


def preprocess_for_age():
    print str(full_path.shape[0]) + " images found"

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    countnan = 0

    for i in range(full_path.shape[0]):
        head,tail = os.path.split(full_path[i][0])

        if  0 < age[i] <= 10:
            newtail = "1/"+tail
            _path = "imdb_crop/"+str(full_path[i][0])
            t = cv2.imread(_path)
            tru = cv2.imwrite(newtail,t)                                                                                                                                                                           
            if tru:
                count1 += 1
        elif  10 < age[i] <= 20:
            newtail = "2/"+tail
            _path = "imdb_crop/"+str(full_path[i][0])
            t = cv2.imread(_path)
            tru = cv2.imwrite(newtail,t)                                                                                                                                                                           
            if tru:
                count2 += 1
        elif  20 < age[i] <= 30:
            newtail = "3/"+tail
            _path = "imdb_crop/"+str(full_path[i][0])
            t = cv2.imread(_path)
            tru = cv2.imwrite(newtail,t)                                                                                                                                                                           
            if tru:
                count3 += 1

        elif  30 < age[i] <= 40:
            newtail = "4/"+tail
            _path = "imdb_crop/"+str(full_path[i][0])
            t = cv2.imread(_path)
            tru = cv2.imwrite(newtail,t)                                                                                                                                                                           
            if tru:
                count4 += 1
        elif  40 < age[i] <= 55:
            newtail = "5/"+tail
            _path = "imdb_crop/"+str(full_path[i][0])
            t = cv2.imread(_path)
            tru = cv2.imwrite(newtail,t)                                                                                                                                                                           
            if tru:
                count5 += 1
        elif  55 < age[i] <= 65:
            newtail = "6/"+tail
            _path = "imdb_crop/"+str(full_path[i][0])
            t = cv2.imread(_path)
            tru = cv2.imwrite(newtail,t)                                                                                                                                                                           
            if tru:
                count6 += 1
        elif  65 < age[i] <= 90:
            newtail = "7/"+tail
            _path = "imdb_crop/"+str(full_path[i][0])
            t = cv2.imread(_path)
            tru = cv2.imwrite(newtail,t)                                                                                                                                                                           
            if tru:
                count7 += 1
        else :
            countnan += 1


        


    print count1,count2,count3,count4,count5,count6,count7,countnan



def convert_graysale(f):
    '''
    :param f: file name
    :return: returns the grayscaled and scaled version of the image
    '''
    image = cv2.imread(f)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (100, 100))
    cv2.imwrite(f, resized_image)
    # return resized_image


def grayscale_resize_save(file_name):
    '''
    :param f: file path
    :return: grayscales all images in the directory
    '''
    count = 0
    for cur, _dirs, files in os.walk(file_name):
        head, tail = os.path.split(cur)
        while head:
            head, _tail = os.path.split(head)

        for f in files:
            if ".jpg" in f:
                path = "MM" + tail + "/" + f
                convert_graysale(path)
                print count, "converted ", path
                count += 1



def facecrop(image):
    facedata = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)
    print type(img)
    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

        sub_face = img[y:y+h, x:x+w]
        fname, ext = os.path.splitext(image)
        cv2.imwrite(image, sub_face)

    return 

def facecrop_save(file_name):
    '''
    :param f: file path
    :return: grayscales all images in the directory
    '''
    count = 0
    for cur, _dirs, files in os.walk(file_name):
        head, tail = os.path.split(cur)
        while head:
            head, _tail = os.path.split(head)

        for f in files:
            if ".jpg" in f:
                path = "MM" + tail + "/" + f
                facecrop(path)
                print count, "converted ", path
                count += 1


    return
# preprocess_for_age ()
# preprocess_for_gen()
# grayscale_resize_save("MM/")
facecrop_save("MM/")