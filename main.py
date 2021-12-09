import keyboard as keyboard
import random

keyboard.block_key("ctrl")
keyboard.block_key("alt")
keyboard.block_key("esc")
random.seed(version=2)

print("Введите размер матрицы (от 2 до 5): ", end="")
while True:
    M = input()
    if M == "2" or M == "3" or M == "4" or M == "5":
        M = int(M)
        break
    else:
        print("Неверный ввод. Введите число от 2 до 5: ", end="")

a = [["" for _ in range(M)] for _ in range(M)]

print("Ввести строки с клавиатуры (0) или задать автоматически(1): ", end="")
while True:
    an = input()
    if an == "0" or an == "1":
        an = int(an)
        break
    else:
        print("Неверный ввод. Введите 0 или 1: ", end="")



if an == 0:
    print("Введите слова, состоящие из четырех букв английского алфавита: ", end="")
    for i in range(M):
        for j in range(M):
            while True:
                flag = True
                temp = input()
                if len(temp) != 4:
                    print("Неверная длина. Введите слово повторно: ", end="")
                    continue
                for c in temp:
                    if not(c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z'):
                        print("Обнаружена символ, не являющийся буквой английскиго алфавита. Введите слово повторно: ", end="")
                        flag = False
                        break
                if flag:
                    a[i][j] = temp
                    break

else:
    for i in range(M):
        for j in range(M):
            for _ in range(4):
                if random.randint(0, 1) == 1:
                    a[i][j] += chr(ord('a') + int(random.randint(0,25)))
                else:
                    a[i][j] += chr(ord('A') + int(random.randint(0, 25)))

print("Введите букву английского алфавита, с которой будут искаться слова: ", end="")
while True:
    l = input()
    if len(l) == 1 and (l >= 'a' and l <= 'z' or l >= 'A' and l <= 'Z'):
        break
    else:
        print("Неверный ввод. Введите букву английского алфавита повторно: ", end="")

ans = []
for i in range(M):
    for j in range(M):
        if a[i][j].lower().find(l.lower()) != -1:
            ans.append(a[i][j])

for i in range(len(ans)):
    for j in range(i, len(ans)):
        c1, c2 = 0, 0
        for g1 in ans[i]:
            if "aeiouy".find(g1.lower()) != -1:
                c1 += 1
        for g2 in ans[j]:
            if "aeiouy".find(g2.lower()) != -1:
                c2 += 1
        if c1 > c2:
            ans[i], ans[j] = ans[j], ans[i]

for i in range(len(ans)):
    print(ans[i], end=' ')