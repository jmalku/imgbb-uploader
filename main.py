import base64
import requests
import random

image = 'sample_image.jpg'
api_imgbb = 'YOUR_API_KEY'

with open(image, "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": api_imgbb,
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)
    dict = res.json()
    imge = dict['data']['url']
    print("The URL of your image is: ", imge)
