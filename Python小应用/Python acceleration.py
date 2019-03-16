import cv2
import time
import glob

'''
首先需要从处理内容的文件列表开始
使用 for 循环逐个处理每个数据，然后在每个循环迭代上运行预处理
'''
# loop through all jpg file in the current folder
# resize each one to size 600*600
start_time = time.time()
for image_filename in glob.glob('./Airport/*.jpg'):
    img = cv2.imread(image_filename)

    # resize the image
    img = cv2.resize(img, (600, 600))
print('time:', time.time() - start_time)
# 2.667  360 jpgs

'''
将 jpg 文件列表分成4个小组
运行 python 解释器中的 4 个独立的实例
让 python 的每个实例处理 4 个数据小组中一个
结合 4 个处理过程得到的结构得出最终那那个结果列表
'''
import concurrent.futures

start_time1 = time.time()


def load_and_resize(image_filename):
    img = cv2.imread(image_filename)
    img = cv2.resize(img, (600, 600))


# create a pool of processes. By default,one is created for each cpu in your machine
with concurrent.futures.ProcessPoolExecutor() as executor:
    # get a list of files to process
    image_files = glob.glob('*.jpg')

    # executor.map() 将你想要运行的函数和列表作为输入，列表中的每个元素都是我们函数的单个输入，由于我们有6个核，我们将同时处理该列表中的6个项目
    executor.map(load_and_resize, image_files)

print('acceleration time:', time.time() - start_time1)
# 0.139