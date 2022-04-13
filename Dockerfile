FROM ultralytics/yolov3:latest

EXPOSE 8080

RUN curl -fsSL https://code-server.dev/install.sh | sh -s

CMD ["code-server --port 8080 --host 0.0.0.0 --auth none"]
    