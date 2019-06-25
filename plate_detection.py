import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

    
if __name__=='__main__':
    if len(sys.argv) > 1:
        parsed=sys.argv[1]
    else:
        print("No arguments passed.")

    img = cv2.imread(parsed)
    print(img.shape)
    
    img=cv2.resize(img,(640,480))
    cv2.imshow('image',img)
    print(img.shape)
    
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(img_grey,100,200)

    cv2.imshow('canny',edges)

    # Find contours for image, which will detect all the boxes
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    idx=0
    for c in contours:
        # Returns the location and width,height for every contour
        x, y, w, h = cv2.boundingRect(c)
        if (h > 10)and w > 3*h:
            idx += 1
            new_img = img[y:y+h, x:x+w]
            if(new_img.shape[0]<100)or(new_img.shape[1]<100):
                
                new_img=cv2.resize(new_img,(800,100))
            
            image=cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
            
            imgBlur = cv2.GaussianBlur(image, (9, 9), 0)
            
            plt.imshow(imgBlur,cmap='gray')
            cv2.imwrite("img_"+str(idx)+".jpg",imgBlur)
            plt.show()       
    cv2.waitKey(0)
        
