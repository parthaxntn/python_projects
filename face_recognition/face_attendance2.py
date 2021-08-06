import datetime

import cv2
import numpy as np
import face_recognition
import os
# try:
a=1
while a==1:
    a=2
    path = 'image_input'
    images = []
    classNames = []
    mylst = os.listdir(path)

    for cl in mylst:
        # print(f"{path}/{cl}")
        curImg = cv2.imread(f"./{path}/{cl}")
        images.append(curImg)
        classNames.append(cl.split(".")[0])
        # print(curImg)
    # print(images)
    print(classNames)

    def findencodings(images):
        encodelist = []
        # i = 0
        for imgTest in images:
            imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
            print(len(face_recognition.face_encodings(imgTest)))
            encode = face_recognition.face_encodings(imgTest)[0]

            encodelist.append(encode)

        return encodelist

    def mark_attendence(name):
        with open('./attendence/attendence.txt',"r+t") as f:
            attendence = f.read()
            # print(attendence)
        with open('./attendence/attendence.txt','a') as g:
            attendence_list = str(attendence).split("\n")
            # print(attendence_list)
            attendence_name = [an.split(",")[0] for an in attendence_list]
            # print(attendence_name)
            for i in attendence_name:
                print(i)
                if name in i:
                    break
            else:
                g.write("\n"+name+"   "+","+datetime.datetime.now().strftime('%I:%M %p'))

    encodeListKnown = findencodings(images)
    # print(len(encodeListKnown))

    # cap = cv2.Sc(0)
    cap = cv2.VideoCapture(0)

    while True:
        success,img = cap.read()
        imgs = cv2.resize(img,(0,0),None,0.5,0.5)
        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

        facesCurFrms = face_recognition.face_locations(imgs)
        encodeCurFrame = face_recognition.face_encodings(imgs,facesCurFrms)


        for encodeFace,facelog in zip(encodeCurFrame,facesCurFrms):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            facedis = face_recognition.face_distance(encodeListKnown,encodeFace)
            matchIndex = np.argmin(facedis)

            if matches[matchIndex]:
                name = classNames[matchIndex].capitalize()

                #saving the frame
                if f'{name}.png' not in os.listdir(f'./attendence/face_recognised'):
                    cv2.imwrite(f'./attendence/face_recognised/{name}.png',imgs)

                y1,x2,y2,x1 = facelog
                y1, x1, y2, x2 = y1*2,x1*2,y2*2,x2*2
                cv2.rectangle(img, (x1 - 40,y1 - 100),(x2 + 40 ,y2 + 40 ), (4, 141, 100, 0.719),2)
                # cv2.rectangle(img,(x1 - 40,y2),(x2 + 40 ,y2 + 40),(4, 141, 100, 0.719),cv2.FILLED)
                # cv2.putText(img,f"{name} {round(1-(facedis[matchIndex]),4) * 100}%match",(x1-34,y2+34),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)
                mark_attendence(name)


        # print(img)
        cv2.imshow('webcam', img)
        cv2.waitKey(1)
        # cv2.rectangle(imgs, (facesCurFrms[3], facesCurFrms[0], facesCurFrms[1], facesCurFrms[2]), (255, 0, 255), 2)

    # cap
        # faceloc = face_recognition.face_locations(imgElon)[0]
        # encodeElon = face_recognition.face_encodings(imgElon)[0]
        # cv2.rectangle(imgElon, (faceloc[3], faceloc[0], faceloc[1], faceloc[2]), (255, 0, 255), 2)
        #
        # facelocTest = face_recognition.face_locations(imgTest)[0]
        # encodeTest = face_recognition.face_encodings(imgTest)[0]
        # cv2.rectangle(imgTest, (facelocTest[3], facelocTest[0], facelocTest[1], facelocTest[2]), (255, 0, 255), 2)
        #
        # results = face_recognition.compare_faces([encodeElon], encodeTest)
        # facedis = face_recognition.face_distance([encodeElon], encodeTest)


    # mylist = os.listdir("./image_input")
    #
    # for imgs in mylist:
    #     img = face_recognition.load_image_file(f"./images/{imgs}")


# except Exception as e:
#     print(e)
