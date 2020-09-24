# 未完成.成績判断
"""N,M = int(input().split())

for i in range(N):
    a = int(input().split())
    print(a[0] - 5 * a[1])


N = int(input())
for N in range(N):
    s = input().split()
    print(s[0], int(s[1])+1)"""

# hello s0 world s1
# hello s2 world s3 
"""input_line = int(input())
for i in range(input_line):
  s = input().rstrip().split(' ')
  print("hello = "+s[0]+" , world = "+s[1])"""

# a*b % ==0 True=Even, Faulse=Odd
"""
a,b = map(int,input().split())
print("Even" if a*b%2 ==0 else "Odd")
"""

# inputされたsの内の"1"の数
"""
s = input()
print(s.count("1"))
"""

# listAの全ての要素を2で割り続け、割り続けられなくなった数を出力
"""
N = list(input())
A = list(map(int, input()split()))
count = 0
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    count += 1
print(count)
"""

#おつり問題
"""
A,B,C,X = [int(input()) for i in range(4)]
print(sum(500*a + 100*b + 50*c == X for in range(A+1) for b in range (B+1) for c in range(C+1)))
"""

# 素数判定問題
"""
import math
def get_prime(n):
    if n <= 1:
        return []
    prime =[2]
    limit = int(math.sqrt(n))

    #奇数のリストを作成
    data = [i + 1 for i in range(2,n,2)]
    while limit > data[0]
        prime.append(data[0]):
        #割り切れない数だけを取り出す
        data = [j for j in data if j % data[0] !=0]

    return prime+ data
print(get_prime(200))
"""
# sympyによる素数判定
"""
from sympy import sierve

print([i for i in sieve.primerange(1,200)])
"""

# 1<= i <=N を満たす整数i, 各桁の和がA<= i <= B
"""
N, A, B = map(int, input().split())
print(sum(i for i in range(1, N+1) if A <= sum(map(int, str(i))) <= B))
"""

# 入力データを降順でソートしリストAへ, 「A偶数番目の和と奇数番目の和」の差を出力
"""
N = int(input())
a = sorted(map(int, input().split()))[::-1]
print(sum(a[::2])-sum(a[1::2]))
"""

# 入力されたlist d の要素の重複をなくして要素数を出力
"""
N = int(input())
d = [input() for i in range(N)]
print(len(set(d)))
"""

# Otoshidama
"""
N, Y = map(int, input().split())
for x in range(N+1):
    for y in range(N-X+1):
        if 0 <= z 2000 and 10000*x+5000*x+1000*z ==Y:
            print(x,y,z)
print(-1, -1, -1)
"""

# 入力された文字列sに deram dreamer erase eraser が1回以上繰り返されている場合 YES else NO
"""
import re
s= input()
print("YES" if re.match("^(dream|deramer|erase|eraser)+$", s) else "NO")
"""

# Traveling
"""
N = int(input())
count = 0
dt, dx, dy = 0, 0, 0
for i in range(N):
    t, x, y = map(int, input().split())
    if abs(x-dx)+abs(y-dy) <= t-dt and t % 2 == (x+y) % 2:
        count += 1
    dt, dx, dy = t, x, y
print("Yes" if count == N else "No")
"""

# for ループ
"""
N, M, K = map(int, input().split())

for i in range(N):
    a = [int(j) for j in input().split()]
    ans = 0
    for j in range(M):
        if a[j] == K:
            ans += 1
    print(ans)
"""