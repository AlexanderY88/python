from finale.circle import Circle
from finale.rectangle import Rectangle
from finale.right_triangle import RightTriangle
from finale.square import Square


def add_new_shape(shapes):
    print("Choose a shape to add:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Right Triangle")

    choice = int(input("Enter your choice (1-4): "))

    color = input("Enter the color of the shape: ")

    if choice == 1:
        width: float = float(input("Enter the width of the square: "))
        shapes.append(Square(color, width))
    elif choice == 2:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        shapes.append(Rectangle(color, width, height))
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        shapes.append(Circle(color, radius))
    elif choice == 4:
        width = float(input("Enter the width of the right triangle: "))
        height = float(input("Enter the height of the right triangle: "))
        shapes.append(RightTriangle(color, width, height))
    else:
        print("Invalid choice")


def list_all_shapes(shapes):
    for shape in shapes:
        print(f"{shape.__class__.__name__}: {shape.color}", end="")
        if isinstance(shape, Square):
            print(f", width={shape.width}")
        elif isinstance(shape, Rectangle):
            print(f", width={shape.width}, height={shape.height}")
        elif isinstance(shape, Circle):
            print(f", radius={shape.radius}")
        elif isinstance(shape, RightTriangle):
            print(f", width={shape.width}, height={shape.height}")


def sum_all_circumferences(shapes):
    total_circumference = sum(shape.calculate_circumference() for shape in shapes)
    print(f"Total circumferences: {total_circumference}")


def sum_all_areas(shapes):
    total_area = sum(shape.calculate_area() for shape in shapes)
    print(f"Total areas: {total_area}")


def find_biggest_circumference(shapes):
    max_circumference_shape = max(shapes, key=lambda x: x.calculate_circumference())
    max_circumference = max_circumference_shape.calculate_circumference()
    print(f"Shape with the biggest circumference: {max_circumference_shape.__class__.__name__} ({max_circumference})")


def find_biggest_area(shapes):
    max_area_shape = max(shapes, key=lambda x: x.calculate_area())
    max_area = max_area_shape.calculate_area()
    print(f"Shape with the biggest area: {max_area_shape.__class__.__name__} ({max_area})")


if __name__ == "__main__":
    shapes = []

    while True:
        print("\nMenu:")
        print("1. Add new shape")
        print("2. List all shapes")
        print("3. Sum all circumferences")
        print("4. Sum all areas")
        print("5. Find biggest circumference")
        print("6. Find biggest area")
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            add_new_shape(shapes)
        elif choice == 2:
            list_all_shapes(shapes)
        elif choice == 3:
            sum_all_circumferences(shapes)
        elif choice == 4:
            sum_all_areas(shapes)
        elif choice == 5:
            find_biggest_circumference(shapes)
        elif choice == 6:
            find_biggest_area(shapes)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
