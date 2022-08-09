from datetime import datetime
from tkinter import *
from tkinter.ttk import Combobox

from seckill.taobao import TaoBao
from seckill.jd import JDong


def run_killer(time, password, platform):
    # 抢购时间
    seckill_time = time.get()
    # 支付密码
    password = str(password.get())
    # 平台类型
    platform = platform.get()
    # print(seckill_time, password)
    if platform == "京东":
        JDong(seckill_time_str=seckill_time, password=password).sec_kill(login_time_out=20)
    elif platform == "淘宝":
        TaoBao(seckill_time_str=seckill_time, password=password).sec_kill(login_time_out=20)
    else:
        raise Exception("未知平台类型")


def main():
    win = Tk()
    win.title('电商秒杀助手')
    width = 540
    height = 350
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    win.geometry(align_str)

    # 设置开抢时间
    label1 = Label(win, text="开抢时间:", width=12, height=3, font=("Lucida Grande", 12))
    label1.grid(column=0, row=0)
    start_time = StringVar()
    time = Entry(win, textvariable=start_time, width=23, fg="blue", font=("Lucida Grande", 12))
    time.grid(column=1, row=0)
    start_time.set(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # 支付密码
    label2 = Label(win, text="支付密码:", width=12, height=2, font=("Lucida Grande", 12))
    label2.grid(column=0, row=1)
    password = Entry(win, width=23, show='*', fg="blue", font=("Lucida Grande", 12))
    password.grid(column=1, row=1)

    # 选择平台
    label3 = Label(win, text="抢购平台:", width=12, height=3, font=("Lucida Grande", 13))
    label3.grid(column=0, row=2)
    platform_value = StringVar()
    platform = Combobox(win, textvariable=platform_value, width=18, font=("Lucida Grande", 13))
    platform["values"] = ("京东", "淘宝")
    # 默认选择第一个
    platform.current(0)
    platform.grid(column=1, row=2)

    # 开始抢购
    b1 = Button(win, text='开始抢购',
                command=lambda: run_killer(time, password, platform),
                background="green", width=21, height=6,
                font=("Lucida Grande", 13))
    b1.place(x=320, y=16)
    win.resizable(width=False, height=False)

    # 使用说明
    txt0 = Label(win, text='使用说明:', width=10, height=1, font=("Lucida Grande", 11), fg='green')
    txt0.place(x=10, y=150)

    txt1 = Label(win, text='1、安装chrome浏览器以及chromeDriver（放置在python安装根目录下）',
                 font=("Lucida Grande", 10),
                 fg='green')
    txt1.place(x=15, y=180)

    txt2 = Label(win, text='2、抢购前要清空购物车，然后把要抢的东西加入购物车',
                 font=("Lucida Grande", 10),
                 fg='green')
    txt2.place(x=15, y=205)

    txt3 = Label(win, text='3、开抢时间必须是 %Y-%m-%d %H:%M:%S 形式，如2020-12-29 12:10:15',
                 font=("Lucida Grande", 10),
                 fg='green')
    txt3.place(x=15, y=230)

    txt4 = Label(win, text='4、输入开抢时间和支付密码后点开始，程序会控制浏览器打开淘宝登陆页',
                 font=("Lucida Grande", 10),
                 fg='green')
    txt4.place(x=15, y=255)

    txt5 = Label(win, text='5、扫码登陆后，程序会自动刷新购物车页面，到点会完成抢购动作',
                 font=("Lucida Grande", 10),
                 fg='green')
    txt5.place(x=15, y=280)

    txt6 = Label(win, text='6、如果想手动付款，输入开抢时间后不用输入支付密码，直接点开始就可以了',
                 font=("Lucida Grande", 10),
                 fg='green')
    txt6.place(x=15, y=305)
    win.mainloop()


if __name__ == '__main__':
    main()
