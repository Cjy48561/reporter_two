import pandas as pd
# 读取数据并删除带空值的行,删除房价为0的行
df=pd.read_excel('数据.xls',header=3).dropna()
df = df.drop(df[df['房价'] == 0].index)
# 日期设置
df['到日']=pd.to_datetime(df['到日'])
df['日期']=df['到日'].dt.strftime('%m-%d')
# 提成额度设置

# 天数
df['到日']=pd.to_datetime(df['到日'])
df['离日']=pd.to_datetime(df['离日'])
df['天数']=(df['离日']-df['到日']).dt.days
# 总提成=提成额度*天数

# 循环处理部分-提成处理部分

# 导出到excel
print(df[['日期','房号','姓名','房价','天数']])
df=df[['日期','房号','姓名','房价','天数']]
df.to_excel('demo.xlsx',index=False)


# 张红，李娜，黄丽伟，王斐，李康康，任晓瑜，陈雯文，陈洋
# ['日期','房号','姓名','房价','提成额度','天数','总提成','员工姓名']

if __name__=='__main__':
    pass