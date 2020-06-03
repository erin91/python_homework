#coding=utf-8
"""
    --->> 整数(int类)    v ＝ 1
    --->> 布尔值(bool类)   v ＝ True
    --->> 字符串(str类)   v ＝ "ABC123"
    --->> 列表(list类)    v = ["张三",18,"学习"]
                    v[2]
                    v[0] = "李四"
    --->> 元祖(tuple类)    v = ("张三",18,"学习")
    --->> 字典(dict类)    v = {
                        "name":"张三",
                        "age":18,
                        "hobby":"看书"
                        }
                    v['name']
                    v['age']
"""
#------------->>> str类中当前对象提供的功能，字符串原值不变 <<<-------------
# a.upper()   #所有变大写
# a.lower()   #所有变小写
# a.capitalize()  #首字母变大写其他为小写
# a.strip()   #去除首尾空格
# a.lstrip()  #去除左边空格
# a.rstrip()  #去除右边空格
# a.split("aaa")    #以aaa为分隔符分割字符串
# a.split("aaa"，2)    #以aaa为分隔符分割字符串，分割到第二个停止
# a.isdecimal() ＃判断a中是数字
# a.replace("要替换的值","想替换的值",2) # 数字为想替换第几个，不传则替换所有 替换功能
# #求字符串长度&取值
#     v = "哈哈大家都打开看看打开看看看看看看看"
#     le = len(v) - 1
#     value = le[2] #取字符串中某一个字符
#     value = le[-2] #取字符串从后往前数倒数第2个字符
#     value = v[0:5] #取字符串中从0，1，2，3，4位置的字符，不包括5
#     value = v[4:] #取字符串中从4开始到最后一位的字符
#     value = v[4,-1] #取字符串中从4开始到倒数第二个字符，不包括最后一位字符
#     value = v[1:15:2] #取字符串中从1开始以2的步长取值，直到第14位字符
#
# 练习题1:
# v = "哈都会觉得到了哈哈哈后来山山水水哈思考算了睡觉睡觉"
# le = len(v)-1
# i = 0
# while i<le:
#     value = v[i]
#     print(value)
#     i+=1
# print("字符串长度是： " +str(le))
# val = v[2:8:3]
# print(val)

#练习题2: 做一个加法计算器
# v1 = input("请输入第一个数字： ")
# v2 = input("请输入第二个数字： ")
# v3 = int(v1) + int(v2)
# print("您输入的数字之和22是： " + str(v3))

# int(v)    str(v)  bool(v)

#------------->>> list类中当前对象提供的功能 <<<-------------
# v = [11,22,33,"快看看","hh哈哈"]
# print(v)
# v.append("张山")  #在列表后面加数据
# print(v)
# v.insert(2,"李四")    #在列表中指定位置插入数据
# print(v)
# value =v[2]
# print(value)    #取列表某一数据
# value1 = v[2:6]
# value2 = v[0:6:2]
# print(value1,value2)
# v[3] = "22122"
# print(v)
# del v[3]    #删除列表某一数据
# print(v)
# del v[2:4]  #删除列表某一段数据
# print(v)
# v[3:7]=["高规格","uuu","快看看","jsjg","逛逛街是"]
# print(v)
# v.reverse() #将列表反转排序
# print(v)
# v = ["会打开看看","考克斯","京津冀经济界",666]
# print(v[1][1])  #取列表第2个字符串中的第2个值
#
# # 练习题：
# v = ["赶大集",[11,22,33,"空空旷旷",555],"哈萨克",888]
# print(v[1][3][1:3])
# print(v)
# v[1][3]= v[1][3].replace("空旷","很好")
# print(v)
#

#------------->>> tuple类中当前对象提供的功能,只能获取，不能修改 <<<-------------
# 元祖中列表、字典可以被修改，元祖本身不能被修改
# v = (111,222,333,444,555,666)
# val = len(v)
# print(v)
# print(v[2])
# print(v[0:5])
# print(v[1:5:2])
#
# v = (111,222,333,444,("aaa","bbb",987),666,["www","可视化",226,],"经济界",999)
# print(v)
# v[6].append("jsjs")
# print(v)

#------------->>> dict类中当前对象提供的功能,只能获取，不能修改 <<<-------------
v = {
    "k1":"v1",
    "k2":"v2",
}

# val = v.get('k1')   #key不存在，默认取none
# print(val)
# #搭配for循环一起使用
#     val = v.keys()
#     print(val)
#     val = v.values()
#     print(val)
#     val = v.items()
#     print(val)
# print(len(v))
# # 存在则更新对应值，不存在则创建键值对
# v['k2'] = 888
# print(v)
# v['k3'] =3333
# print(v)
# del v['k3'] #删除键值对
# print(v)
#
# for i in v.keys():
#     print(i,v[i])
#
# for a,b in v.items():
#     print(a,b)
# print("<<<----------------分隔符---------------->>>")
# 字典嵌套
val = {
    'k1':123,
    'k2':"sshh2d",
    'k3':True,
    'k4':[111,222,333],
    'k5':(1,2,3),
    'k6':{
        'kk1':'vv1',
        'kk2':'vv2'
    },
    'k7':[1,2,(56,99,72),{"k111":'v111'},55]
}
print(val)

val['k7'][4] = 66
print(val)
val['k4'].append(444)
print(val)
val['k6']['kk3'] = 333
print(val)
del val['k6']['kk3']
print(val)






