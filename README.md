# Person-detection
Utilize YOLOV5 to detect person
cd yolov5
  python detect.py --save-txt
  original pictures are saved in data/imgages, new pictures and labels are saved in runs/detect/exp#
 
 run cut.py to cut off 'person', make sure the pictures are saved in ./images and labels are saved in ./yolo_label, and the new pictures will be saved in ./new
