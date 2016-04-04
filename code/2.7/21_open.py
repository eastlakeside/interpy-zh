# coding=utf-8

# 错误写法
def open_file():
	f = open('photo.jpg', 'r+')
	jpgdata = f.read()
	f.close()


#正确写法
def open_file_right():
	with open('photo.jpg', 'r+') as f:
		jpgdata = f.read()

