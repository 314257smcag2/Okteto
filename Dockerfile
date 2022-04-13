FROM wwkiyyx/vscode:root880510

EXPOSE 8080

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install libglib2.0-dev -y
RUN apt-get install libgl1-mesa-lgx -y
RUN apt-get install python3-pip -y 
RUN git clone https://github.com/ultralytics/yolov3
RUN git clone https://github.com/ultralytics/yolov5
RUN pip install -r ./yolov3/requirements.txt
    
    