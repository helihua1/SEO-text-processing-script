import pandas as pd

# 读取 Excel
input_file = "output.xlsx"
df = pd.read_excel(input_file, header=None)  # 假设无表头

output_rows = []

for idx, row in df.iterrows():
    keyword = row[0]  # 第一列是关键词
    content = str(row[1])  # 第二列内容
    # 按 '》》' 拆分成多行
    lines = content.split('》》')
    for line in lines:
        # 按 '|' 拆分单元格，并去掉首尾空格
        cells = [cell.strip() for cell in line.split('|')]
        # 在每行前加上关键词
        output_rows.append([keyword] + cells)

# 转成 DataFrame
df_out = pd.DataFrame(output_rows)

# 保存新的 Excel
output_file = f"{input_file}转为excel格式.xlsx"
df_out.to_excel(output_file, index=False, header=False)

print(f"转换完成，已生成文件：{output_file}")
