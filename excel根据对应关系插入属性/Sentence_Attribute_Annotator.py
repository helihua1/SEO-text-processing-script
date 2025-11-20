import pandas as pd

# 读取ExcelA（句子表）
df_sentences = pd.read_excel("需要标注.xlsx", header=None)

# 读取ExcelB（属性-关键词表）
df_keywords = pd.read_excel("对应关系.xlsx", header=None)

# 构建关键词到属性的字典
keyword_to_attr = dict(zip(df_keywords[1], df_keywords[0]))

# 定义一个函数，根据句子匹配关键词
def match_attribute(sentence):
    for keyword, attr in keyword_to_attr.items():
        if str(keyword) in str(sentence):
            return attr
    return ""  # 没有匹配返回空

# 在原句子前插入一列
df_sentences.insert(0, '属性', df_sentences[0].apply(match_attribute))

# 保存结果
df_sentences.to_excel("需要标注_处理结果.xlsx", index=False, header=False)

print("处理完成！")
