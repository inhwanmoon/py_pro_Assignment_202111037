#def get_fixed_price():
    #y = int(input('A상품의 할인된 가격은? '))
    #z = int(input('B상품의 할인된 가격은? '))
    #a = 100 * y // (100 -x)
    #b = 100 * z // (100 -x)
    #print('A 상품의 정가는',a,'원')
    #print('B 상품의 정가는',b,'원')


#x = int(input('할인율은? '))
#get_fixed_price()

def get_fixed_price(discounted_price, discount_rate):
    original_price = 100 * discounted_price // (100 -discount_rate)
    return original_price
    
discount_rate = int(input('할인율은? '))
discounted_price_A = int(input('A상품의 할인된 가격은? '))
discounted_price_B = int(input('B상품의 할인된 가격은? '))

original_price_A = get_fixed_price(discounted_price_A ,discount_rate)
original_price_B = get_fixed_price(discounted_price_B ,discount_rate)
print('A 상품의 정가는',original_price_A,'원')
print('B 상품의 정가는',original_price_B,'원')
