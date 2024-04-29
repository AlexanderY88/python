# functions  checks the browser color:
def get_browser_color(value) -> str:
    lowercase_browser = value.lower()

    if "firefox" in lowercase_browser:
        return "blue"
    elif "chrome" in lowercase_browser:
        return "red"
    elif "edge" in lowercase_browser:
        return "yellow"
    else:
        return "green"


# function takes input: browser name, and checks the color
def print_browser_color():
    browser_name = input("Enter the browser name: ")
    color = get_browser_color(browser_name)
    print(f"The browser name is {browser_name.lower()}, the color is: {color}")

print_browser_color()