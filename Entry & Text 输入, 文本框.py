# View more python learning tutorial on my Youtube and Youku channel!!!
# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
# e = tk.Entry(window, show="*")
e = tk.Entry(window, show="") # Entry语法格式如下：
                                    # w = Entry( master, option, ... )
                                    # master: 按钮的父容器。
                                    # options: 可选项，即该按钮的可设置的属性。这些选项可以用键 = 值的形式设置，并以逗号分隔。
e.pack()

def insert_point():
    var = e.get() # var是enter输入的值
    t.insert('insert', var) #insert()方法语法：
                                #list.insert(index, obj)
                                    #index -- 对象 obj 需要插入的索引位置。
                                    #obj -- 要插入列表中的对象。
def insert_end():
    var = e.get()
    # t.insert('end', var)
    t.insert('end', var)

b1 = tk.Button(window, text='insert point', width=15,
              height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end',
               command=insert_end)
b2.pack()
t = tk.Text(window, height=2) #text可以直接输入 用于显示多行文本
t.pack()

window.mainloop()
