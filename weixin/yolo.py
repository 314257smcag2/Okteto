import os
import requests

while True:
    os.system("rm /home/coder/image_yolov3_spp.jpg")
    os.system("rm -rf /home/coder/yolov3/runs/detect/exp4")

    os.system("wget -O /home/coder/image_yolov3_spp.jpg http://xiaomi-baota/xiaomi/image.jpg")

    os.system("python3 /home/coder/yolov3/detect.py --weights /home/coder/yolov3/yolov3-spp.pt --source /home/coder/image_yolov3_spp.jpg")

    file = open("/home/coder/yolov3/runs/detect/exp4/image_yolov3_spp.jpg", "rb")
    response = requests.post("http://xiaomi-baota/xiaomi.php", files = {"file": file})
    print(response.text)
    file.close()

    os.system("rm /home/coder/image_yolov3_spp.jpg")
    os.system("rm -rf /home/coder/yolov3/runs/detect/exp4")




    os.system("rm /home/coder/image_yolov5x.jpg")
    os.system("rm -rf /home/coder/yolov5/runs/detect/exp6")

    os.system("wget -O /home/coder/image_yolov5x.jpg http://xiaomi-baota/xiaomi/image.jpg")

    os.system("python3 /home/coder/yolov5/detect.py --weights /home/coder/yolov5/yolov5x.pt --source /home/coder/image_yolov5x.jpg")

    file = open("/home/coder/yolov5/runs/detect/exp6/image_yolov5x.jpg", "rb")
    response = requests.post("http://xiaomi-baota/xiaomi.php", files = {"file": file})
    print(response.text)
    file.close()

    os.system("rm /home/coder/image_yolov5x.jpg")
    os.system("rm -rf /home/coder/yolov5/runs/detect/exp6")



