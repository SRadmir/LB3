import math
class Shape:
    def __init__(self):
        pass
    @staticmethod
    def about():
        print("Программа разработана для вычисления объема шарового сегмента.")
class SphericalSegment(Shape):
    def __init__(self, radius, height):
        super().__init__()  
        self.__radius = radius 
        self.__height = height  
    def volume(self):
        return (math.pi * self.__height**2 * (3 * self.__radius - self.__height)) / 3
    @staticmethod
    def about():
        print("Это класс для вычисления объема шарового сегмента.")
Shape.about()
try:
    radius = float(input("Введите радиус сферы: "))
    height = float(input("Введите высоту сегмента: "))

    if height > 2 * radius:
        print("Высота сегмента не может превышать диаметр сферы. Попробуйте ещё раз.")
    elif height <= 0 or radius <= 0:
        print("Радиус и высота должны быть положительными числами.")
    else:
        segment = SphericalSegment(radius, height)
        print(f"Объем шарового сегмента с радиусом сферы {radius} и высотой сегмента {height} составляет: {segment.volume():.2f} кубических единиц.")
except ValueError:
    print("Пожалуйста, введите валидные числовые значения.")
