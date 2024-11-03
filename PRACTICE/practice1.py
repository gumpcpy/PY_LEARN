'''
Author: gumpcpy gumpcpy@gmail.com
Date: 2024-11-03 13:42:31
LastEditors: gumpcpy gumpcpy@gmail.com
LastEditTime: 2024-11-03 16:25:19
Description: 
1-
把一張圖片放到excel裡面

2-
把圖片寬度固定在 350  圖片的長寬比維持原圖

3-
把一個指定folder裡面的png,jpg依照名稱順序 寫入excel B欄位裡
且A欄位為檔名

4-
一切和3一樣 但是含有圖片的路徑由使用者輸入
然後 excel 存到含有圖片的路徑下

'''
import os
from openpyxl import Workbook
from openpyxl.drawing.image import Image as xlImage
from PIL import Image
import shutil


def step1():

   return True


if __name__ == '__main__':
   step1()

