from cProfile import run
import sys
import time
import cv2
import myjarvis
sys.path.insert(1, 'C://my python programmin/ai_projects/jarvis')
import detectMaster
from threading import Timer


def main():
    myVideo = cv2.VideoCapture(0)
    myVideo.set(3, 640)
    myVideo.set(4, 480)
    faces = []
  

    face_detector_file =  cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    master_detected = False
    eTime = time.time()+5
    cTime = time.time()
    print('Recognizing user...')
    while True:
        successful_frame_read, frame = myVideo.read()
        # print(frame)
        if int(cTime) >= eTime:
            break
        frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector_file.detectMultiScale(frame_grayscale, scaleFactor=1.1, minNeighbors=4)
        
        for (x, y, w, h) in faces:  
            faceCrop = frame[y:y+h, x:x+w]
            faceCrop = cv2.cvtColor(faceCrop, cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if  master_detected == False:
                result = detectMaster.detectMaster(frame, faceCrop)
              
                if result.count(True) > 0:
                    # cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 255, 0), 2)

                    cv2.imwrite('filename.png', faceCrop)
        
                    master_detected = True
                    # break
                else:
                    cv2.imwrite('filename.png', faceCrop)
                    master_detected = False


            # detect smile in the face area
            if len(faces) == 0:
                master_detected = False
        
                cv2.destroyAllWindows()    
                break
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 255, 0), 2)
        
        if master_detected == True:
            break
        
        cTime = time.time() 
    print('Detection complete.'+'\n Result: ', master_detected)
       
    return master_detected  
 
        
        

if __name__ == '__main__':
    main()
    


    