# output

s21 = "姓名: {}, 性别: {}, 年龄: {}".format("张三", "男", 23)
print(s21)
s22 = "姓名: {2}, 性别: {1}, 年龄: {0}".format(23, "男", "张三")
print(s22)
s23 = "姓名: {n}, 性别: {g}, 年龄: {a}".format(a=23, g="男", n="张三")
print(s23)

s31 = "num: {:*^20,.3f}".format(31415.92657)  # num: *****31,415.927*****
print(s31)

s32 = "{{姓名: {0}, 性别: {1}}}".format("张三", "男")  # {姓名: 张三, 性别: 男}
print(s32)

name, gender, age = "张三", "男", 23
s41 = f"姓名: {name}, 性别: {gender}, 年龄: {age}"
print(s41)

s42 = f"{name = }, {gender = }, {age = }"  # name = '张三', gender = '男', age = 23
print(s42)

s43 = f"{{姓名: {name}, 性别: {gender}}}"  # {姓名: 张三, 性别: 男}
print(s43)
