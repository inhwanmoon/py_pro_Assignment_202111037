shopping_bag = []
d = {}
print('[구입]')

while True:
    item = input('상품명? ')
    if item == '':
        print(f'\n장바구니 보기:{d}\n')
        print('[검색]')
        ask = input('장바구니에서 확인하고자 하는 상품은? ')
        if ask in d:
            count = d[ask]
            print(f'{ask}은(는) {count}개 담겨 있습니다.')
        break
    amount = int(input('수량은? '))
    shopping_bag.append(item)
    d[item] = amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.\n')



