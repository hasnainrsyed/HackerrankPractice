# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Score: 10

def wierd(n):
    if n % 2 == 1 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')
        
if __name__ == '__main__':
    n = int(input().strip())
    wierd(n)
