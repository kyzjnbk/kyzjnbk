# %%

'''
How to use class
'''

def cal(x, y, kind):
    if kind == '+':
        val = x + y
    return val # val = x +-*/ y


# %%
x = 1
y = 2
kind = '+'

print('>>> calculator:')
print(cal(x, y, kind))


# %%
class CAL(): # 类
    def __init__(self, kind): # 类的初始化函数
        self.kind = kind
        return

    def calculation_2(self, x, y): # 方法 / 函数
        if self.kind == '+':
            return x + y

    def calculation_3(self, x, y, z):
        if self.kind == "+": # 调用类里所有函数共用的变量
            res1 = self.calculation_2(x, y) # 调用类里定义的其他函数
            res2 = self.calculation_2(res1, z)
            return res2

cal = CAL(kind='+') # 类的实例，当类传入初始化参数后，就会得到一个实例

print(cal.calculation_2(1, 2))
print(cal.calculation_3(1, 2, 3))
# %%
