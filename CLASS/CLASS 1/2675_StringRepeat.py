# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
#
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 예제 입력 1
# 2
# 3 ABC
# 5 /HTP
# 예제 출력 1
# AAABBBCCC
# /////HHHHHTTTTTPPPPP

p=""
num = int(input())

for i in range(num):
    n,s = input().split()
    for j in range(len(s)): #문자열의 길이만큼 반복
        p+=s[j]*int(n)
    print(p)
    p=""

