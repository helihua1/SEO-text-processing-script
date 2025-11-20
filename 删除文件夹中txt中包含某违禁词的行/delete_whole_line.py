import os
import shutil
'''
在一个文件夹下的，包括其子文件夹 中，有很多txt文件，每个txt有很多行，
如果某一行包含 违禁词.txt 中的某个词（很多行，每行是一个违禁词），就删除整行。处理后所有的文件放入一个新的文件夹中。
'''



# ======= 参数设置 =======
# 原始 txt 文件所在的根目录
input_folder = "D:\写的所有程序都在这里\小工具集合\删除文件夹中txt中包含某违禁词的行\需要处理"
output_folder = input_folder + "-过滤后文本"        # 处理后的输出目录
banned_file = "违禁词.txt"          # 存放违禁词的文件路径
encoding = "utf-8"                  # 文件编码，可改为 gbk、utf-8-sig 等

# ======= 读取违禁词 =======
with open(banned_file, "r", encoding=encoding) as f:
    banned_words = [line.strip() for line in f if line.strip()]
print(banned_words)
print(f"已加载违禁词 {len(banned_words)} 个")

# ======= 处理函数 =======
def contains_banned_word(line):
    return any(word in line for word in banned_words)

def process_file(input_path, output_path):
    """读取单个文件并删除包含违禁词的行"""
    with open(input_path, "r", encoding=encoding, errors="ignore") as fin:
        lines = fin.readlines()

    filtered_lines = [line for line in lines if not contains_banned_word(line)]

    # 确保输出路径存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding=encoding) as fout:
        fout.writelines(filtered_lines)

# ======= 遍历文件夹 =======
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)  # 删除旧的输出目录
os.makedirs(output_folder)

for root, dirs, files in os.walk(input_folder):
    for filename in files:
        if filename.endswith(".txt"):
            input_path = os.path.join(root, filename)
            # 保持原文件夹结构
            rel_path = os.path.relpath(input_path, input_folder)
            output_path = os.path.join(output_folder, rel_path)

            process_file(input_path, output_path)

print("✅ 所有文件已处理完毕！")
