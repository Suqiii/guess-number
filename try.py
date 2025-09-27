import tkinter as tk
import random

window = tk.Tk() # 创建主窗口对象
window.title("猜数字小游戏") # 设置窗口标题
window.geometry("800x600") # 设置窗口大小
window.config(bg="lightblue") # 设置窗口背景颜色

# 增加文字内容
welcome = tk.Label(window, text="欢迎来到猜数字小游戏！", font=("Arial", 28), bg="lightblue")
welcome.pack(pady=20)
name = tk.Label(window, text="制作人：Li", font=("Arial", 14), bg="lightblue")
name.pack(pady=15)

# 电脑随机生成数字
num = random.randint(1, 100)
# 记录猜测次数
count = 0

# 增加输入框
enter = tk.Entry(window, font=("Arial", 16))
enter.pack(pady=20)

# 增加结果显示标签
result = tk.Label(window, text="请输入1-100的数字", font=("Arial", 18), bg="lightblue")
result.pack(pady=15)

# 尝试次数显示标签
count_label = tk.Label(window, text=f"尝试次数: {count}/10", font=("Arial", 14), bg="lightblue")
count_label.pack(pady=5)

# 提前创建重新开始按钮，但先隐藏
restart_button = tk.Button(window, text="重新开始", font=("Arial", 16), command=lambda: new_game())
restart_button.pack(pady=10)
restart_button.pack_forget()  # 隐藏按钮

# 新游戏事件
def new_game():
    global num, count
    num = random.randint(1, 100)
    count = 0
    result.config(text="新游戏开始！请输入1-100的数字")
    count_label.config(text=f"尝试次数: {count}/10")
    enter.delete(0, tk.END)
    enter.config(state="normal")  # 启用输入框
    guess_button.config(state="normal")  # 启用猜测按钮
    restart_button.pack_forget()  # 隐藏重新开始按钮

# 按钮点击事件
def check_guess():
    global count
    guess_text = enter.get() # 获取输入框内容
    
    # 检查输入是否为空
    if not guess_text:
        result.config(text="请输入一个数字！")
        return
        
    # 检查输入是否为数字
    if not guess_text.isdigit():
        result.config(text="请输入有效的数字！")
        enter.delete(0, tk.END)
        return
    
    guess = int(guess_text)
    
    # 检查数字范围
    if guess < 1 or guess > 100:
        result.config(text="请输入1-100之间的数字！")
        enter.delete(0, tk.END)
        return
    
    count += 1
    count_label.config(text=f"尝试次数: {count}/10")

    if count >= 10 and guess != num:
        result.config(text=f"游戏结束！您已经猜了10次，正确答案是{num}。")
        enter.delete(0, tk.END)
        enter.config(state="disabled")  # 禁用输入框
        guess_button.config(state="disabled")  # 禁用猜测按钮
        restart_button.pack()  # 显示重新开始按钮
    elif guess < num:
        result.config(text=f"第{count}次：猜小了！再试一次！")
    elif guess > num:
        result.config(text=f"第{count}次：猜大了！再试一次！")
    else:
        enter.delete(0, tk.END)
        result.config(text=f"恭喜你，猜对了！您一共猜了{count}次。")
        enter.config(state="disabled")  # 禁用输入框
        guess_button.config(state="disabled")  # 禁用猜测按钮
        restart_button.pack()  # 显示重新开始按钮
    
    enter.delete(0, tk.END) # 清空输入框内容

# 增加猜测按钮
guess_button = tk.Button(window, text="猜一下", font=("Arial", 16), command=check_guess)
guess_button.pack(pady=10)

# 绑定回车键到猜测功能
enter.bind("<Return>", lambda event: check_guess())

window.mainloop() # 让窗口保持显示并响应用户的操作