import datetime
from nicegui import ui



sudoku_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
starttime = datetime.datetime.now()


    

def validate_sudoku_input(value:str,boxes):
    if value and value.isdigit():
        #if value in boxes
        return sudoku_numbers.count(int(value)) == 1
    return False


@ui.page('/')
async def index():
    b = ui.button('START')
    await b.clicked()
    sudoku_mainpage()
@ui.page('/input')
def sudoku_mainpage():
    #starttime = resetStarttime()
    ui.markdown('**## Sudoku Game')
    boxes = [[],[],[],[],[],[],[],[],[]]
    with ui.grid(rows=3,columns=3):
        for i in range(9):
            with ui.grid(columns=3):
                for i in range(len(sudoku_numbers)):
                    boxes[i].append(ui.input(value=sudoku_numbers[i], validation={"Invalid input": lambda value: validate_sudoku_input(value,boxes)}))
    

def updateGamingTime():
    label = ui.label().classes('absolute top-0 right-0')
    diff = datetime.datetime.now() - starttime
    past = int(diff.total_seconds())
    label.set_text(f"Gaming time: {past} seconds")
    ui.timer(1.0, updateGamingTime)



def resetStarttime():
    global starttime
    starttime = datetime.datetime.now()
    ui.timer(1.0,updateGamingTime)

#ui.button("START",on_click=resetStarttime)
ui.run(title="Suduku online games", port=5000)