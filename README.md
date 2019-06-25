# license_plate_recognition
In this project we will detect license plate of vehicles and display the number to the terminal.

## Steps to follow:

step 1 : Install following packages:
            numpy
            opencv
            matplotlib
            tesseract
            
step 2 : Run plate_detection.py by passing image name 
 Ex:- python pate_detection.py car.jpg

step 3 : check your current working directory which will contain the detected image.

step 4 : Now recognition of numbers on plate have to be done, for this we will use tesseract-ocr.
         Ex:- tesseract img_5.jpg output
        This will detect the text of img_5 and write it to output.txt.
        
        
        
 ![car image](https://upload.wikimedia.org/wikipedia/commons/b/bd/Singapore_1990_vehicle_registration_plate_of_a_silver_Ford_Focus.jpg)


![detected image](https://user-images.githubusercontent.com/38654965/60074704-27eca780-9741-11e9-9fa9-4b6266bbd51e.png)


![outuput.txt](https://user-images.githubusercontent.com/38654965/60074810-713cf700-9741-11e9-938e-ff52572a6db4.png)
