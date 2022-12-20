

# import the opencv library
import cv2  
# define a video capture object
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = cam.read()
    if not ret:
        print("fail to grab frame")
        break
    
    # Display the resulting frame
    cv2.imshow('test', frame)

    k = cv2.waitKey(0)
    if k % 256 == 27:
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("{} written!".format(img_name))
        img_counter += 1 
  
# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()