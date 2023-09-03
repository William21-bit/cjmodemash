from django.shortcuts import render
import random
from .models import Photo

source =list(Photo.objects.values('img'))
photos= [item['img'] for item in source]
Random_store=[]
length =int(len(photos))


def Random_image():
    global photos,Random_store
    while True:
        image1 = random.choice(photos)
        if image1 not in Random_store:
            Random_store.append(image1)
            break
        else:
            continue
    while True:
        image2 = random.choice(photos)
        if image2 not in Random_store:
            Random_store.append(image2)
            break
        else:
            continue
    return image1,image2

def index(request):
    global Random_store
    Random_store.clear()
    img1,img2 = Random_image()
    data ={'img1':img1, 'img2':img2}
    return render(request,'index.html',data)


def check(request):
    global Random_store, length
    if length == int(len(Random_store)):
        return render(request,'lastpage.html')
    else:
        img1, img2 = Random_image()
        data = {'img1': img1, 'img2': img2}
        return render(request,'index.html',data)