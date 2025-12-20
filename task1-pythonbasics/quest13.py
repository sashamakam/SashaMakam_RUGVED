from abc import ABC,abstractmethod 

class shape(ABC):
    def __init__(self,c):
        self.color = c
    
    def get_color(self)->str:
        return self.color
    
    def get_area(self) ->float:
        pass

class square(shape):
    def __init__ (self,c,side:float):
        super().__init__(c)
        self.side=side
    def get_area(self) -> float:
        return self.side * self.side


if __name__=="__main__":
    square_obj = square(c="blue", side=4.0)
    print("The color of the square is:" , square_obj.get_color())
    print("The area of the square is:" , square_obj.get_area())


    