print("Masukkan kalimat: ")
text = input()

chk = 0
countWord = 0
textLen = len(text)

for i in range(textLen):
    if text[i]==' ':
        if chk!=0:
            countWord = countWord+1
        chk = 0
    else:
        chk = chk+1

if chk!=0:
    countWord = countWord+1

def c_word(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(c_word(text))
print("\nTotal kata: ", countWord)
print("Kata unik: ",)