# -*- coding: utf-8 -*-
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import sys
import cv2
import signal
import time

cap = cv2.VideoCapture(0)

number = 0

num = 0

while(True):
    # フレームをキャプチャする
    ret, frame = cap.read()

    # 画面に表示する
    cv2.imshow('frame',frame)

    # キーボード入力待ち
    key = cv2.waitKey(1) & 0xFF

    # qが押された場合は終了する
    if key == ord('q'):
        print("終了")
        break

    num += 1

    if num % 100 == 0:
        number += 1
        path = "image/photo" + str(number) + ".jpg"
        cv2.imwrite(path,frame)

        filename = "image/photo" + str(number) + ".jpg"
        model = VGG16(weights='imagenet')
        img = image.load_img(filename, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        preds = model.predict(preprocess_input(x))
        results = decode_predictions(preds, top=5)[0]
        if results[0][1] == "water_bottle":
            print("水！")

        print("=====================")
        for result in results:
            print(result)

    # sが押された場合は保存する
    if key == ord('s'):
        number += 1
        path = "image/photo" + str(number) + ".jpg"
        cv2.imwrite(path,frame)

        filename = "image/photo" + str(number) + ".jpg"
        model = VGG16(weights='imagenet')
        img = image.load_img(filename, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        preds = model.predict(preprocess_input(x))
        results = decode_predictions(preds, top=5)[0]
        if results[0][1] == "water_bottle":
            print("水！")

        print("=====================")
        for result in results:
            print(result)

# キャプチャの後始末と，ウィンドウをすべて消す
cap.release()
cv2.destroyAllWindows()
