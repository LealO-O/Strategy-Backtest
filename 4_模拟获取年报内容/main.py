## 分为两部分
# 1. copy内容
# 2.合并行
import subprocess
import pyautogui
import time

# 定义PDF文件的路径
pdf_file_path = "C:/Users/PC208/Desktop/横向extract文本/pdf/2020-03-16__中航航空高科技股份有限公司__600862__中航高科__2019年__年度报告.pdf"

# 打开PDF阅读器应用程序（例如，Adobe Acrobat Reader）
subprocess.Popen(["start", "msedge.exe", pdf_file_path], shell=True)

# 等待一段时间以确保PDF阅读器应用程序已经打开
time.sleep(5)

# 模拟按下Ctrl+A（选择所有文本）
pyautogui.hotkey("ctrl", "a")

# 等待一段时间以确保文本被选择
time.sleep(2)

# 模拟按下Ctrl+C（复制选定文本）
pyautogui.hotkey("ctrl", "c")

# 文本已经复制到剪贴板，可以在此粘贴或进行其他操作


# 一些应用程序可能需要时间来处理粘贴操作，所以等待一段时间
time.sleep(2)

# 定义要写入的文本文件的路径
txt_file_path = "C:/Users/PC208/Desktop/横向extract文本/b.txt"  # 替换为实际的txt文件路径
subprocess.Popen(["start", "notepad.exe", txt_file_path], shell=True)
# 模拟按下Enter键，将粘贴的文本保存到txt文件
pyautogui.press("enter")
# 模拟按下Ctrl+V（粘贴操作）
time.sleep(2)
pyautogui.hotkey("ctrl", "v")
print(f"文本已成功粘贴到 {txt_file_path}")

# 将不同行合并成一行
# 定义文本文件的路径
txt_file_path = "C:/Users/PC208/Desktop/横向extract文本/b.txt"  # 替换为实际的txt文件路径


# 打开文本文件并读取内容
with open(txt_file_path, "r", encoding="utf-8") as txt_file:
    lines = txt_file.readlines()

# 合并多行文本为一行
merged_text = ' '.join([line.strip() for line in lines])

# 输出合并后的文本内容
print(merged_text)

