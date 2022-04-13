FROM wwkiyyx/vscode:root880510

EXPOSE 8080

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install libglib2.0-dev -y && \
    apt-get install libgl1-mesa-lgx -y && \
    apt-get install python3-pip -y && \
    git clone https://github.com/ultralytics/yolov3 && \
    git clone https://github.com/ultralytics/yolov5 && \
    pip install -r ./yolov3/requirements.txt
    
    