import pandas as pd
import os

def batch_generate_html(template_path, excel_path):
    # 获取模板文件名（不带扩展名）
    template_name = os.path.splitext(os.path.basename(template_path))[0]

    # 读取 html 模版
    with open(template_path, "r", encoding="utf-8") as f:
        template_html = f.read()

    # 读取 excel
    # 默认情况下，pandas.read_excel() 会 把第一行作为列名（header），也就是 DataFrame 的列名。
    # DataFrame 的第一行索引是 0，对应 Excel 中的 第二行（第一行是标题）
    # 除非加上header=None
    df = pd.read_excel(excel_path)


    # 设置输出目录（同 excel 目录）
    excel_dir = os.path.dirname(excel_path)
    output_dir = os.path.join(excel_dir, f"根据{template_name}模版批量生成的结果")
    os.makedirs(output_dir, exist_ok=True)

    # 遍历 Excel 每一行
    for index, row in df.iterrows():
        # 新 html 文件名来自第二列
        output_name = str(row.iloc[1]) + ".html"
        output_file = os.path.join(output_dir, output_name)

        new_html = template_html

        # 第3列开始为替换字段1
        replace_start_col = 2

        for i in range(replace_start_col, len(row)):
            placeholder = f"【替换字段{i - replace_start_col + 1}】"
            value = "" if pd.isna(row.iloc[i]) else str(row.iloc[i])
            new_html = new_html.replace(placeholder, value)

        # 写新 HTML 文件
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(new_html)

    print("🎉 批量生成完成！文件已输出到：", output_dir)


# 主程序入口
if __name__ == "__main__":
    template = input("请输入 HTML 模版路径：").strip()
    excel = input("请输入 Excel 文件路径：").strip()
    # template = r"C:\Users\zhang\Downloads\专题单页简化\专题单页简化\zt\index.html"
    # excel = r"C:\Users\zhang\Downloads\专题单页简化\专题单页简化\静态文件批量生成-物料小样.xlsx"
    if not os.path.isfile(template):
        print("❌ HTML 模版文件不存在，请检查路径！")
        exit()

    if not os.path.isfile(excel):
        print("❌ Excel 文件不存在，请检查路径！")
        exit()

    batch_generate_html(template, excel)
