def buy(shopping_bag_dict):
    
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        return False
    try:
        amount = int(input('수량은? '))
        shopping_bag_dict[item] = shopping_bag_dict.get(item, 0) + amount
        print(f'장바구니에 {item} {amount}개가 담겼습니다.\n')
        return True
    except ValueError:
        print("수량은 숫자로 입력해야 합니다. 다시 시도해주세요.\n")
        return True

def show(shopping_bag_dict):
    
    print(f'>>> 장바구니 보기: {shopping_bag_dict}')

def find(shopping_bag_dict):
   
    print('[검색]')
    ask = input('장바구니에서 확인하고자 하는 상품은? ')
    if ask in shopping_bag_dict:
        count = shopping_bag_dict[ask]
        print(f'{ask}은(는) {count}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {ask}은(는) 없습니다.')


shopping_bag = {}
while True:
    if not buy(shopping_bag):
        break
show(shopping_bag)
find(shopping_bag)
