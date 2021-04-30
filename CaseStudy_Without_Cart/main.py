from product import Product
from search import Search
from order import Order

# p = Product.productRepository()
# s = Search.search(p)
# Search.displayBrand(s)
# Order.placeOrder(s)

class Main():
    def Sys():  
        p = Product.productRepository()
        s = Search.search(p)
        Search.displayBrand(s)

        if len(s) != 0:
            try:
                decide = str(input("Do you wish to purchase (y/n) : "))
                if decide == 'y':
                    Order.placeOrder(s)
                
                elif decide == 'n':
                    print("Thanks for visiting")
                else:
                    raise ValueError
            except ValueError:
                print("Wrong Choise")
    
    
Main.Sys()
