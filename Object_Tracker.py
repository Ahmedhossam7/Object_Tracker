#Import open cvs library 
import cv2

def main():
    vid=cv2.VideoCapture(0) #0 is the laptops webcam
    
    #Read the first frame to then select ROI
    ret, frame=vid.read()
    #check  return of .read 
    if not ret:
        print("Error:Couldnt read first frame.")
        return
    #Selecting Region of Interest 
    print("Choose object to track using Mouse and press Enter")
    #return the boundix box for the region of interest
    bounding_box=cv2.selectROI("Select Object",frame,showCrosshair=True,fromCenter=False)
    cv2.destroyWindow("Select Object")
    
    object_tracker=cv2.TrackerCSRT.create()
    object_tracker.init(frame,bounding_box)
    
    #Tracking Process
    while True:
        #keep returning frames from webcam
        ret,frame2=vid.read()
        
        #check if camera no longer returns
        if not ret:
            break #break from loop
        
        #update tracker using new frame
        success,box=object_tracker.update(frame2)
        
        if success:
            # Draw bounding box
            x, y, w, h = map(int,box)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame2, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            # Tracking failure
            cv2.putText(frame2, "Lost Track - Press A to reselect object", (20, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
        cv2.imshow("Object Tracker",frame2)

        #Exit if ESC is pressed        
        key=cv2.waitKey(1)
        if key==27:
            break
        elif key==ord('a') and not success: #reselect object if lost track and a pressed
            #Repeat the selection process again
            print("Choose object to track using Mouse and press Enter")
            ret,frame3=vid.read()
            if ret:
                new_bounding_box=cv2.selectROI("Reselect Object",frame3,showCrosshair=True,fromCenter=False)
                #close the window where you select the bounding box
                cv2.destroyWindow("Reselect Object")
                #Create the tracker 
                object_tracker=cv2.TrackerCSRT.create()
                object_tracker.init(frame3,new_bounding_box)
            
    vid.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
        