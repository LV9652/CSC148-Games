# import random
#
#
# def generateNums(bound):
#     result = []
#     for i in range(4):
#         result.append(random.randint(0, 10))
#
#     return result
#
#
# def sign(num):
#     if num == 0:
#         return "+"
#     if num == 1:
#         return "-"
#     if num == 2:
#         return "*"
#
#     return "/"
#
#
# def run(nums):
#     a = nums[0]
#     b = nums[1]
#     c = nums[2]
#     d = nums[3]
#
#     result = 0
#
#     for i in range(4):
#         result = calculate(a, b, i)
#
#         for j in range(4):
#             result = calculate(result, c, j)
#
#             for k in range(4):
#                 result = calculate(result, d, k)
#
#                 if result == 24:
#                     print(result)
#                     return formula(a, b, c, d, i, j, k)
#
#
# def formula(a, b, c, d, i, j, k):
#
#     return str(a) + sign(i) + str(b) + sign(j) + str(c) + sign(k) + str(d)
#
#
# def calculate(a, b, condition):
#     if condition == 0:
#         return a + b
#     elif condition == 1:
#         return a - b
#     elif condition == 2:
#         return a * b
#     elif condition == 3:
#         return a / b
#
#
# nums = generateNums(10)
# print(nums)
#
# formula = run([8, 8, 8, 6])
#
# print(formula)

# result = []
# for x in 'abcd':
#     re = x
#     li = 'abcd'
#     li = li.strip(x)
#     for y in li:
#         re += y
#         li = li.strip(y)
#         for z in li:
#             re += z
#             li = li.strip(z)
#             for m in li:
#                 re += m
#                 result.append(re)
# print(result)
#
#
# symbols_1 = ['+++', '*++', '+*+', '**+', '*+*', '***', '++*', '+**',
#              '-++', '/++', '-*+', '/*+', '/+*', '/**', '-+*', '-**',
#              '+-+', '*-+', '+/+', '*/+', '*-*', '*/*', '+-*', '+/*',
#              '++-', '*+-', '+*-', '**-', '*+/', '**/', '++/', '+*/',
#              '+--', '*--', '+/-', '*/-', '*-/', '*//', '+-/', '+//',
#              '-+-', '/+-', '-*-', '/*-', '/+/', '/*/', '-+/', '-*/',
#              '--+', '/-+', '-/+', '//+', '/-*', '//*', '--*', '-/*',
#              '---', '/--', '-/-', '//-', '/-/', '///', '--/', '-//'
#              ]

if __name__ == '__main__':
    for i in range(100000):
        exp = '3/4*(10+2)'
        eval(exp)
        print(exp)
if __name__ == "__main__":
    count = 1
    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                    print("Given numbers : " + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d))
                    if cal(a, b, c, d) is True:
                        count += 1
    print("Number of Solutions : " + str(count))
