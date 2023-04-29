import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from tkinter.simpledialog import askinteger, askstring


# 页面1展示内容
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Page 1", font=("Arial", 18))
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_page(Page2))
        button.pack()
# 页面2展示内容
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Page 2", font=("Arial", 18))
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page(Page1))
        button.pack()

        button1 = tk.Button(self, text="选择文件", command=lambda: controller.select_file())
        button1.pack()

        input_box = tk.Entry(self)
        input_box.pack()

        btn = tk.Button(self, text="设置员工总数和姓名", command=lambda :controller.input_count_emp())
        btn.pack()

# 主要设置
class mainloop(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # 设置窗口大小
        self.geometry("600x300")
        # 设置窗口位置
        self.geometry("+500+200")
        # 设置窗口标题
        self.title("散客报表生成器")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.pages = {}
        for F in (Page1, Page2):
            page = F(container, self)
            self.pages[F] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(Page1)
    # 页面切换函数
    def show_page(self, page):
        self.pages[page].tkraise()
    # 文件选择函数
    def select_file(self):
        self.withdraw()
        file_path=tkinter.filedialog.askopenfilename()
        tkinter.messagebox.showinfo('提示','你选择了'+file_path)
        self.destroy()
    # 用户输入员工总数和员工姓名并处理成字典数据例如{'陈洋':['洋']}
    def input_count_emp(self):
        count=askinteger(title='',
                           prompt='员工总数:')

        L = {}
        N_L = []
        NN_L = []

        for i in range(count):
            name=askstring(title='',
                           prompt='员工姓名:')
            L.setdefault(name, [])
        for m in L:
            for n in range(0, len(m)):
                L[m].append(m[n])
                L[m] = list(set(L[m]))
        # 将字典中值组成新列表并提取出重复出现的值
        for value in L.values():
            if isinstance(value, list):
                N_L += value
        for num in N_L:
            if N_L.count(num) > 1 and num not in NN_L:
                NN_L.append(num)
        # 进行比较，覆写字典中的值
        for i in L.keys():
            set1 = set(L[i])
            set2 = set(NN_L)
            intersection = set1.intersection(set2)
            L[i] = [x for x in L[i] if x not in intersection]
        print(L)

if __name__=='__main__':
    m=mainloop()
    m.mainloop()