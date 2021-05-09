import sys
words = ["Practice", "makes", "perfect", "coding", "makes"]
#words = list(input().split(" "))
word1 = input()
word2 = input()
minimun = sys.maxsize
for i in range(len(words)):
    if words[i] == word1:
        for j in range(len(words)):
            if words[j] == word2:
                if (abs(i-j)<minimun):
                    minimun = abs(i-j)
print(minimun)
