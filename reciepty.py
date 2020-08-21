import os
import sys
import json
def test():
    print('Welcome to receipty, a CLI receipt saving program with dozens of useful features to interact with your receipts!')
    print('Would you like to either [1], save a receipt, or [2], check your receipt database, or [3], exit the program')
    x = input()
    if x == '3': #
        sys.exit()
    if x == '[3]':
        sys.exit()
    if x == '1':
        print("Please enter receipt info below.")
        print('What is the total price of all items on your receipt?')
        total_receipt_price = input()
        print('How many items do you have on your receipt?')
        total_receipt_items = input()
        if int(total_receipt_items) < 5:
            print('Please enter the names and prices of your 4 or less items.')
            print('What is the name of item one?')
            item_one_name = input()
            print('How much did item one cost?')
            item_one_price = input()
            print('Is that all you are saving to the receipt database?')
            receipt_answer = input()
            if receipt_answer == 'yes':
                sys.exit()
            if receipt_answer == 'yes':
                sys.exit()
            else:
                os.system('python reciepty.py')
            # Data to be written
            if int(total_receipt_items) > 5:
                print('Please enter the names and prices of your 5 or more items.')
                print('What is the name of item one?')
                item2_one_name = input()
                print('What is the price of item one?')
                item2_one_price = input()
                print('Is that all you are saving to the receipt database?')
                receipt2_answer = input()
            if receipt2_answer == 'yes':
                sys.exit()
            if receipt2_answer == 'YES':
                sys.exit()
            if receipt2_answer == 'Yes':
                sys.exit()
            else:
                os.system('python reciepty.py')
    if x == '[1]':
        print("Enter receipt info below...")
        print('What is the total price of all items on your receipt?')
    if x == '2':
        print('The price for your last item is')
        with open('C:/Users/username/Downloads/receipty/database.json') as jsonfile:
            data = json.load(jsonfile)
            print(data["item_one_price"])
    if x == '[2]':
        print('Loading receipt database...')
test()
