def read_number(n):
     n100 = n // 100
     N100=read_single_digit(n100)
     n10 = n % 100 // 10
     N10=read_single_digit(n10)
     n1 =  n % 100 % 10
     N1=read_single_digit(n1)
     return f'{N100} {N10} {N1}'

def read_single_digit(n):
    if n== 1:
        return '일'
    elif n ==2:
        return '이'
    elif n == 3:
        return '삼'
    elif n == 4:
        return '사'
    elif n == 5:
        return '오'
    elif n == 6:
        return '육'
    elif n == 7:
        return '칠'
    elif n == 8:
        return '팔'
    elif n == 9:
        return '구'
    else:
        return '영'


number = int(input('세 자리 이하 정수 입럭: ' ))

if 0<= number <= 999:
    print(read_number(number))
else:
    print('세 자리 수 이하 10진 정수를 입력하세요.')
