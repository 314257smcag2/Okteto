FROM ultralytics/yolov3:latest

EXPOSE 8080

RUN curl -fsSL https://code-server.dev/install.sh | sh -s -- --dry-run 


    