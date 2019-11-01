import random

# def tran(a,b,s):
#     a_ = int(a)
#     b_ = int(b)
#     if s == '+':
#         return  a_ + b_
#     elif s == '-':
#         return a_ - b_
#     elif s == '*':
#         return  a_ * b_
#     elif s == '/':
#         return a_ / b_
#     else:
#         return None

def cal(a, b, c, d):
    perm = [[a] + [b] + [c] + [d], [a] + [b] + [d] + [c], [a] + [c] + [b] + [d], [a] + [c] + [d] + [b],
            [a] + [d] + [b] + [c], [a] + [d] + [c] + [b], [b] + [a] + [c] + [d], [b] + [a] + [d] + [c],
            [b] + [c] + [a] + [d], [b] + [c] + [d] + [a], [b] + [d] + [a] + [c], [b] + [d] + [c] + [a],
            [c] + [a] + [b] + [d], [c] + [a] + [d] + [b], [c] + [b] + [a] + [d], [c] + [b] + [d] + [a],
            [c] + [d] + [a] + [b], [c] + [d] + [b] + [a], [d] + [a] + [b] + [c], [d] + [a] + [c] + [b],
            [d] + [b] + [a] + [c], [d] + [b] + [c] + [a], [d] + [c] + [a] + [b], [d] + [c] + [b] + [a]]
    symbols_1 = ['+++', '*++', '+*+', '**+', '*+*', '***', '++*', '+**',
                 '-++', '/++', '-*+', '/*+', '/+*', '/**', '-+*', '-**',
                 '+-+', '*-+', '+/+', '*/+', '*-*', '*/*', '+-*', '+/*',
                 '++-', '*+-', '+*-', '**-', '*+/', '**/', '++/', '+*/',
                 '*--', '*/-', '*-/',
                 '-*-', '/*-', '-*/',
                 '/-*', '--*', '-/*',
                 '//-', '/-/'
                 ]
    for nums in perm:
        for syms in symbols_1:

            # exp1 = tran(nums[0],nums[1], syms[0])
            # exp2 = tran(nums[0], nums[1], syms[0])

            exp = nums[0] + syms[0] + nums[1] + syms[1] + nums[2] + syms[2] + nums[3]
            if eval(exp) == 24:
                    print(exp)
                    return True
        for syms in symbols_1:
            exp = nums[0] + syms[0] + '(' + nums[1] + syms[1] + nums[2] + syms[2] + nums[3] + ')'
            if eval(nums[1] + syms[1] + nums[2] + syms[2] + nums[3]) != 0:
                if eval(exp) == 24:
                        print(exp)
                        return True
        for syms in symbols_1:
            exp = '(' + nums[0] + syms[0] + nums[1] + ')' + syms[1] + '(' + nums[2] + syms[2] + nums[3] + ')'
            if eval(nums[2] + syms[2] + nums[3]) != 0 or syms[1] != '/':
                if eval(exp) == 24:
                    print(exp)
                    return True
        for syms in symbols_1:
            exp = nums[0] + syms[0] + '(' + nums[1] + syms[1] + nums[2] + ')' + syms[2] + nums[3]
            if eval(nums[1] + syms[1] + nums[2]) != 0:
                if eval(exp) == 24:
                        print(exp)
                        return True
        for syms in symbols_1:
            exp = '(' + nums[0] + syms[0] + nums[1] + ')' + syms[1] + nums[2] + syms[2] + nums[3]
            if eval(exp) == 24:
                    print(exp)
                    return True
    print("No solution")
    return 0

if __name__ == '__main__':
    i = 0
    count = 0
    li = [0,0,0,0,0]
    dic = {'+++':0, '*++':0, '+*+':0, '**+':0, '*+*':0, '***':0, '++*':0, '+**':0,
           '-++':0, '/++':0, '-*+':0, '/*+':0, '/+*':0, '/**':0, '-+*':0, '-**':0,
           '+-+':0, '*-+':0, '+/+':0, '*/+':0, '*-*':0, '*/*':0, '+-*':0, '+/*':0,
                 '++-':0, '*+-':0, '+*-':0, '**-':0, '*+/':0, '**/':0, '++/':0, '+*/':0,
                 '+--':0, '*--':0, '+/-':0, '*/-':0, '*-/':0, '*//':0, '+-/':0, '+//':0,
                 '-+-':0, '/+-':0, '-*-':0, '/*-':0, '/+/':0, '/*/':0, '-+/':0, '-*/':0,
                 '--+':0, '/-+':0, '-/+':0, '//+':0, '/-*':0, '//*':0, '--*':0, '-/*':0,
                 '---':0, '/--':0, '-/-':0, '//-':0, '/-/':0, '///':0, '--/':0, '-//':0
           }
    while i < 1000:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        d = random.randint(1, 10)
        print("Given numbers : " + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d))
        m = cal(a, b, c, d)
        if m is True:
            # li[m-1] += 1
            count += 1
        i += 1
    print("Number of Solutions : " + str(count))
    print(li)

    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                    print("Given numbers : " + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d))
                    m = cal(a, b, c, d)
                    if m in dic:
                        count += 1
                        dic[m] += 1
    print("Number of Solutions : " + str(count))
    print(dic)
