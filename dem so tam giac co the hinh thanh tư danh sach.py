from itertools import combinations

def count_triangles(sides):
    sides.sort()
    count = 0
    n = len(sides)
    # Duyệt tất cả các bộ ba cạnh
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a, b, c = sides[i], sides[j], sides[k]
                if a + b > c and a + c > b and b + c > a:
                    count += 1
    return count

# Đọc dữ liệu vào
def main():
    t = int(input())
    for _ in range(t):
        sides = list(map(int, input().split()))
        print(count_triangles(sides))

if __name__ == "__main__":
    main()
