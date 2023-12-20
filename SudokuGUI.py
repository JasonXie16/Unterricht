#bis jetzt nur zeit
import sudokuRules
import math
import datetime
from nicegui import ui
import suduku_matrix as sm

starttime = None
ui.query('body').classes('h-screen w-full bg-cyan-200 justify-between')
ui.markdown('## Sudoku Game')


sudoku_numbers = sm.suduku_matrix(placeholder = 0)
difficulty = ui.radio(["Easy","Normal","Hard"],value=1).props('inline')
# return sudoku numbers for give culomnIndex
def get_sudoku_numbers_colmn(columnIndex: int):
    for j in range(0,9,3):
        for i in range(0,9,3):
            print(sudoku_numbers[round(columnIndex / 3) + j][0 + i])


def get_sudoku_numbers_row(rowIndex: int):
    if rowIndex in [0, 3, 6]:
        return sudoku_numbers[rowIndex - 0][0:3] + sudoku_numbers[rowIndex + 1][0:3] + sudoku_numbers[rowIndex + 2][:3]
  
    elif rowIndex in [1, 4, 7]:
        return sudoku_numbers[rowIndex - 1][3:6] + sudoku_numbers[rowIndex][3:6] + sudoku_numbers[rowIndex + 1][3:6]

    elif rowIndex in [2, 5, 8]:
        return sudoku_numbers[rowIndex - 2][6:9] + sudoku_numbers[rowIndex - 1][6:9] + sudoku_numbers[rowIndex][6:9]

# Aufgabe 1: reset timer
def start_timerAndGame(button):
    difficulty.set_visibility(False)
    sudoku_numbers =  sudokuRules.zerosInSudoku(difficulty.value)
    print(sudoku_numbers)
    endtext.set_visibility(False)
    global starttime
    starttime = datetime.datetime.now()
    ui.timer(1.0, timer)
    #sudoku_numbers = sm.suduku_matrix(placeholder = 0)
    for i in range(9):
        for j in range(9):
            inputs[i][j].set_visibility(True)
            inputs[i][j].set_value(sudoku_numbers[i][j])
          
    label.set_visibility(True)
    start_button.set_visibility(False)

def timer():
    if starttime is not None:
        diff = datetime.datetime.now() - starttime
        past = int(diff.total_seconds())
        label.set_text(f"Gaming time: {past} seconds")

label = ui.label().classes('absolute top-0 right-0')
endtext =  ui.markdown()
def updateBlock(new_value: str, i: int, block_index: int):
    print(f"new Value: {new_value} at position {i} in block at {block_index}.")
    sudoku_numbers[block_index][i] = int(new_value)
    if not any(0 in block for block in sudoku_numbers):
        for i in inputs:
            for j in i:
                j.set_visibility(False)
        label.set_visibility(False)
        endtext = ui.markdown("## Congratulations! You have solved the " + str(difficulty.value) + " Sudoku after " + str(int((datetime.datetime.now() - starttime).total_seconds())) + " Seconds!")
        endtext.set_visibility(True)
        start_button.set_visibility(False)
        #difficulty.set_visibility(True)
        


    


def isUnique(new_value: str, block_index: int):
    if new_value != "0" and new_value != 0:      
        print(f"Validate new Value: {new_value} in block {sudoku_numbers[block_index]}.")
        valdiate_result = sudoku_numbers[block_index].count(int(new_value)) == 1
        print(f"Validate result: {valdiate_result}.")
        return valdiate_result
    return True
#https://quasar.dev/style/color-palette/
colors = ["green","blue","grey"]
start_button = ui.button("Start Sudoku Game", on_click=start_timerAndGame)
inputs=[[],[],[],[],[],[],[],[],[]]
def show_one_sudoku_block(block_index,bgcolor, one_sudoku_block = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]):
    with ui.grid(columns=3):
        for i in range(9):
            inputs[block_index].append(ui.input(value=one_sudoku_block[i], on_change=lambda inputevent, i=i: updateBlock(str(inputevent.value), i, block_index), validation={"found duplicate": lambda inputevent: isUnique(inputevent, block_index) }).props("bg-color=" + bgcolor))
with ui.grid(columns=3):
    for block_index in range(9):
        show_one_sudoku_block(block_index, str(colors[block_index % 3])+ "-" + str(block_index + 1),one_sudoku_block=sudoku_numbers[block_index])
        for i in inputs:
            for j in i:
                j.set_visibility(False)
        label.set_visibility(False)
        endtext.set_visibility(False)



ui.run()

# Vorbereitung: Fertig mit der Methode get_sudoku_numbers_colmn.
#  
# Aufgaben für nächste Woche bis 20.12.2023:
# 1. Baue ein selectbox mit 3 Schwierigkeitsstufen: easy(0), medium(1), hard(2), mit default value "easy".

# 2. Nach dem Starten des Spiels, soll 
# 2.1.die Zeit gestartet werden, 
# 2.2(optional). die selectbox verschwinden.
# 2.3. sudoku_numbers mit entsprechenden Placeholder 0 initialisiert werden. 
# Easy bedeutet 37-40 Zahle sind vorgegeben, Medium 32-36, Hard 27-31.

# 3. Wenn alle Lücken in Sudoku gefüllt sind, soll die Zeit gestoppt werden, und dann
# ein großer Text zusammen mit der benötigten Zeit in niceGui ausgegeben werden. Z.B:
# "Congratulations! You have solved the easy Sudoku after 90 seconds!"