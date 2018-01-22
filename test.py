# -*- coding: utf-8 -*-
import numpy as np
import cv2
import signal
import time

cap = cv2.VideoCapture(0)

number = 0

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

    # sが押された場合は保存する
    if key == ord('s'):
        print("撮影！")
        number += 1
        path = "image/photo" + str(number) + ".jpg"
        print(number)
        cv2.imwrite(path,frame)

# キャプチャの後始末と，ウィンドウをすべて消す
cap.release()
cv2.destroyAllWindows()
