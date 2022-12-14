display = input('Press enter to continue.')
name = input('Enter your name \n')
student_id = input('Enter your student id \n')
room_no = input('Enter your room no \n')
print('------------------Welcome to the Akshay Supermarket------------------')
print()

menu = ['Dettol handwash', 'Patanjali handwash', 'Dettol soap', 'Dove soap', 'Santoor soap', 'Toothbrush', 'Shampoo', 'Floor cleaner', 'Detergent', 'Lays chips', 'Too yum', 'Oreo biscuit', 'Hajmola', 'Rice', 'Maggie', 'Hot ramen', 'ParleG biscuit', 'Weighing machine', 'Battery', 'Wall clock', 'Trimmer', 'Charger']
sector = [ 'Toiletry ', 'Toiletry ', '        Toiletry ', '        Toiletry ', '        Toiletry ', '        Toiletry ', '        Toiletry ', 'Toiletry ', '        Toiletry ', '        Food     ', '        Food     ', 'Food     ', '        Food     ', '        Food     ', '        Food     ', '        Food     ', 'Food     ','electronic', '        electronic', '        electronic', '        electronic', '        electronic']
price = [50, 60, 40, 80, 70, 110, 77, 55, 90, 39, 74, 98, 107, 35, 55, 209, 67 ,24, 56, 90, 40, 250]
print('ITEM', 'SECTOR', 'PRICE (INR), excl. Tax', sep='\t\t\t\t\t\t')
print()
for kk in range(len(menu)):
    print(str(kk+1)+'. '+menu[kk], sector[kk], price[kk], sep='\t\t\t\t\t')

print()   
search = 0
while search==0:
    product = (input('Which item do you want to search?,or type 0 for exiting search option\n'))

    if product.capitalize() in menu:
        print('The item no. of ' + product + ' is ' + str(menu.index(product.capitalize())))
    else:
        print('Item not found') 
        search = 1

shopping_cart = [] 
shopping_quant= []
shopping_complete = 0

while shopping_complete==0:

    order = int(input('Enter 1 to 22 to select an item, 23 to proceed to checkout.\n')) 
    
   
    
    if order <= 22:
    
        print('You selected', menu[order-1])
        quant = int(input('How many units do you wish to purchase?\n'))

    
        if menu[order-1] in shopping_cart:
            idx = shopping_cart.index(menu[order-1])
            shopping_quant[idx]+=quant
        else:
            shopping_cart.append(menu[order-1])        
            shopping_quant.append(quant)        
        
        print('Added to shopping cart:', quant, 'units of', menu[order-1])
    elif order == 23:
        shopping_complete = 1
    else: 
        print("Sorry that was not a valid input.")
     


item =input('enter the name of item you would like to remove from the shopping list.\n')
if item.capitalize() in shopping_cart:
    shopping_cart.remove(item.capitalize())
else:
    print('Item not found in your list')    


        
print()
print('Your Shopping Cart:')

grand_tot = 0.0
print('ITEM', 'QUANT', 'UNIT PRICE', 'TOTAL', sep='\t\t\t')    
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price=price[idx]
    tot_price = round(unit_price*shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

grand_tot = round(grand_tot, 2)
print()
print('Your total order is (INR)', grand_tot)

print()

next_500 = 500*(grand_tot//500+1)
gap_500 = next_500 - grand_tot



print()

print('If you purchase for (INR)', next_500, 'you will get a 10% discount', sep=' ')
discount_wanted = input('Would you like to take this offer? (y/n)')
add_quant=[]
if discount_wanted == 'y':
    print('You have the following options\n')
    for kk in range(len(menu)):
        add_quant.append((int(gap_500//price[kk]+1)))
        print(str(kk+1), '. Add', menu[kk], str(add_quant[kk]), 'units')
    
    add_on = int(input('Please indicate your preference\n'))

    if menu[add_on-1] in shopping_cart:
        idx = shopping_cart.index(menu[add_on-1])
        shopping_quant[idx]+=add_quant[add_on-1]
    else:
        shopping_cart.append(menu[add_on-1])        
        shopping_quant.append(add_quant[add_on-1])        

    print('shopping cart updated')
    print('Proceed to checkout')    
else:
    print('Proceed to checkout')

grand_tot = 0.0
print('ITEM', 'QUANT', 'UNIT PRICE', 'TOTAL',sep='\t\t\t\t')    
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price=price[idx]
    tot_price = round(unit_price*shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price,sep='\t\t\t\t')

print()

dct_rate = 10.0; 
tax_rate = 10.0; 

if discount_wanted == 'y':
    discount = round(dct_rate/100.0*grand_tot, 2)
else:
    discount = 0.0; 

tax = round(tax_rate/100.0*(grand_tot-discount), 2)

print(student_id.upper())
print(name.upper())
print(room_no.upper())
print('Your total order is (INR)', grand_tot)
print('Discount (10%) is (INR)', discount)
print('Your order value, after discount is (INR)', round(grand_tot-discount, 2))
print('Tax (10%) is (INR)', round(tax, 2)); 
print('Total you have to pay (INR) ', round(grand_tot - discount + tax, 2))

print('Thanks')
print('Bye')

# I am unable to create admin login at the moment ,so i did this 'discount wanted' and 'tax rate' thing that i learned previously.
