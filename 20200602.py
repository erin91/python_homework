#coding=utf-8
#2020.6.2的练习题目
#作业1: 打印 1～99 之间所有的奇数
#作业2： 打印1～99之间所有能被3整除的整数
#作业3: 打印1+2+...＋100的和
#作业4: 打印1～99 之间所有奇数总和
#作业5: 打印1-2+3-4+。。。＋99 总和


# 作业1:打印1～99之间所有的奇数

i=1
while i<100:
    if i%2==0:
        pass
    else:
        print(i)
    i+=1
print("---------->>> 作业1已完成")

# 作业2： 打印1～99之间所有能被3整除的整数
i=1
while i<100:
    if i%3==0:
        print(i)
    else:
        pass
    i+=1
print("---------->>> 作业2已完成")


# 作业3: 打印1+2+...＋100的和
i=1
sum=0
while i<100:
    sum+=i
    i+=1
print(sum)
print("---------->>> 作业3已完成")

# 作业4: 打印1～99 之间所有奇数总和
i=1
sum=0
while i<100:
    if i%2==0:
        pass
    else:
        sum+=i
    i+=1
print(sum)
print("---------->>> 作业4已完成")


# 方式1作业5: 打印1-2+3-4+。。。＋99 总和
i=1
sum=0
while i<100:
    if i%2==0:
        sum-=i
    else:
        sum+=i
    i+=1
print(sum)
#方式2完成作业5: 打印1-2+3-4+。。。＋99 总和
sum = 0
for i in range(1, 100):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i

print(sum)
print("---------->>> 作业5已完成")

# 占位符只有格式化时才有意义，不想让％表示为格式化时候，再加上一个％
name = input("请输入姓名：")
age = input("请输入年龄：")
hobby = input("请输入爱好：")
msg = "我的名字是%s,我的年龄是%s,我的爱好是%s，学习进度是80%%" %(name,age,hobby)
print(msg)




