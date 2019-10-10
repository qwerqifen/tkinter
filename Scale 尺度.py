# 范围控件；显示一个数值刻度，为输出限定范围的数字区间
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):# 这里相比前面多了参数v，这里的参数v即将滚动条定位的数据，即如效果图中最开始，定位到5.00，label中显示you have selected 5.00
    l.config(text='you have selected ' + v)

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=1, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()
'''
参数from_=5，to=11的意思就是从5到11，即这个滚动条最小值为5，最大值为11（这里使用from_是因为在python中有from这个关键词）
参数orient=tk.HORIZONTAL在这里就是设置滚动条的方向，如我们所看到的效果图，这里HORIZONTAL就是横向。
参数length这里是指滚动条部件的长度，但注意的是和其他部件width表示不同，width表示的是以字符为单位，
    比如width=4，就是4个字符的长度，而此处的length=200，是指我们常用的像素为单位，即长度为200个像素
参数resolution=0.01这里我们可以借助数学题来理解，我们做的很多数学题都会让我们来保留几位小数，
    此处的0.01就是保留2位小数，即效果图中的5.00 9.00等等后面的两位小数，如果保留一位就是resolution=0.1 这里的showvalue就是设置在滚动条上方的显示。
    showvalue=0显示的就是效果图，上方无结果显示，如果改为showvalue=1，则会显示为：
'''

window.mainloop()
