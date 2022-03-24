###############
#  Create by  #
#   kiri11    #     
###############
def WhatItIs(Task):
    flagSum, flagQuan, flagMin, flagMax, flagEnd, flagMult = False, False, False, False, False, False
    if "сумма" in Task or "сумму" in Task:
        flagSum = True
    if "определяет количество чисел" in Task:
        flagQuan = True
    if "кратное" in Task or "кратных" in Task:
        if "кратное" in Task:
            digitalMult = Task[Task.find("кратное") + 8]
        if "кратных" in Task:
            digitalMult = Task[Task.find("кратных") + 8]
        flagMult = True
    if "оканчивающееся" in Task or "оканчивающихся" in Task:
        if "оканчивающееся" in Task:    
            digitalEnd = Task[Task.find("оканчивающееся") + 18]
        if "оканчивающихся" in Task:
            digitalEnd = Task[Task.find("оканчивающихся") + 18]
        flagEnd = True
    if "максимальное число" in Task:
        flagMax = True
    if "минимальное число" in Task:
        flagMin = True
    if flagMult == True and flagEnd == False:
        return flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, digitalMult, 0
    elif flagMult == False and flagEnd == True:
        return flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, 0, digitalEnd
    else:
        return flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, digitalMult, digitalEnd 
def decisionWhile(flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, digitalMult, digitalEnd, Task):
    if flagSum == True:
        sum1=0
        if flagEnd == True and flagMult == True:
            x=int(input("Введите входные данные "))
            while x != 0:
                if x % 10 == digitalEnd and x % digitalMult == 0:
                    sum1+=x
                x=int(input())
        elif flagEnd == True or flagMult == True:
            if flagEnd == True:
                x=int(input("Введите входные данные "))
                while x != 0:
                    if x % 10 == digitalEnd:
                        sum1+=x
                    x=int(input())
            elif flagMult == True:
                x=int(input("Введите входные данные "))
                while x != 0:
                    if x % digitalMult == 0:
                        sum1+=x
                    x=int(input())
        result = sum1
    elif flagQuan == True:
        if flagMult == True and flagEnd == True:
            x,k=int(input("Введите входные данные ")),0
            while x != 0:
                if x % 10 == digitalEnd and x % digitalMult == 0:
                    k+=1
            x=int(input())
        elif flagMult == True:
            x,k=int(input("Введите входные данные ")),0
            while x != 0:
                if x % digitalMult == 0:
                    k+=1
            x=int(input())
        elif flagEnd == True:
            x,k = int(input()), 0
            while x != 0:
                if x % 10 == digitalEnd:
                    k+=1
            x=int(input())
        result = k
    if flagQuan == True and flagSum == True:
        if "количество введёных чисел" in Task:
            if flagMult == True and flagEnd == True:
                x, k, sum1 = int(input()), 0, 0
                while x != 0:
                    if x % 10 == digitalEnd and x % digitalMult == 0:
                        sum1 += x
                    k += 1
            elif flagMult == True:
                x, k, sum1 = int(input()), 0, 0
                while x != 0:
                    if x % digitalMult == 0:
                        sum1 += x
                    k += 1
            elif flagEnd == True:
                x, k, sum1 = int(input()), 0, 0
                while x != 0:
                    if x % 10 == digitalEnd:
                        sum1 += x
                    k += 1
    if flagMax == True:
        x=int(input("Введите входные данные "))
        max1 = -30001
        while x != 0:
            if flagEnd == True:
                if x % 10 == digitalEnd and x > max1:
                    max1 = x
            elif flagMult == True:
                if x % digitalMult == 0 and x > max1:
                    max1 = x
            elif flagMult == True and flagEnd == True:
                if x % digitalMult == 0 and x % 10 == digitalEnd and x > max1:
                    max1 = x
            x = int(input())
        result = max1
    if flagMin == True:
        x = int(input("Введите входные данные "))
        min1 = 30001
        while x != 0:
            if flagEnd == True:
                if x % 10 == digitalEnd and x < max1:
                    min1 = x
            elif flagMult == True:
                if x % digitalMult == 0 and x < max1:
                    min1 = x
            elif flagMult == True and flagEnd == True:
                if x % digitalMult == 0 and x % 10 == digitalEnd and x < max1:
                    min1 = x
            x = int(input())
        result = max1
    return result
def decisionFor(flagSum,flagQuan,flagEnd,flagMult,flagMax,flagMin,digitalMult,digitalEnd,Task):
    much = int(input("Введите сколько раз будет введных чисел "))
    if flagSum == True:
        if flagEnd == True:
            sum1 = 0
            for _ in range(much):
                x = int(input())
                if x % 10 == digitalEnd:
                    sum1 += x
        elif flagMult == True:
            sum1 = 0
            for _ in range(much):
                x = int(input())
                if x % digitalMult == 0:
                    sum1 += x
        elif flagMult == True and flagEnd == True:
            sum1 = 0
            for _ in range(much):
                x = int(input())
                if x % digitalMult == 0 and x % 10 == digitalEnd:
                    sum1 += x
        result = sum1
    elif flagQuan == True:
        if flagMult == True and flagEnd == True:
            k = 0
            for _ in range(much):
                x = int(input())
                if x % digitalMult == 0 and x % 10 == digitalEnd:
                    k += 1
        elif flagMult == True:
            k = 0
            for _ in range(much):
                x = int(input())
                if x % digitalMult == 0:
                    k += 1
        elif flagEnd == True:
            k = 0
            for _ in range(much):
                x = int(input())
                if x % 10 == digitalEnd:
                    k += 1
        result = k
    if flagSum == True and flagQuan == True:
        if "количество введёных чисел" in Task:
            if flagMult == True and flagEnd == True:
                k, sum1 = 0, 0
                for _ in range(much):
                    x = int(input())
                    if x % 10 == digitalEnd and x % digitalMult:
                        sum1 += x
                    k += 1
            elif flagMult == True:
                k, sum1 = 0, 0
                for _ in range(much):
                    x = int(input())
                    if x % digitalMult == 0:
                        sum1 += x
                    k += 1
            elif flagEnd == True:
                k, sum1 = 0, 0
                for _ in range(much):
                    x = int(input())
                    if x % 10 == digitalEnd:
                        sum1 += x
                    k += 1
            result = [sum1, k]
    elif flagMax == True:
        if flagMult == True:
            max1 = -30001
            for _ in range(much):
                x = int(input())
                if x % digitalMult == 0 and x > max1:
                        max1 = x
        elif flagEnd == True:
            max1 = -30001
            for _ in range(much):
                x = int(input())
                if x % 10 == digitalEnd and x > max1:
                    max1 = x
        elif flagEnd == True and flagMult == True:
            max1 = -30001
            for _ in range(much):
                x = int(input())
                if x % 10 == digitalEnd and x % digitalMult == 0 and x > max1:
                    max1 = x
        result = max1
    elif flagMin == True:
        if flagMult == True:
            min1 = 30001
            for _ in range(much):
                x = int(input())
                if x % digitalMult == 0 and x < min1:
                        min1 = x
        elif flagEnd == True:
            min1 = 30001
            for _ in range(much):
                x = int(input())
                if x % 10 == digitalEnd and x < min1:
                    min1 = x
        elif flagEnd == True and flagMult == True:
            min1 = 30001
            for _ in range(much):
                x = int(input())
                if x % 10 == digitalEnd and x % digitalMult == 0 and x < min1:
                    min1 = x    
        result = min1
    return result   
def speed():
    pass 
def CodeFor(flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, digitalMult, digitalEnd):
    print("much = int(input())")
    if flagSum == True and flagQuan == True:
        print("sum1, k = 0, 0")
        print("for _ in range(much):")
        print("    x = int(input())")
        if flagEnd == True and flagMult == True:
            print("    if x % 10 ==", digitalEnd, "and", "x %", digitalMult, "== 0:")
            print("        sum1 += x")
            print("    k += 1")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, ":")
            print("        sum1 += x")
            print("    k += 1")
        elif flagMult == True:
            print("    if x %", digitalMult, "== 0:")
            print("        sum1 += x")
            print("    k += 1")
        print("print(sum1, k, sep='\n')")
    elif flagSum == True:
        print("sum1 = 0")
        print("for _ in range(much):")
        print("    x = int(input())")
        if flagEnd == True and flagMult == True:
            print("    if x % 10 ==", digitalEnd, "and", "x %", digitalMult, "== 0:")
            print("        sum1 += x")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, ":")
            print("        sum1 += x")
        elif flagMult == True:
            print("    if x %", digitalMult, "== 0:")
            print("        sum1 += x")
        print("print(sum1)")
    elif flagQuan == True:
        print("k = 0")
        print("for _ in range(much):")
        print("    x = int(input())")
        if flagEnd == True and flagMult == True:
            print("    if x % 10 ==", digitalEnd, "and x %", digitalEnd, "== 0:")
            print("        k += 1")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, ":")
            print("        k += 1")
        elif flagMult == True:
            print("    if x %", digitalMult, "== 0:")
            print("        k += 1")
        print("print(k)")
    elif flagMax == True:
        print("max1 = -30001")
        print("for _ in range(much):")
        print("    x = int(input())")
        if flagEnd == True and flagMult == True:
            print("    if x % 10 ==", digitalEnd, "and x %", digitalMult, "== 0: and x > max1")
            print("        max1 = x")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, "and x > max1:")
            print("        max1 = x")
        elif flagMult == True:
            print("    if x %", digitalMult, "== 0 and x > max1:")
            print("        max1 = x")
        print("print(max1)")
    elif flagMin == True:
        print("min1 = 30001")
        print("for _ in range(much):")
        print("    x = int(input())")
        if flagEnd == True and flagMult == True:
            print("    if x % 10 ==", digitalEnd, "and x %", digitalMult, "== 0 and x < min1:")
            print("        min1 = x")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, "and x < min1:")
            print("        min1 = x")
        elif flagMult == True:
            print("    if x %", digitalMult, "== 0 and x < min1:")
            print("        min1 = x")
        print("print(min1)")
def CodeWhile(flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, digitalMult, digitalEnd):
    print("x = int(input())")
    if flagSum == True and flagQuan == True:
        print("sum1, k = 0, 0")
        print("while x != 0:")
        if flagEnd == True and flagMult == True:
            print("    if x % 10 ==", digitalEnd, "and x %", digitalMult, "== 0:")
            print("        sum1 += x")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, ":")
            print("        sum1 += x")
        elif flagMult == True:
            print("    if x %", digitalMult, "== 0:")
            print("        sum1 += x")
        print("    k += 1")
        print("    x = int(input())")
        print("print(sum1, k, sep='\n')")
    elif flagSum == True:
        print("sum1 = 0")
        print("while x != 0:")
        if flagEnd == True and flagMult == True:
            print("    if x % 10 ==", digitalEnd, "and x %", digitalMult, "== 0:")
            print("        sum1 += x")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, ":")
            print("        sum1 += x")
        elif flagMult == True:
            print("    if x %", digitalEnd, "== 0:")
            print("        sum1 += x")
        print("    x = int(input())")
        print("print(sum1)")
    elif flagQuan == True:
        print("k = 0")
        print("while x != 0:")
        if flagEnd == True and flagMult == True:
            print("    if x % 10 ==", digitalEnd, "and x %", digitalMult, "== 0:")
            print("        k += 1")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, ":")
            print("        k += 1")
        elif flagMult == True:
            print("    if x %", digitalMult, "== 0:")
            print("        k += 1")
        print("    x = int(input())")
        print("print(k)")
    elif flagMax == True:
        print("max1 = -30001")
        print("while x != 0:")
        if flagEnd == True and flagMult == True:
           print("    if x % 10 ==", digitalEnd, "and x %", digitalMult, "== 0 and x > max1:")
           print("        max1 = x")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, "and x > max1:")
            print("        max1 = x")
        elif flagMult == True:
            print("    if x %", digitalMult, "== 0 and x > max1:")
            print("        max1 = x")
        print("    x = int(input())")
        print("print(max1)")
    elif flagMin == True:
        print("min1 = 30001")
        print("while x != 0:")
        if flagEnd == True and flagMult == True:
            print("    if x %", digitalMult, "== 0 and x % 10 ==", digitalEnd, "and x < min1:")
            print("        min1 = x")
        elif flagEnd == True:
            print("    if x % 10 ==", digitalEnd, "and x < min1:")
            print("        min1 = x")
        elif flagMult == True:
            print("    if x %", digitalMult, "== 0 and x < min1:")
            print("        min1 = x")
        print("    x = int(input())")
        print("print(min1)")
input("Здравствуйте")
Task = input("Пожалуйста введите задние ")
flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, digitalMult, digitalEnd = WhatItIs(Task)
#print(flagSum, flagQuan, flagEnd, flagMult, flagMin, flagMax, digitalMult, digitalEnd)
if "получает на вход количество чисел" in Task:
    result = decisionFor(flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, int(digitalMult), int(digitalEnd), Task)
    print("Код")
    CodeFor(flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, int(digitalMult), int(digitalEnd))
if "количество введённых чисел неизвестно" in Task:
    result = decisionWhile(flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, int(digitalMult), int(digitalEnd), Task)
    print("Код")
    CodeWhile(flagSum, flagQuan, flagEnd, flagMult, flagMax, flagMin, int(digitalMult), int(digitalEnd))
print("Результат", result, sep="\n")
#print(flagSum,flagEnd,flagMult,flagMin,flagMax,digitalMult,digitalEnd, sep="\n")
input("End Programm")