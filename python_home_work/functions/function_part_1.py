# to create function it starts with word: def
def print_menu(is_child):
    print("*** Italian kitchen ***")
    print("Please Choose from the menu:")
    print("1. Pizza")
    print("2. Salad")
    if is_child:  # means like: is_child = True
        print("3. Water")
        print()
    else:  # means like: (else) is_child = False
        print("3. Wine")
        print()


print_menu(True)
print_menu(False)


