import os
import requests

os.system("rm /home/coder/uoogou_yolov3_spp.jpg")
os.system("rm -rf /home/coder/yolov3/runs")

os.system("wget -O /home/coder/uoogou_yolov3_spp.jpg http://xiaomi-baota/xiaomi/uoogou.jpg")

os.system("python3 /home/coder/yolov3/detect.py --weights /home/coder/yolov3/yolov3-spp.pt --source /home/coder/uoogou_yolov3_spp.jpg")

file = open("/home/coder/yolov3/runs/detect/exp/uoogou_yolov3_spp.jpg", "rb")
response = requests.post("http://xiaomi-baota/xiaomi.php", files = {"file": file})
print(response.text)
file.close()

os.system("rm /home/coder/uoogou_yolov3_spp.jpg")
os.system("rm -rf /home/coder/yolov3/runs")




os.system("rm /home/coder/gionee_yolov5x.jpg")
os.system("rm -rf /home/coder/yolov5/runs")

os.system("wget -O /home/coder/gionee_yolov5x.jpg http://xiaomi-baota/xiaomi/gionee.jpg")

os.system("python3 /home/coder/yolov5/detect.py --weights /home/coder/yolov5/yolov5x.pt --source /home/coder/gionee_yolov5x.jpg")

file = open("/home/coder/yolov5/runs/detect/exp/gionee_yolov5x.jpg", "rb")
response = requests.post("http://xiaomi-baota/xiaomi.php", files = {"file": file})
print(response.text)
file.close()

os.system("rm /home/coder/gionee_yolov5x.jpg")
os.system("rm -rf /home/coder/yolov5/runs")


