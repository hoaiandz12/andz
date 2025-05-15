
import turtle

# Khởi tạo màn hình
screen = turtle.Screen()
screen.title("Điều khiển Rùa bằng phím mũi tên")
screen.bgcolor("white")


# Khởi tạo con rùa
t = turtle.Turtle()
t.speed(0)  # Tốc độ nhanh nhất
t.shape("turtle")  # Hình dạng rùa
t.color("green")  # Màu xanh lá
t.penup()
# Khoảng cách di chuyển mỗi lần nhấn phím
MOVE_DISTANCE = 10
TURN_ANGLE = 45

# Định nghĩa các hàm di chuyển
def move_forward():
    t.forward(MOVE_DISTANCE)

def move_backward():
    t.backward(MOVE_DISTANCE)

def turn_left():
    t.left(TURN_ANGLE)

def turn_right():
    t.right(TURN_ANGLE)

# Thiết lập phím điều khiển
screen.onkey(move_forward, "Up")    # Phím mũi tên lên
screen.onkey(move_backward, "Down") # Phím mũi tên xuống
screen.onkey(turn_left, "Left")    # Phím mũi tên trái
screen.onkey(turn_right, "Right")  # Phím mũi tên phải

# Cho phép màn hình lắng nghe sự kiện bàn phím
screen.listen()

# Giữ cửa sổ hiển thị
screen.mainloop() 