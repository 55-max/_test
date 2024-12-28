#%%

# import
import cv2
import glob

# 画像を読み込む
img_path_wild_card = './*.jpg'
img_path_list = glob.glob(img_path_wild_card)
img_path = img_path_list[0]

output_path = './resized.png'
resize_size = (2100, 2100)

class Resize_img:
    def __init__(self, img_path, output_path, resize_size):
        self.img_path = img_path
        self.output_path = output_path
        self.resize_size = resize_size

    def resize(self):
        img = cv2.imread(self.img_path)
        print(self.resize_size)
        img_resized = cv2.resize(img, self.resize_size)
        cv2.imwrite(self.output_path, img_resized)

def main():
    resize_img = Resize_img(img_path, output_path, resize_size)
    resize_img.resize()

if __name__ == '__main__':
    main()

#%%