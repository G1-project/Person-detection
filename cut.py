import cv2
import os
from PIL import Image
def cut_one_image(img_path, txt_path, path):
    def read_list(txt_path):
        pos = []
        with open(txt_path, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                    pass
                # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
                p_tmp = [float(i) for i in lines.split(' ')]
                pos.append(p_tmp)  # 添加新读取的数据
                pass
        return pos

    # txt转换为box
    def convert(size, box):
        xmin = (box[1] - box[3] / 2.) * size[1]
        xmax = (box[1] + box[3] / 2.) * size[1]
        ymin = (box[2] - box[4] / 2.) * size[0]
        ymax = (box[2] + box[4] / 2.) * size[0]
        box = (int(xmin), int(ymin), int(xmax), int(ymax))
        return box
    image = cv2.imread(img_path)
    global ans
    ans = image
    pos = read_list(txt_path)
    global img
    for i in range(len(pos)):
        box = convert(image.shape, pos[i])
        image = cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 1)
        save_path = path + '_' + str(i) + '.jpg'
        #print(save_path)
        for j in range(box[1], box[3]+1):
            for k in range(box[0], box[2]+1):
                ans[j, k] = (255, 255, 255)
        cv2.imwrite('temp.png', ans)
        img = Image.open("temp.png")
        img = img.convert("RGBA")  # 转换格式，确保像素包含alpha通道
        width, height = img.size  # 长度和宽度
        for i in range(0, width):  # 遍历所有长度的点
            for j in range(0, height):  # 遍历所有宽度的点
                data = img.getpixel((i, j))  # 获取一个像素+
                if (data.count(255) == 4):
                    img.putpixel((i, j), (255, 255, 255, 0))
    img.save("new/"+path+".png")

def choose_one(img_folder, label_folder, i):
    img_list = os.listdir(img_folder)
    img_list.sort()
    label_list = os.listdir(label_folder)
    label_list.sort()
    img_path = img_folder + "/" + img_list[i]
    path1 = img_path.split(".")[0].split("/")[1]
    txt_path = label_folder + "/" + label_list[i]
    cut_one_image(img_path=img_path, txt_path=txt_path, path=path1)

def main():
    i = 0
    for file in os.listdir('./images'): i += 1
    Exception = []
    for j in range(i):
        try:
            choose_one(img_folder="images", label_folder="yolo_label", i=j)
            print(str(j)+'/'+str(i-1))
        except:
            choose_one(img_folder="images", label_folder="yolo_label", i=j)
            print(str(j) + '/' + str(i - 1))
            Exception.append(j)

    f = open("exception.txt", "w")
    for line in Exception:
        f.write(str(line) + '\n')
    f.close()
if __name__ == '__main__':
    main()

