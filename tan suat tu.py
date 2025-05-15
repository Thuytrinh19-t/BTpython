from collections import defaultdict

n = int(input())

word_count = defaultdict(int)

for _ in range(n):
    line = input().strip().split()
    for word in line:
        word_count[word] += 1


sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word, count)
