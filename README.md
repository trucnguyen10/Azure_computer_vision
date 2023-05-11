**To run the program in your computer using the terminal:** <br />
              + cd azureproject<br />
              + myenv\Scripts\activate <br />
              + python main.py <br />

**A description of what the code does:** <br />
1. The code imports necessary modules from Azure Cognitive Services, array, os, PIL, and sys. <br />
2. The subscription key and endpoint are defined for the Computer Vision API. <br />
3. The code specifies the input and output folders where the images to be processed are stored and where the output images will be saved. <br />
4. The code lists all the files in the input folder and loops through each file to perform object detection, image description, and color analysis using the Computer Vision API. <br />
5. For each image file, the code opens the image file and creates an ImageDraw object to draw bounding boxes around detected objects. <br />
6. The code then calls the detect_objects_in_stream method of the Computer Vision API to detect objects in the image and draws a bounding box around each detected object using ImageDraw.rectangle method. <br />
7. The code also writes the name of the detected object and its confidence score inside the bounding box using ImageDraw.text method. <br />
8. The processed image is then saved in the output folder with the same filename. <br />
9. The code then calls describe_image_in_stream method of the Computer Vision API to generate a description of the image, including the main subject and any relevant information about the scene. <br />
10. The code then calls analyze_image_in_stream method of the Computer Vision API to analyze the colors in the image and prints the dominant foreground color, dominant background color, and accent color. <br />
11. Overall, the code uses the Computer Vision API to perform object detection, image description, and color analysis on a set of input images, and saves the processed images in the output folder. <br />

![terinal](https://github.com/trucnguyen10/Azure_computer_vision/assets/87359204/104ebe42-11ca-4272-8d92-eb3f6062760d)

![coachella](https://github.com/trucnguyen10/Azure_computer_vision/assets/87359204/cbadc251-4000-4fe3-892b-bb9a29d3d054)
![coachella](https://github.com/trucnguyen10/Azure_computer_vision/assets/87359204/048a1c10-04d0-4ed8-9bc5-6dcb5280a9c3)

![timesquare](https://github.com/trucnguyen10/Azure_computer_vision/assets/87359204/5a6bc9c4-be8e-4271-99f1-e36142fd7f33)
![timesquare](https://github.com/trucnguyen10/Azure_computer_vision/assets/87359204/c68fa8b3-f051-46de-aee1-7771f2537f91)

![football](https://github.com/trucnguyen10/Azure_computer_vision/assets/87359204/ca2f5e18-a9ff-4ba7-b25a-1ac0b2d454f5)
![football](https://github.com/trucnguyen10/Azure_computer_vision/assets/87359204/4e2ceae9-884c-4f75-aa3f-9dc4bf0e83fc)
