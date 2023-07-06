# ფაიგეიმის მოდულიდან ყველაფრის ინდივიდუალურად შემოტანა
from pygame import *
# from pygame import mixer
# ფაიგეიმის ინიციაცია
init()
#საათის შექმნა თამაშის მთავარი ციკლის სიხშირის გასაკონტროლებლად
clock = time.Clock()
# სიხშირე
fps = 30
#ეკრანის მონაცემების მოთხოვნა
info = display.Info()

icon = image.load("images/car.png")
display.set_icon(icon)
display.set_caption("driving cars!")
# თამაშის ეკრანის ზომების მორგება კომპის ეკრანის ზომებზე
width = info.current_w
height = info.current_h

screen = display.set_mode((width, height))

proportion = 840 / 650
background = image.load("images/road.png")
background = transform.scale(background, (width, height))
#
# differance = width - background.get_width()

# scroll = 0

# მოთამაშის კლასი
class Player:
    #კონსტრუქტორი
    def __init__(self, x, y, name):
        self.size = int(width / 8)
        self.image = image.load("images/car1.png")
        self.image = transform.scale(self.image, (self.size, self.size))
        self.rect = Rect(x, y, self.size, self.size)
        self.speed = 10
        self.speed_x = 0
        self.speed_y = 0
        self.name = name
    # დახატვის ფუნქცია
    def draw(self):
        # draw.rect(screen, (200, 100, 100), self.rect)
        screen.blit(self.image, self.rect)
    # მოძრაობის ფუნქცია
    def move(self):
        # მოძრაობის კოდი
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y
        # ეკრანიდან გასვლის აკრძალვის კოდი
        if self.rect.centerx < self.size / 2:
            self.rect.centerx = self.size / 2

        if self.rect.centerx > width - self.size / 2:
            self.rect.centerx = width - self.size / 2

        if self.rect.centery < self.size / 2:
            self.rect.centery = self.size / 2

        if self.rect.centery >height - self.size / 2:
            self.rect.centery = height - self.size / 2


    # კლავიატურის კონტროლი (სიჩქარეების ცვლილება)
    def controls(self):
        keys = key.get_pressed()
        # სიჩქარეების განულება როცა არ ვაჭერთ კნოპს
        self.speed_x = 0
        self.speed_y = 0
        # სიჩქარეების ცვლილება კნოპზე დაჭერის მიხედვით (ორი ფლეიერისთვის სხვადასხვა)
        if self.name == "rocket":
            if keys[K_d]:
                self.speed_x = self.speed
            if keys[K_a]:
                self.speed_x = -self.speed



    # ყველა საჭირო ფუნქციის ერთად გამოძახება
    def update(self):
        self.draw()
        self.controls()
        self.move()



# ობიექტების შექმნა
player1 = Player(700, 650, "rocket")



# მთავარი ციკლი
run = True
while run:
    clock.tick(fps)
    screen.blit(background, (0, 0))
    # for i in range(0, 2):
    #     screen.blit(background, (i * background.get_width() + scroll, 0))
    # scroll -= 5
    # if scroll <= differance:
    #     scroll = 0
    # screen.fill((100, 200, 100))
    # ობიექტების აფდეითი
    player1.update()



    for ev in event.get():
        if ev.type == QUIT:
            run = False
    # ეკრანის განახლება
    display.update()
#ფაიგეიმიდან გამოსვლა
quit()









