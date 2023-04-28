# 用户输入用户员工总数
# total_emp=int(input("请输入提成员工总数:"))
# L={}
# N_L=[]
# NN_L=[]
# # 用户循环输入员工姓名
# for i in range(total_emp):
#     L.setdefault(input("请输入员工姓名:"),[])
# for m in L:
#     for n in range(0, len(m)):
#         L[m].append(m[n])
#         L[m]=list(set(L[m]))
# # 将字典中值组成新列表并提取出重复出现的值
# for value in L.values():
#     if isinstance(value,list):
#         N_L+=value
# for num in N_L:
#     if N_L.count(num) > 1 and num not in NN_L:
#         NN_L.append(num)
# # 进行比较，覆写字典中的值
# for i in  L.keys():
#     set1 = set(L[i])
#     set2 = set(NN_L)
#     intersection = set1.intersection(set2)
#     L[i] = [x for x in L[i] if x not in intersection]
L1=['日期','房号','姓名','房价','提成额度','天数','总提成','员工姓名']
L2=['张红','李娜','黄丽伟','王斐','李康康','任晓瑜','陈雯文','陈洋']
print(L1+L2)