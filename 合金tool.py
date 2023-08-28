import os
import keyboard


#读取文件
bef = open('forge.cfg', 'r')
trueforge = bef.read()

print(trueforge)


def insides():
    directory = r'C:\MCLDownload\Game\.minecraft\config'
    filename = 'forge.cfg'
    file_path = os.path.join(directory, filename)

    if os.path.exists(file_path):
        return "文件存在"
    else:
        return "文件不存在"
print("按下s启动")
keyboard.wait('s')
print('start')
with open(r'C:\MCLDownload\Game\.minecraft\config\测试.txt', 'w') as f:
    f.write('这是一个测试文件')
while True:
    ff = insides()
    if ff == "文件不存在":
        break
        print("检测到启动器做出改动。")

time.sleep(0.1)
app = open(r'C:\MCLDownload\Game\.minecraft\config\forge.cfg', 'w')
app.write(trueforge)
app.close()
print('开启多线程执行完毕')


#检查
with open(r'C:\MCLDownload\Game\.minecraft\config\forge.cfg') as ff:
    exe = ff.read()
if trueforge == exe:
    print("开启多线程优化成功！")
    print("s键退出")
    Keyboard.wait("s")
else:
    print('失败！')
    print("s键退出")
    Keyboard.wait("s")







