comport='/dev/tty.Bluetooth-Incoming-Port'

import cv2 as cv
import argparse
import sys
import numpy as np
import os.path
import serial                                                              
import time   
ArduinoUnoSerial = serial.Serial(comport,9600) 

ArduinoUnoSerial.close()

confThreshold = 0.9
nmsThreshold = 0.2   
inpWidth = 416       
inpHeight = 416      
file=input("Enter input file(ex:1.jpg)")
print(file)

classesFile = "coco.names"
classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')



modelConfiguration = "yolov3.cfg"
modelWeights = "yolov3.weights"
# yolo object detector trained on coco names
net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)


net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
#print('Using CPU device.')


def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i - 1] for i in net.getUnconnectedOutLayers()]

def drawPred(classId, conf, left, top, right, bottom):
    # Draw a bounding box.
    cv.rectangle(frame, (left, top), (right, bottom), (np.random.randint(255), np.random.randint(255), np.random.randint(255)), 2)
    
    label = '%.2f' % conf
        

    if classes:
        assert(classId < len(classes))
        label = '%s : %s' % (classes[classId], label)


    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])
    cv.rectangle(frame, (left, top - round(1.5*labelSize[1])), (left + round(1.5*labelSize[0]), top + baseLine), (255, 255, 255), cv.FILLED)
    cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 1)

def postprocess(frame, outs):
    frameHeight = frame.shape[0] 
    frameWidth = frame.shape[1]


    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])
                if(classId==20):
                    print(classId)
                    ArduinoUnoSerial = serial.Serial(comport,9600) 
                    var='*1'
                    for i in range(2):
                        ArduinoUnoSerial.write(var.encode())                      #send 1 to the arduino's Data code       
                          
                        time.sleep(2)               
                    print("DONE...")
                    ArduinoUnoSerial.close()
                        


    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        #i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        drawPred(classIds[i], confidences[i], left, top, left + width, top + height)
        
        



winName = 'RESULT OF ANIMAL DETECTION'
cv.namedWindow(winName, cv.WINDOW_NORMAL)


cap = cv.VideoCapture(file)
outputFile = file[:-4]+'_out.jpg'



while cv.waitKey(1) < 0:
    
    hasFrame, frame = cap.read()
    
    if not hasFrame:
        print("Done processing !!!")
        print("Output file is stored as ", outputFile)
        cv.waitKey(3000)
        # Release device
        cap.release()
        break

    # Create a 4D blob from a frame.
    blob = cv.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)

 
    net.setInput(blob)

    outs = net.forward(getOutputsNames(net))
  

    postprocess(frame, outs)

    
    t, _ = net.getPerfProfile()
    label = 'Inference time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
    cv.putText(frame, label, (100, 400), cv.FONT_HERSHEY_SIMPLEX, 1, (25, 10, 120))
    #cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 1)

  
    cv.imwrite(outputFile, frame.astype(np.uint8))
    

    cv.imshow(winName, frame)
    cv.waitKey(0)
cv.destroyAllWindows()

