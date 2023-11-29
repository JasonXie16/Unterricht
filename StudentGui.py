from nicegui import ui



class Student():
    def __init__(self,name:str,age:int,height:int,sex:str,schoolname:str,classname:str):
        self.name=name
        self.age = age
        self.height = height
        self.sex = sex
        self.schoolname = schoolname
        self.classname = classname
    def printinfo(self):
        print("name:", self.name)
        print("age:", str(self.age))
        print("height:", str(self.height))
        print("sex:", self.sex)
        print("schoolname:", self.schoolname)
        print("classname:", self.classname)


student1 = Student("John", 14, 180, "M", "Hogwarts", "7b")
student1.printinfo()

student2 = Student("Mary", 11, 160, "F", "Hogwarts", "5a")
student2.printinfo()

student3 = Student("Peter", 9, 200, "M", "Hogwarts", "11a")
student3.printinfo()

student4 = Student("Lisa", 15, 150, "F", "Hogwarts", "9d")
student4.printinfo()

student5 = Student("Tom", 13, 160, "M", "Hogwarts", "7c")
student5.printinfo()

student6 = Student("Sue", 22, 190, "F", "Hogwarts", "8b")
student6.printinfo()


with ui.dialog() as dialogjohn, ui.card():
    ui.label("name:John, age:14, height:180cm, sex:M, schoolname:Hogwarts, classname: 7b")
    ui.button("Close", on_click=dialogjohn.close)
with ui.dialog() as dialogMary, ui.card():
    ui.label("name:Mary, age:11, height:160cm, sex:F, schoolname:Hogwarts, classname: 5a")
    ui.button("Close", on_click=dialogMary.close)
with ui.dialog() as dialogPeter, ui.card():
    ui.label("name:Peter, age:9, height:200cm, sex:M, schoolname:Hogwarts, classname: 11a")
    ui.button("Close", on_click=dialogPeter.close)
with ui.dialog() as dialogLisa, ui.card():
    ui.label("name:Lisa, age:15, height:150cm, sex:F, schoolname:Hogwarts, classname: 9d")
    ui.button("Close", on_click=dialogLisa.close)
with ui.dialog() as dialogTom, ui.card():
    ui.label("name:Tom, age:13, height:160cm, sex:M, schoolname:Hogwarts, classname: 7c")
    ui.button("Close", on_click=dialogTom.close)
with ui.dialog() as dialogSue, ui.card():
    ui.label("name:Sue, age:22, height:190cm, sex:F, schoolname:Hogwarts, classname: 8b")
    ui.button("Close", on_click=dialogSue.close)


with ui.grid(columns=3):
    with ui.card().tight():
        ui.interactive_image('students/John.png',on_mouse=dialogjohn.open).classes('w-64')
    with ui.card().tight():
        ui.interactive_image('students/Mary.jpg',on_mouse=dialogMary.open).classes('w-64')
    with ui.card().tight():
        ui.interactive_image('students/peter.jpg',on_mouse=dialogPeter.open).classes('w-64')
    with ui.card().tight():
        ui.interactive_image('students/Lisa.jpg',on_mouse=dialogLisa.open).classes('w-64')
    with ui.card().tight():
        ui.interactive_image('students/Tom.png',on_mouse=dialogTom.open).classes('w-64')
    with ui.card().tight():
        ui.interactive_image('students/Sue.jpg',on_mouse=dialogSue.open).classes('w-64')


ui.run()