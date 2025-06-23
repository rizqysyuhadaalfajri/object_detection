# Object Detection Using Camera

_Rizqy Syuhada Alfajri
(2155301134)_

# Background
Along with the rapid development of digital technology, the need for visual-based automation systems is increasing, especially in the fields of surveillance, security, industry, and transportation. One solution that is widely used to support visual automation is a real-time object detection system, which allows computers to recognize and track objects directly through the camera.
Object detection is part of the field of Computer Vision that utilizes artificial intelligence (AI) algorithms to identify certain objects in images or videos. One of the well-known and widely used algorithms is YOLO (You Only Look Once). The latest version of this algorithm, YOLOv8, offers better speed and accuracy, as well as ease of integration in the development of Python-based detection systems.
This project aims to build a real-time object detection application using YOLOv8 and OpenCV. This application will display the detection results from the camera directly with a simple but informative interface, including the name of the detected object and the level of confidence of the detection. With this approach, the system can be used as a basis for developing various applications such as monitoring systems, smart surveillance, and automatic detection in industrial environments.

# Models Used:
This camera object detection project uses the YOLOv8 (You Only Look Once version 8) model, specifically the lightweight version, yolov8n.pt (YOLOv8 Nano). This model is a pre-trained model made by Ultralytics that is very lightweight and fast, suitable for use in real-time systems even when run on devices with limited specifications such as ordinary laptops or Raspberry Pi. 
This model has been trained using the COCO dataset (Common Objects in Context), which is one of the most popular datasets in the field of computer vision. COCO contains more than 118,000 images with 80 categories of objects commonly found in everyday life, such as humans, vehicles (cars, bicycles, trucks), animals (dogs, cats, cows), household objects (chairs, tables, televisions, laptops), and many more.

# Formulation of the problem
1. How to build an object detection system that can work in real-time using a camera?
2. How to display detection information (object name and confidence) directly on the screen with a simple and easy-to-understand interface?
3. How to integrate a pre-trained YOLOv8 detection model with an OpenCV-based visualization system?

# Purppose
1. Building a real-time object detection application using the YOLOv8 model and a laptop camera.
2. Displaying detection results in the form of bounding boxes, object labels, and confidence levels directly on the video display.
3. Increasing practical understanding in the application of computer vision and the use of pre-trained AI-based models.

# Scope
1. The system only uses the internal camera (webcam) of the laptop device.
2. The model used is YOLOv8 pre-trained on the COCO dataset, without retraining.
3. The system will display object detection directly (real-time) with a simple interface in the form of labels and confidence.
4. The project is focused on technical demos or prototypes, not for direct industrial production or deployment.
  
# Source
1. Model   : Yolo V8 (You Only Look Once)
2. Dataset : COCO

# Dokumentation 
![image](https://github.com/user-attachments/assets/88efaa24-1a1b-4110-8247-292082178cd1)
