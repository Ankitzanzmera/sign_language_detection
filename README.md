## Sign Language Detection Using YOLOv5

## Steps

## Data Collection :  
    python capture.py

## Data Annotation :
    For Data Annotation You use lblimg.exe which is in annotation_tool folder or you can use Roboflow for faster Annotation

## Clone yolov5 repository:
    !git clone https://github.com/ultralytics/yolov5.git

## Install Dependencies
    %cd yolov5
    pip install -r requirements.txt

## Update yolov5/models/custom_yolov5s.yaml
    For reference you can see sign_language_detection.ipynb

## Training
    %cd yolov5
    !python train.py --img 416 --batch 16 --epochs 300 --data <input_path> --cfg "/content/yolov5/models/custom_yolov5s.yaml" --weights "yolov5s.pt" --name yolov5_results --cache 

Since i used google colab to train model so write command as shown above.

## Evaluation
    ![Evaluation](assets/image.png)

## for inference 
    %cd yolov5
    !python detect.py --weights <input_path> --img 416 --conf 0.1 --source <output_path>

## To show real time prediction through Camera run following command in Terminal
    %cd yolov5
    python run.py