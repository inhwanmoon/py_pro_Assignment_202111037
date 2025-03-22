def get_integer(prompt):
    res = int(input(prompt))
    return res

def exchange(coin):
    n500 = coin // 500
    coin %= 500
    n100 = coin // 100
    coin %= 100
    n50 = coin // 50
    coin %= 50
    n10 = coin // 10
    coin %= 10
    print('500원 동전의 개수: ', n500)
    print('100원 동전의 개수: ', n100)
    print('50원 동전의 개수: ', n50)
    print('10원 동전의 개수: ', n10)


money = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(money)
