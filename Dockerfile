FROM ultralytics/yolov3:latest

EXPOSE 8080

RUN wget https://github.com/coder/code-server/releases/download/v4.1.0/code-server-4.1.0-linux-amd64.tar.gz \
    && tar xf code-server-4.1.0-linux-amd64.tar.gz \
    && cd code-server-4.1.0-linux-amd64 \
    && ./code-server --port 8080 --host 0.0.0.0 --auth None 
    