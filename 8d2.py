word = input("Введите слово: ").upper()
score = 0
for letter in word:
    if letter in "АВЕИНОРСТ":
        score += 1
    elif letter in "ДКЛМПУ":
        score += 2
    elif letter in "БГЁЬЯ":
        score += 3
    elif letter in "ЙЫ":
        score += 4
    elif letter in "ЖЗХЦЧ":
        score += 5
    elif letter in "ШЭЮ":
        score += 8
    elif letter in "ФЩЪ":
        score += 10
print(f"Стоимость слова: {score} очков.")