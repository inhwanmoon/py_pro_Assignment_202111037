def display_multiplication_table_all_horizontal():
   
    for i in range(1, 10):
        line1 = ""
        for dan in range(2, 6):
            line1 += f'{dan} x {i} = {dan * i}\t' 
        print(line1)

    print()  

    
    for i in range(1, 10):
        line2 = ""
        for dan in range(6, 10):
            line2 += f'{dan} x {i} = {dan * i}\t'  
        print(line2)


display_multiplication_table_all_horizontal()
