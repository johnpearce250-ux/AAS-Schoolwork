from polygon_area_calculator import Rectangle, Square

def main():
    r = Rectangle(4, 3)
    s = Square(5)

    print(r)                # Rectangle(width=4, height=3)
    print('Area:', r.get_area())
    print('Perimeter:', r.get_perimeter())
    print('Diagonal:', r.get_diagonal())
    print(r.get_picture())

    print(s)                # Square(side=5)
    print('Square area:', s.get_area())

if __name__ == '__main__':
    main()
