# The difference between tuple to list that we can`t change "format" like we can`t add or delete elements
# if created tuple with 1 element need to add comma , else it will be string
browsers = ("chrome", "edge", "safari")
print(browsers)
print(browsers[1])
print(browsers[-1]) # prints last element
for browser in browsers:
    print(browser, end=" , ")
print()
print(type(browsers))
print("number of elements: ", len(browsers))
# add element
browsers = browsers + ("firefox", )
print("the tuple browsers is: ", browsers)
