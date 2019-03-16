from MyQR import myqr
import os

# words = 'https://goss4.vcg.com/creative/vcg/800/version23/VCG21gic16374358.jpg'
# words = 'https://pan.baidu.com/play/video#/video?path=%2F%E7%94%B5%E5%BD%B1%2FCoursera-%E5%90%95%E4%B8%96%E6%B5%A9-%E7%A7%A6%E5%A7%8B%E7%9A%87%2FWeek%201%2F3%20-%201%20-%201-1%20%E9%96%8B%E5%AE%97%E6%98%8E%E7%BE%A9%20(09-13).mp4&t=-1'
words = 'https://music.163.com/#/program?id=2058535948'

version, level, qr_name = myqr.run(
    words,
    version=1,
    level='H',
    picture='wife.jpg',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=None,
    save_dir=os.getcwd()
)

'''
# help(myqr)
Positional parameter
   words: str
   在命令后输入连接或者句子作为参数，然后在程序的当前目录中产生相应的二维码图片文件，默认名就是'qrcode.png'

Optional parameters
   version: int, from 1 to 40
   默认边长是取决于你输入的信息的长度和使用的纠错等级

   level: str, just one of ('L','M','Q','H')
   默认的纠错等级最高的是H

   控制边长，范围是1-40，数字越大边长越大
   控制纠错水平，范围是L,M,Q,H，从左到右一次升高

   picutre: str, a filename of a image
   用来将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片

   colorized: bool
   可以使产生的图片由黑白变成彩色的

   constrast: float
   可以调节图片的对比度，1表示原始图片，更小的值表示更低对比度，更大反之

   brightness: float
   用来调节图片的亮度

   save_name: str, the output filename like 'example.png'
   默认输出图片qrcode.png

   save_dir: str, the output directory
   自定义输出目录
'''
