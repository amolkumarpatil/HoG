import cv2
import imutils
import argparse

def pedestrian_detection(image):
    hog = cv2.HOGDescriptor() 
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 
    
    #Reading the image
    image = cv2.imread(image)

    # Resizing the Image 
    image = imutils.resize(image, 
                       width=min(400, image.shape[1])) 
   
    # Detecting all the regions in the  
    # Image that has a pedestrians inside it 
    (regions, _) = hog.detectMultiScale(image,  
                                    winStride=(4, 4), 
                                    padding=(4, 4), 
                                    scale=1.05)

    for (x, y, w, h) in regions: 
        cv2.rectangle(image, (x, y),  
                  (x + w, y + h),  
                  (0, 0, 255), 2) 
    cv2.imshow("Image", image) 
    cv2.waitKey(0) 
   
    cv2.destroyAllWindows()
    return regions


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", required=True,
	help="path to the input image")
    args = vars(parser.parse_args())
    pedestrian_detection(args["image"])