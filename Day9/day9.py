import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

clear = lambda: os.system('clear')

exit = False

blind = {}
max_bid = 0
max_bid_name = ""

while not exit:
    name = input("What is your name ? - ")
    bid = int(input("How bid you want : $"))

    blind[name] = bid
    print(blind)

    another_person = input("There are any person : 'Yes' or 'No' - ")

    if another_person != "Yes":
        exit = True

        for b in blind:
            if blind[b] > max_bid:
                max_bid = blind[b]
                max_bid_name = b
    
        print(max_bid_name)
    else:
        clear()
