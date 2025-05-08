import math
import turtle

def draw_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
        t.end_fill()
def get_color(depth, max_depth):
    if depth == 0:
        return (0.55, 0.27, 0.07)
    green_intensity = min(1.0, depth / max_depth)
    return (0.13, 0.55 * green_intensity, 0.13 * (1 - green_intensity))
def pythagoras_tree(t, size, depth, max_depth):
    if depth > max_depth:
        return
    color = get_color(depth, max_depth)
    draw_square(t, size, color)
    t.forward(size)
    t.left(45)
    new_size = size * math.sqrt(2) / 2
    pos1 = t.position()
    heading1 = t.heading()
    pythagoras_tree(t, new_size, depth + 1, max_depth)
    t.setheading(heading1)
    t.right(45)
    t.backward(size)
def main():
    try:
        depth = int(input("Введите уровень рекурсии (например, 10):"))
        size = float(input("Введите размер основания ( например, 100):"))
        if depth < 0 or size <= 0:
            raise ValueError("Уровень рекурсии должен быть > = 0, размер > 0")
        
        screen = turtle.Screen()
        screen.title("Дерево Пифагора")
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(0, -200)
        t.pendown()
        t.left(90)

        pythagoras_tree(t, size, 0, depth)

        screen.getcanvas().postscript(file ="pythagoras_tree.eps")
        print("Фрактал сохранен как 'pythagoras_tree.eps")

        screen.exitonclick()

    except ValueError as e:
        print(f"ошибка: {e}")

if __name__ == "__main__":
    main()
    