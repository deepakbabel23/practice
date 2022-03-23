import numpy
class Cookie:
    def __init__(self, color):
       self.color = color

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color

if __name__ == "__main__":
    greenCookie = Cookie("green")
    blueCookie = Cookie("blue")

    print(greenCookie.get_color())
    print(blueCookie.get_color())

    greenCookie.set_color("dark green")
    blueCookie.set_color("dark blue")

    print(greenCookie.get_color())
    print(blueCookie.get_color())
