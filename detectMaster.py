import cv2
import face_recognition
masterImage = cv2.cvtColor(cv2.imread('C://my python programmin/ai_projects/jarvis/master.jpeg'), cv2.COLOR_BGR2RGB)
masterImageEncoding = face_recognition.face_encodings(masterImage)[0]
def detectMaster(frame, face):
    faceEncoding = face_recognition.face_encodings(face)
  
    if(len(faceEncoding) > 0):
        result = face_recognition.compare_faces(masterImageEncoding,  faceEncoding)
    else:
        result = []
    return result

# def main():
#     myImage = cv2.imread('C://my python programmin/ai_projects/jarvis/test.png')
#     frameImage = cv2.imread('C://my python programmin/ai_projects/jarvis/test2.png')
#     print(detectMaster(myImage, frameImage))


if __name__ == '__main__':
    pass
    # main()
    


