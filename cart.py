from IPython.display import clear_output as co


def rules():
    print("""Type 'add' to add item to cart.
Type 'remove' to remove item from cart.
Type 'view' to view cart in cart.
Type 'end' to end cart sim.""")
    print("="*50)


class Cart:
    def __init__(self):

    def Cart_list(self):
        input('Welcome, press any key to begin. ')
        print("="*50)

        cart = []
        done = False

        while not done:
            co()

            rules()

            choice = input(
                "What is your choice? add | view | remove | end ")
            if choice == 'add':
                item_name = input("Type in item to add. ")

                item_dictionary = {
                    'item_name': item_name,
                }

                cart.append(item_dictionary)

            elif choice == 'view':
                for item in cart:
                    print(item)
                input('Press any key to continue')
            elif choice == 'remove':
                item_name = input("What would you like to remove? ")
                cart = [i for i in cart if not (i['item_name'] == item_name)]
            elif choice == 'end':
                confirm = input('Are you sure you want to quit? yes/no? ')
                if confirm == 'yes':
                    done = True
                elif confirm == 'no':
                    continue

        print(item)


my_cart = Cart(0)
