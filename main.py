# # 这是一个示例 Python 脚本。
#
# # 按 Shift+F10 执行或将其替换为您的代码。
# # 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#
#
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5]#创建等差数列 0-2之间100个
# y = []
# u = []
# for i in x:
#     a = i*i
#     b = i*i*i
#     y.append(a)
#     u.append(b)
# print(y)
# plt.plot(x, x, label="c")#第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
# plt.plot(x, y, label="b")
# plt.plot(x, u, label="a")
#
# plt.xlabel("x label")#x轴名字
# plt.ylabel("y label")#y轴名字
#
# plt.title("测试折线图")#图标名字
#
# plt.legend()#显示图例
#
# plt.show()#生成图表

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10,6)
# 设置绘制图像显示比例
# varepsilon_values_1 = np.random.randn(200)
# a = np.random.randn(50)*2
# type(varepsilon_values_1)
# print(type(varepsilon_values_1))
# # 随机生成100个服从标准正太分布的点
# plt.plot(b)
# plt.show()
# # 绘制图像
t = 1000
varepsilon_values_2 = []
x = []
def burn(e,f,n):
    d = (e + 1) * n
    xt = (f - 1) * n
    # print(d)
    varepsilon_values_2.append(d)
    varepsilon_values_2.append(xt)
def shade(e,f,n):
    d = e * n
    xt = f * n
    # print(d)
    varepsilon_values_2.append(d)
    varepsilon_values_2.append(xt)



for i in range(t):
    x.append(i)
    e = np.random.randn()
    f=-e
    n=10
    if (i>50 and i<80):
        burn(e,f,10)

    if (i>80 and i<100):
        burn(e,f,5)

    if (i>100 and i<120):
        burn(e,f,3)

    if (i>120 and i<130):
        burn(e,f,2)

    if (i>450 and i<500):
       burn(e,f,6)

    if (i>550 and i<575):
        burn(e,f,3)

    if (i>640 and i<670):
        burn(e,f,6)

    if (i>850 and i<880):
        burn(e,f,5.5)
    if (i>880 and i<900):
        burn(e,f,3)
    else:
        varepsilon_values_2.append(e)
        varepsilon_values_2.append(f)

# 循环获得随机数，并合并入列表
# q = 0
# z = []
# # for a in varepsilon_values_2:
# #     q=q+1
# #
# #     if q<3001:
# #         z.append(a)

# varepsilon_values_1 = []
# for s in z:
#     s=-s
#     varepsilon_values_1.append(s)

plt.rcParams['font.family'] = 'KaiTi'
plt.figure(figsize=(20,5),dpi=100)
plt.rcParams['axes.unicode_minus']=False  #让负号正常显示
plt.title("正常工况",fontsize=20,loc='center',color='purple')
plt.xlabel('时间/10-1s', fontsize=15, color='k')
plt.ylabel('y轴', fontsize=15, color='k')


plt.plot(varepsilon_values_2)
# print(varepsilon_values_2)
plt.show()



