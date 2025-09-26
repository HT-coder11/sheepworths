"""
Advanced Shopping Cart
You're coding a CLI shopping cart for 

a - Add to cart  
r - Remove from cart  
u - Update quantity  
v - View cart  
c - Clear cart  
q - Checkout & quit

1- Add to cart (a)

Display all products with indices, names, prices, and stock.

Prompt for a product index (0-4) and desired quantity.

If the index is invalid or quantity > available stock, print an error and return to the menu.

Otherwise:

If the item is already in the cart, increase its quantity (but don't exceed stock).

Else, use .append() to add the name to cart_items and the quantity to cart_quantities.

Subtract the quantity from product_stock.

If total bill amount is more than 150 then you get 10% discount.

----> example 
> a
Products:
0: T-shirt   $20.0   stock 10
1: Jeans     $50.0   stock 5
2: Sneakers  $100.0  stock 3
3: Cap       $15.0   stock 20
4: Socks     $5.0    stock 30

Enter product index: 0
Enter quantity: 6
Added 6 x T-shirt.
"""







# 1 - Import packages, libraries 
import pygame, pygwidgets, sys


# 2 - Define constants
BGCOLOR = (240, 243, 189)
TEXTCOLOR = (26, 26, 26)
BUTTONCOLOR = (2, 128, 144)
OVERBUTTONCOLOR = (2, 195, 154)
FPS = 30
ERRORMSG = (255,0,0)
MSG = (5, 102, 141)
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
WHITE = (255,255,255)

# 3 - Initialise the world
pygame.init()
pygame.display.set_caption("sheepworths")
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets - Images/Sounds

# 5 - Initialise Variables

total_bill_amount = 0
TITLECARd = pygwidgets.DisplayText(window, (440,20), "Woolworths", fontSize= 40, textColor= TEXTCOLOR,fontName= "trebuchetms")
robloxhdadmin_btn = pygwidgets.TextButton(window, (30,20), "Admin Mode", fontSize= 18, textColor=TEXTCOLOR, upColor=BUTTONCOLOR, overColor=OVERBUTTONCOLOR, width=130,fontName= "trebuchetms")
product_panel = pygame.Rect(20,270,300,400)
cart_panel = pygame.Rect(770,270,300,400)
products_title = pygwidgets.DisplayText(window, (100,280), "Products", fontSize = 25,textColor=TEXTCOLOR,fontName= "trebuchetms")
cart_title = pygwidgets.DisplayText(window, (850,280), "Cart Items", fontSize = 25,textColor=TEXTCOLOR,fontName= "trebuchetms")
item_index_text = pygwidgets.DisplayText(window, (95,80), "Item Index", fontSize = 22,textColor=TEXTCOLOR,fontName= "trebuchetms")
item_input = pygwidgets.InputText(window, (45, 120), textColor=TEXTCOLOR, backgroundColor=OVERBUTTONCOLOR, width=240, fontSize=18,fontName= "trebuchetms")
add_to_cart_btn = pygwidgets.TextButton(window, (20,170), "Add to Cart", fontSize= 18, textColor=TEXTCOLOR, upColor=BUTTONCOLOR, overColor=OVERBUTTONCOLOR, width=130,fontName= "trebuchetms")
removefromcart_btn = pygwidgets.TextButton(window, (160,170), "Remove from Cart", fontSize= 18, textColor=TEXTCOLOR, upColor=BUTTONCOLOR, overColor=OVERBUTTONCOLOR, width=150,fontName= "trebuchetms")
item_quantity_text = pygwidgets.DisplayText(window, (850,80), "Item Quantity", fontSize = 22,textColor=TEXTCOLOR,fontName= "trebuchetms")
quantity_input = pygwidgets.InputText(window, (795, 120), textColor=TEXTCOLOR, backgroundColor=OVERBUTTONCOLOR, width=240, fontSize=18,fontName= "trebuchetms")
clearCart_btn = pygwidgets.TextButton(window, (780,170), "Clear Cart", fontSize= 18, textColor=TEXTCOLOR, upColor=BUTTONCOLOR, overColor=OVERBUTTONCOLOR, width=130,fontName= "trebuchetms")
checkout_btn = pygwidgets.TextButton(window, (920,170), "Checkout", fontSize= 18, textColor=TEXTCOLOR, upColor=BUTTONCOLOR, overColor=OVERBUTTONCOLOR, width=130,fontName= "trebuchetms")
errMes = pygwidgets.DisplayText(window, (330,380), "", fontSize = 20,textColor=ERRORMSG,fontName= "trebuchetms")
Message = pygwidgets.DisplayText(window, (330,530), "", fontSize = 20,textColor=MSG,fontName= "trebuchetms")
total_bill_text = pygwidgets.DisplayText(window, (780, 640), f"Total Bill : {total_bill_amount}", fontName="comicsansms", fontSize=18, textColor=TEXTCOLOR)
nextcustomerdudeleavenowplease = pygwidgets.TextButton(window, (500,630), "Bill Paid", textColor=TEXTCOLOR, fontName="trebuchetms", fontSize=20)
nextcustomerdudeleavenowplease.hide()

product_items   = ["T-shirt", "Jeans", "Sneakers", "Cats", "Socks"]
product_quantities  = [     10,       5,         3,     1053,      30] 
product_prices  = [   20.0,     50.0,      100.0,   500.0,    5.0]
product_text = []

cart_items      = []
cart_quantities = []
cart_prices = []
cart_text = []
cart_totals = []


item_index = 0
quantity = 0


def main():
    # 6 - Look forever
    while True:

        # 7 - check and handle for events
        for event in pygame.event.get():
            # Clicked the close button? Quit pygame and end program 
            if event.type == pygame.QUIT:           
                pygame.quit()  
                sys.exit()

            if item_input.handleEvent(event):
                pass
    
            if quantity_input.handleEvent(event):
                pass
            
            if add_to_cart_btn.handleEvent(event):
                errMes.setText("")
                Message.setText("")
                try:
                    print("in try")
                    item_index = int(item_input.getValue())
                    quantity = int(quantity_input.getValue())
                    add_to_cart(item_index,quantity)
                    
                except ValueError:
                    print("in except")
                    errMes.setText("Item Index and Quantity MUST BE numbers")
                item_index=0
                quantity = 0
                quantity_input.clearText()
                item_input.clearText()
               

                
            if removefromcart_btn.handleEvent(event):
                errMes.setText("")
                Message.setText("")
                try:
                    item_index = int(item_input.getValue())
                    quantity = int(quantity_input.getValue())
                    remove_cart(item_index,quantity)
                except:
                    errMes.setText("Item Index and Quantity MUST BE numbers")
                quantity_input.setText("")
                item_input.setText("")

            if nextcustomerdudeleavenowplease.handleEvent(event):
                clear_cart()  
                Message.setText("Your turn now the other guy left")
                nextcustomerdudeleavenowplease.hide()


            if clearCart_btn.handleEvent(event):
                clear_cart()

            if checkout_btn.handleEvent(event):
                total_bill_amount=sum(cart_totals)
                checkout_thing(total_bill_amount)

            
        



        


        # 8 - Do any "per frame" actions
        product_text.clear()
        cart_text.clear()
        cart_totals.clear()
        
        for i in range(len(product_items)):
            y = 330 + (i*30)
            txt = pygwidgets.DisplayText(window, (62, y), f"{i}: {product_items[i]} - ${product_prices[i]} [ {product_quantities[i]} Left ]", fontSize=18,fontName= "trebuchetms")
            product_text.append(txt)
            i+=1

        # for loop to show cart items example : f"{i} : {items} - ${price} X {stock}
        for i in range(len(cart_items)):
            y = 330 + (i*30)
            line_total = cart_prices[i]*cart_quantities[i]
            txt = pygwidgets.DisplayText(window, (800,y), f"{i}: {cart_items[i]} - ${cart_prices[i]} x {cart_quantities[i]} = ${cart_prices[i]*cart_quantities[i]}", fontSize=18, fontName="trebuchetms")
            cart_totals.append(line_total)
            cart_text.append(txt)
            i+=1

        total_bill_amount=sum(cart_totals)
        total_bill_text.setText(f"Total Bill: ${total_bill_amount}")

        # 9 - Clear the window 
        window.fill(BGCOLOR)


        # 10 - Draw all window elements

        pygame.draw.rect(window, WHITE, product_panel)
        pygame.draw.rect(window, WHITE, cart_panel)
        TITLECARd.draw()
        robloxhdadmin_btn.draw()
        products_title.draw()
        cart_title.draw()
        item_index_text.draw()
        item_input.draw()
        add_to_cart_btn.draw()
        removefromcart_btn.draw()
        item_quantity_text.draw()
        checkout_btn.draw()
        clearCart_btn.draw()
        quantity_input.draw()
        errMes.draw()
        Message.draw()
        nextcustomerdudeleavenowplease.draw()
        total_bill_text.draw()
        for txt in product_text:
            txt.draw()
        for txt in cart_text:
            txt.draw()


        # 11 - Update the window
        pygame.display.update()

        # 12 - Slow things down
        clock.tick(FPS)
        



def add_to_cart(item_index,quantity):
  

    if item_index < 0 or item_index >= len(product_items): 
        errMes.setText("Invalid Item Index ¥50")
        return
        
    if quantity <= 0:
        errMes.setText("Quantity must be bigger than 0")
        return
        
    if quantity > product_quantities[item_index]:
        errMes.setText("Not enough stock.")
        return
    
    # if the item is already in my cart and i add more of the same item then it should add onto the previous amount of items
    if product_items[item_index] in cart_items:
        e = cart_items.index(product_items[item_index])
        cart_quantities[e] += quantity
       
    else :
        # add the product name in cart items, product quantity in cart_quantities, price in cart_price
        cart_items.append(product_items[item_index])
        cart_quantities.append(quantity)
        cart_prices.append(product_prices[item_index])
    
    product_quantities[item_index] = product_quantities[item_index] - quantity
    

    errMes.setText("")
    
    # Added 100 Apples to your cart
    Message.setText(f"Added {quantity} {product_items[item_index]} to your cart")
    


    

def remove_cart(item_index,quantity): #item_index = 0 , quantity = 5

    # product_items = ["dogs", "snakes", "cats"]
    # product_quantities = [20,10,30]
    
    # cart_items = ["cats", "dogs"]
    # cart_quantities = [ 5,50] #5 cats removed
    # cart_items[item_index] = cats

    #validation 1 - check if item_index is less than length cart_items

    if item_index < 0 or item_index >= len(cart_items):
        errMes.setText("Invalid item index :'(")
        return

    #validation 2- check if quantities > cart_quantities[item_index]

    if quantity > cart_quantities[item_index]:
        errMes.setText(f"You dont have {quantity} {cart_items[item_index]} in your cart :'(")
        return

    #validation 3 - check if quantity is matching with cart_quantities[item_index]
    idx = product_items.index(cart_items[item_index])
    if quantity == cart_quantities[item_index]:
        cart_items.pop(item_index)
        cart_quantities.pop(item_index)
        cart_prices.pop(item_index)
        product_quantities[idx] = product_quantities[idx] + quantity


    else:
        cart_quantities[item_index] = cart_quantities[item_index] - quantity
        product_quantities[idx] = product_quantities[idx] + quantity

    


def clear_cart():

    for i in range(len(cart_items)):
        name = cart_items[i]
        quantity = cart_quantities[i] 
        product_index = product_items.index(name) #product_names.index("cats")
        product_quantities[product_index] += quantity


    cart_items.clear()  
    cart_quantities.clear()
    cart_prices.clear()
    cart_text.clear()
    line_total = 0
    errMes.setText("")
    Message.setText("Cart is clear!")




    
def checkout_thing(total_bill_amount):
    if total_bill_amount >= 150:
        discount = total_bill_amount*0.1
        total_bill_amount = total_bill_amount*0.9
        Message.setText(f"Total Bill To Be Paid After 10% DISCOUNT (${discount}): ${total_bill_amount}")
        nextcustomerdudeleavenowplease.show()
        
    else:
        Message.setText(f"Total Bill To Be Paid: ${total_bill_amount}! leave")
        nextcustomerdudeleavenowplease.show()


"""
if there was 10% discount then show text as 
Total bill to be paid after 10% DISCOUNT ($BLA) : &BLA
if there no discount then show text as 
Total bill to be paid : &BLA
"""

main()


#Homework : Make the nextcustomerdudeleavenowplease hidden all time and when checkput is called, show it.
# when that button is clicked, you remove all cart data and var resets. 
