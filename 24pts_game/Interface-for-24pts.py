import random
from itertools import permutations
from tkinter import *


def user_interface():

    global win
    global prompt
    global entry
    global submit_button
    global hint_button
    global num_combination

    win = Tk()
    win.title("Find 24")

    prompt = Label(win, text="Can you find the solution?")
    prompt.grid(row=1, column=1)

    entry = Entry()
    entry.grid(row=2, column=1)

    submit_button = Button(win, text="Submit", width=10)
    submit_button.grid(row=3, column=1)

    hint_button = Button(win, text="Give me a hint", width=10)
    hint_button.grid(row=4, column=1)

    win.mainloop()


user_interface()


def give_hint():
    print_solutions(num_combination)


def generate_nums(bound):
    global result

    result = []
    for i in range(4):
        result.append(random.randint(0, bound - 1) + 1)

    return result


def sign(num):
    if num == 0:
        return "+"
    if num == 1:
        return "-"
    if num == 2:
        return "*"

    return "/"


def permutate(nums):
    result = []
    permutation_result = permutations(nums)

    for i in permutation_result:
        result.append(list(i))

    return result


def arrange_nums(a, b, c, d):
    result = []
    for x in [a, b, c, d]:
        re = str(x)
        li = [a, b, c, d]
        li.remove(x)
        for y in li:
            re += str(y)
            li.remove(y)
            for z in li:
                re += str(z)
                li.remove(z)
                for m in li:
                    re += str(m)
                    result.append(re)
    return result


def find24_for_all(nums):
    permutated_list = permutate(nums)
    result = []

    for i in permutated_list:
         result += find24_for_one(i)

    return remove_duplicate(result)


def remove_duplicate(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)

    return newlist


def find24_for_one(nums):
    result = general_condition(nums)
    if exception1(nums) is not None:
        result.append(exception1(nums))
    if exception2(nums) is not None:
        result.append(exception2(nums))

    return result


def general_condition(nums):
    a = nums[0]
    b = nums[1]
    c = nums[2]
    d = nums[3]
    final_result = []

    for i in range(4):
        result1 = calculate(a, b, i)

        for j in range(4):
            result2 = calculate(result1, c, j)

            for k in range(4):
                result3 = calculate(result2, d, k)

                if result3 == 24:
                    final_result.append(formula(a, b, c, d, i, j, k))
                else:
                    result3 = result2

    return final_result


"""
    When first & third are * or / && second is + or =
"""


def exception1(nums):
    a = nums[0]
    b = nums[1]
    c = nums[2]
    d = nums[3]

    if a * b - c * d == 24:
        return str(a) + "*" + str(b) + "-" + str(c) + "*" + str(d)
    elif a * b + c * d == 24:
        return str(a) + "*" + str(b) + "+" + str(c) + "*" + str(d)
    elif a * b - c / d == 24:
        return str(a) + "*" + str(b) + "-" + str(c) + "/" + str(d)
    elif a * b + c / d == 24:
        return str(a) + "*" + str(b) + "+" + str(c) + "/" + str(d)
    elif a / b + c / d == 24:
        return str(a) + "/" + str(b) + "+" + str(c) + "/" + str(d)
    elif a / b - c / d == 24:
        return str(a) + "/" + str(b) + "-" + str(c) + "/" + str(d)
    elif a / b + c * d == 24:
        return str(a) + "/" + str(b) + "+" + str(c) + "*" + str(d)
    elif a / b - c * d == 24:
        return str(a) + "/" + str(b) + "-" + str(c) + "*" + str(d)
    else:
        return None


"""
    When first & third are + or - && second is * or /
"""


def exception2(nums):
    a = nums[0]
    b = nums[1]
    c = nums[2]
    d = nums[3]

    if a - b != 0 and c - d != 0:
        if (a + b) * (c + d) == 24:
            return "(" + str(a) + "+" + str(b) + ")" + "*(" + str(c) + "+" + str(d) + ")"
        elif (a + b) / (c + d) == 24:
            return "(" + str(a) + "+" + str(b) + ")" + "/(" + str(c) + "+" + str(d) + ")"
        elif (a + b) * (c - d) == 24:
            return "(" + str(a) + "+" + str(b) + ")" + "*(" + str(c) + "-" + str(d) + ")"
        elif (a + b) / (c - d) == 24:
            return "(" + str(a) + "+" + str(b) + ")" + "/(" + str(c) + "-" + str(d) + ")"
        elif (a - b) * (c - d) == 24:
            return "(" + str(a) + "-" + str(b) + ")" + "*(" + str(c) + "-" + str(d) + ")"
        elif (a - b) / (c - d) == 24:
            return "(" + str(a) + "-" + str(b) + ")" + "/(" + str(c) + "-" + str(d) + ")"
        elif (a - b) * (c + d) == 24:
            return "(" + str(a) + "-" + str(b) + ")" + "*(" + str(c) + "+" + str(d) + ")"
        elif (a - b) / (c + d) == 24:
            return "(" + str(a) + "-" + str(b) + ")" + "/(" + str(c) + "+" + str(d) + ")"
        else:
            return None
    else:
        return None


def formula(a, b, c, d, i, j, k):
    if (sign(j) == "*" or sign(j) == "/") and (sign(i) == "+" or sign(i) == "-"):
        return "(" + str(a) + sign(i) + str(b) + ")" + sign(j) + str(c) + sign(k) + str(d)

    elif (sign(k) == "*" or sign(k) == "/") and (sign(j) == "+" or sign(j) == "-"):
        return "(" + str(a) + sign(i) + str(b) + sign(j) + str(c) + ")" + sign(k) + str(d)

    return str(a) + sign(i) + str(b) + sign(j) + str(c) + sign(k) + str(d)


def calculate(a, b, condition):
    if condition == 0:
        return a + b
    elif condition == 1:
        return a - b
    elif condition == 2:
        return a * b
    elif condition == 3:
        return a / b


def has_solution(nums):
    return find24_for_all(nums) != []


def print_solutions(nums):
    solutions = find24_for_all(nums)

    if len(solutions) == 1:
        str = "Solution: "
    elif len(solutions) == 0:
        str = "No result is found"
    else:
        str = "Solutions: "

    for i in find24_for_all(nums):
        str = str + i + ", "

    str = str[: len(str) - 2]

    print(str)


def ask_solution():
    nums = generate_nums(10)

    while not has_solution(nums):
        nums = generate_nums(10)

    print("Plz give the solution for" + str(nums) + "\n" + """Press "E" to give the right answer""")

    user_solution = input(">>")

    while user_solution not in find24_for_all(nums):

        if user_solution == "E":
            print_solutions(nums)
            break

        print("Your answer is wrong. Plz try again!")
        user_solution = input(">>")

    if user_solution != "E":
            print("You are a genius!")

    replay = input("Do you want to play again?")

    while replay != "y" or "n":
        if replay == "y":
            return True
        elif replay == "n":
            return False

        replay = input("Do you want to play again?")


def repeat_solutions():
    while ask_solution():
        ask_solution()


# repeat_solutions()


def give_solution():
    nums_str = input("What are the numbers that you want to calculate 24?")

    nums = []

    for i in nums_str:
        nums.append(int(i))

    print_solutions(nums)


def get_nums_collection(times):
    result = []

    for i in range(times):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        d = random.randint(1, 10)
        nums = [a, b, c, d]

        result.append(nums)

    return result


def test(nums_collection):
    count = 0
    count_false = 0

    for nums in nums_collection:

        for i in find24_for_all(nums):
            if eval(str(i)) != 24:
                count_false += 1

        if has_solution(nums):
            count += 1

    print("ZF'S Game: Number of Solutions : " + str(count))
    print("ZF'S Game: False solutions:" + str(count_false))


# if __name__ == "__main__":
#     count = 0
#     for a in range(1, 11):
#         for b in range(1, 11):
#             for c in range(1, 11):
#                 for d in range(1, 11):
#                     print("Given numbers : " + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d))
#                     if has_solution([a, b, c, d]):
#                         count += 1
#     print("Number of Solutions : " + str(count))


