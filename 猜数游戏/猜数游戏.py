import random
import os
import sys
import tkinter.messagebox
from tkinter import *
tkinter.Tk().withdraw();
print("欢迎来到SRI for PyGame之猜数字游戏！！！")
print("-------------------------------------------")
tkinter.messagebox.showinfo("欢迎来到SRI for PyGame之猜数字游戏！","按下确定键开始游戏");

def guess_num():
    max_retry = 6
    i=0
    print("请您定义一个猜数范围：")
    try:
        min = int(input("请输入最小值："))
        max = int(input("请输入最大值："))
    except:
        print("您的输入有误，请重新开始")
        tkinter.messagebox.showinfo("发生了错误","您的输入有误，请重新开始");
        os.system("pause")
        guess_num()
    try:
        random_num=random.randint(min,max)
    except:
        print("提醒：生成随机数的时候出现了错误，请您检查您输入的数值是否有误（大小值顺序相反、最小值小于0或最大值超出了预处理范围等其他原因）")
        tkinter.messagebox.showinfo("发生了错误","生成随机数的时候出现了错误，请您检查您输入的数值是否有误（大小值顺序相反、最小值小于0或最大值超出了预处理范围等其他原因）");
        os.system("pause")
        sys.exit()
    print("随机数已生成，您可以开始游戏了\n")
    tkinter.messagebox.showinfo("游戏将开始","随机数已生成，您可以开始游戏了");
    while i<max_retry:
         try:
             num=int(input("请输入一个在{}~{}间的数字：".format(min,max)))
             print(f'你的猜测是：{num}')
             if num>random_num:
                 print('>>但这太大了\n')
             elif num<random_num:
                 print('>>但这太小了\n')
             else:
                 print('恭喜你猜中了这个数字！')
                 tkinter.messagebox.showinfo("恭喜","恭喜你猜中了这个数字！");
                 os.system("pause")
                 sys.exit()
         except Exception as e:
             print('你输入的数字有误，它大于{}或小于了{}\n'.format(max,min))
             tkinter.messagebox.showinfo("发生了错误","你输入的数字有误，它大于{}或小于了{}".format(max,min));
         finally:
             i+=1
             print(f'剩余重试次数：{max_retry-i} \n')
    else:
        print('您的尝试次数已用尽，我们将结束游戏')
        print('正确的数字应该是：{}'.format(random_num))
        tkinter.messagebox.showinfo("很遗憾","您的尝试次数已用尽，我们将结束游戏\n正确的数字应该是：{}".format(random_num));
        os.system("pause")
        sys.exit()
        
guess_num()
