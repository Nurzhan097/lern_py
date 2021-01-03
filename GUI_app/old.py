
# def check_time():
#     time_text = time.strftime('%H:%M:%S')
#     print(time_text)
#     btn_time['text'] = time_text
#
#
# btn_time = Button(root, text="Check time", command=check_time)
# # btn_time.pack()
#
# count = 0
#
#
# def counter():
#     global count
#     count += 1
#     print(count)
#     btn_cnt['text'] = count
#
#
# btn_cnt = Button(root, text="Counter", command=counter)
# # btn_cnt.pack()
#
# l = Label(root, text="Hello \nlabel", bg='red', fg='white', font=("Time New Roman", ), justify=LEFT, width="50", height=10, anchor=NW)
# # l.pack()
#
# img = PhotoImage(file='calculator.png')
# l_logo = Label(root, image=img)
# # l_logo.pack()
#
# labl = Label(root,text="Input field", bg='blue', fg="white")
# labl.pack(fill=X)
#
# entr = Entry(root, text="Hello")
# entr.insert(0, "Hello")
# entr.insert(END, " world")
# entr.pack()
#
#
# def add_str():
#     entr.insert(END, "Na ")
#
#
# def del_str():
#     entr.delete(0, END)
#
#
# def get_str():
#     labl['text'] = entr.get()
#
#
# btn_add = Button(root, text="Add", command=add_str)
# btn_add.pack()
#
# btn_del = Button(root, text="Dell", command=del_str)
# btn_del.pack()
#
# btn_get = Button(root, text="Get", command=get_str)
# btn_get.pack()


# # Buttons
# l = Label(root, bg="white")
# l.pack(fill=X)
#
#
# def set_color(color):
#     l['bg'] = color
#     l['text'] = color
#
#
# colors = {
#     'red': 'Красный',
#     'orange': 'Оражнжевый',
#     'yellow': 'Желтый',
#     'green': 'Зеленый',
#     'blue': 'Голубой',
#     '#007dff': 'Синий',
#     '#7d00ff': 'Фиолетывый',
# }
#
#
# # for k, v in colors.items():
# #     Button(root, text=v, bg=k, command=(lambda color=k: set_color(color))).pack(fill=X)
#
# class MyButtons:
#     def __init__(self, master, text_color, hex_color):
#         self.master = master
#         self.text_color = text_color
#         self.hex_color = hex_color
#         self.b = Button(self.master, text=self.text_color, bg=self.hex_color, command=self.get_color)
#         self.b.pack(fill=X)
#
#     def get_color(self):
#         l['text'] = self.text_color
#         l['bg'] = self.hex_color
#
#
# for k, v in colors.items():
#     MyButtons(root, v, k)


# pack grid position

# f = Frame(root)
#
# f.pack()
#
# btns = [
#     [7, 8, 9],
#     [4, 5, 6],
#     [1, 2, 3],
#     [0],
# ]
#
#
# l2 = Label(root, text="Hello world", bg="#2ecc71", fg="#fff", font="16", padx=20, pady=8)
# l2.place(relx=0.5, rely=0.3, anchor=CENTER)
#
# for ind_r, row in enumerate(btns):
#     if len(row) <=1:
#         Button(f, text=row[0], padx=10, pady=10).grid(row=ind_r, columnspan=3)
#         continue
#     for ind_c, col in enumerate(row):
#         Button(f, text=col, padx=10, pady=10).grid(row=ind_r, column=ind_c)

# btn1 = Button(f, text='1', padx=10, pady=10).grid(row=0, column=0)
# btn2 = Button(f, text='2', padx=10, pady=10).grid(row=0, column=1)
# btn3 = Button(f, text='3', padx=10, pady=10).grid(row=0, column=2)
#
# l_user = Label(root, text="Login:").grid(row=0, column=0, padx=10, pady=10, sticky=E)
# e_user = Entry(root).grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky=W+E)
#
# l_pass = Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky=E)
# e_pass = Entry(root,  show="*").grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky=W+E)
#
# btn_login = Button(root, text="Вход",fg="white", bg="green", padx=5).grid(row=2, column=0, pady=20)
# btn_signin = Button(root, text="Регистрация", padx=5).grid(row=2, column=1)
# btn_forgot = Button(root, text="Забыли пароль?", padx=5).grid(row=2, column=2)


# l1 = Label(root, text="Hello world", bg="#3498db", fg="#fff", font="16", padx=15, pady=10)
# l1.place(x=0, y=0, )
#
#
# l3 = Label(root, text="Hello world", bg="#000", fg="#fff", font="16",)
# l3.place(relx=0.5, rely=0.5, anchor=CENTER, relheight=.8, relwidth=.8)


