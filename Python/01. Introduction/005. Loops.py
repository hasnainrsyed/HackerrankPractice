# Problem: https://www.hackerrank.com/challenges/python-loops/problem
# Score: 10


if __name__ == '__main__':
    n = int(input())
    print(*[num**2 for num in range(n)], sep='\n')