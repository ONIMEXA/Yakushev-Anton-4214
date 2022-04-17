class Factory():
    def __init__(self,type,coord):
        self.type=type
        self.coord=coord
    def move(self,shift):
        for i in range(len(coord)):
            for j in range(2):
                self.coord[i][j]+=shift
    def square(self):
        s=0
        if type=="t":
            n=3
        else:
            n=4
        for i in range(1,n-1):
            s+=self.coord[i][0]*self.coord[i][1]+1
            s-=self.coord[i][0]+self.coord[i][1]
        s+=self.coord[n][0]*self.coord[1][1]
        s-=self.coord[1][0]*self.coord[n][1]
        s=abs(s)*0.5
        return s

def get():
    mas=[]
    type=input("Введите тип первой фигуры(t/r):")
    if type!="t" or type!="r":
        print("Нет такого типа")
        return 0
    coord=[]
    print("Введите координаты точек фигуры:")
    if type=="t":
        for i in range(3):
            s=input().split()
            if len(s)!=2:
                print("Неправильно введены координаты")
                return 0
            for j in range(2):
                try:s[j]=int(s[j])
                except:
                    print("Неправильно введены координаты")
                    return 0
            coord.append(s)
    if type=="r":
        for i in range(4):
            s=input().split()
            if len(s)!=2:
                print("Неправильно введены координаты")
                return 0
            for j in range(2):
                try:s[j]=int(s[j])
                except:
                    print("Неправильно введены координаты")
                    return 0
            coord.append(s)
    mas.append(Factory(type,coord))
    type=input("Введите тип второй фигуры(t/r):")
    if type!="t" or type!="r":
        print("Нет такого типа")
        return 0
    coord=[]
    print("Введите координаты точек фигуры:")
    if type=="t":
        for i in range(3):
            s=input().split()
            if len(s)!=2:
                print("Неправильно введены координаты")
                return 0
            for j in range(2):
                try:s[j]=int(s[j])
                except:
                    print("Неправильно введены координаты")
                    return 0
            coord.append(s)
    if type=="r":
        for i in range(4):
            s=input().split()
            if len(s)!=2:
                print("Неправильно введены координаты")
                return 0
            for j in range(2):
                try:s[j]=int(s[j])
                except:
                    print("Неправильно введены координаты")
                    return 0
            coord.append(s)
    mas.append(Factory(type,coord))

def compare(mas):
    if mas[0].square>mas[1].square:
        print("Площадь первой больше")
    if mas[0].square<mas[1].square:
        print("Площадь второй больше")
     
def main():
    mas=get()
    while True:
        s=input("Введите функцию(move,compare):")
        if s=="move":
            try:ss=int(input("Первую или вторую(1/2):"))
            except:
                print("Неправильное значение")
                return 0
            try:sss=int(input("Насколько?:"))
            except:
                print("Неправильное значение")
                return 0
            try:mas[ss-1].move(sss)
            except:
                print("Неправильное значение")
                return 0
        if s=="compare":
            compare(mas)
        if s=="":
            break



    
if __name__=="__main__":
    main()
