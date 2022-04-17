class Pointer():
    def __init__(self,word,pages):
        self.word=word
        self.pages=pages
        self.amount=len(pages)
    def output(self):
        print(self.word,self.pages,self.amount)
    def output_pages(self):
        print(self.pages)
def getfromk():
    mass=[]
    while True:
        word=input("Введите слово:")
        pages=input("Введите страницы с этим словом:")
        mas=[]
        mas.append(word)
        mas.append(pages.split())
        if 1>len(mas[1])>10:
            print("Количество страниц должно быть от 1 до 10")
            mas=input()
        mass.append(Pointer(mas[0],mas[1]))
        while True:
            s=input("Продолжить вводить?(y/n):")
            if s=="n":
                break
            elif s!="y":
                print("Недопустимый ответ")
            break
        if s=="n":
            break
    return mass
def getfromf():
    mass=[]
    s=input("Введите название файла(с  расширением):")
    try:F=open(s)
    except:
        print("Нет такого файла")
        return []
    for i in F:
        mass.append(Pointer(i.split()[0],i.split()[1:]))
    return mass

def create():
    ss=input("С клавиатуры или с файла(k/f):")
    if ss=="k":
        mas=getfromk()
    elif ss=="f":
        mas=getfromf()
    else:print("Ошибка")
    return mas

def output(mas):
    if len(mas)==0:
        print("Ничего нет")
        return 0
    for i in mas:i.output()

def output_pages(mas):
    ss=input("Введите слово:")
    for i in mas:
        if i.word==ss:
            print(i.pages)
            break
    else:print("Такого слова нет")

def delete(mas):
    ss=input("Введите слово, котороe нужно удалить:")
    for i in mas:
        if i.word==ss:
            mas.remove(i)
            break
    else:print("Такого слова нет")
def main():
    mas=[]
    while True:
        s=input("Введите функцию(create/output/output pages/delete):")
        if s=="create":
            mas=create()
        if s=="output":
            output(mas)
        if s=="output pages":
            output_pages(mas)
        if s=="delete":
            delete(mas)
        if s=="":
            break
        
if __name__ == '__main__':
    main()

        
