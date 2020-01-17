#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyzbar.pyzbar import decode
import cv2

# 画像ファイルの指定
image = cv2.imread("multi-barcode4-sample.png")
# QRコードの読取り
data = decode(image)
# コード内容を出力
for symbol in data:
    #画像のこーどに枠を描画
    cv2.rectangle(image, (symbol.rect.left, symbol.rect.top), (symbol.rect.left + symbol.rect.width, symbol.rect.top + symbol.rect.height), (0,0,255), 4)
    for i in range(len(symbol.polygon)):
        if i != (len(symbol.polygon)-1):
            cv2.line(image, (symbol.polygon[i].x,symbol.polygon[i].y), (symbol.polygon[i+1].x,symbol.polygon[i+1].y), (255,0,0), 4)
        else:
            cv2.line(image, (symbol.polygon[i].x,symbol.polygon[i].y), (symbol.polygon[0].x,symbol.polygon[0].y), (255,0,0), 4)

    print("data:", symbol.data)
    print("type:", symbol.type)
    print("rect:", symbol.rect)
    print("polygon:", symbol.polygon)

cv2.imshow('barcode', image)
cv2.waitKey()