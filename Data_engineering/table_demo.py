from nicegui import ui

import os
current_folder = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_folder, 'Jugendwettbewerb_Statistics.csv')
# read data from csv file
with open(csv_file_path, 'r') as f:
    data = f.readlines()
column_row = data[0].replace('\n', '')
columns_csv = column_row.split(';')

columns_nicegui = [
    {'name': oneColumn, 'label': oneColumn, 'field': oneColumn, 'required': True, 'align': 'left', 'sortable':True} for oneColumn in columns_csv
]


data_csv = data[1:] # e.g.['Stufe1-4;23;18;14;10;1;2023',...]
data_nicegui = []
for oneLine in data_csv:
    one_row = oneLine.replace('\n', '').split(';') # List of values of one record, z.B. ['Stufe1-4', '23', '18', '14', '10', '1', '2023']
    data_nicegui.append(one_row)   
rows = []
for Stufen in range(0,len(data_nicegui)):
    rows.append({})
    newline = data_nicegui[Stufen]
    rows[Stufen]['Jahrgang'] = newline[0]
    rows[Stufen]['Geschlecht'] = newline[1]
    rows[Stufen]['1.Preis'] = newline[2]
    rows[Stufen]['2.Preis'] = newline[3]
    rows[Stufen]['Auszeichnung'] = newline[4]
    rows[Stufen]['Anerkennung'] = newline[5]
    rows[Stufen]['Runde'] = newline[6]
    rows[Stufen]['Jahr'] = newline[7]
    


    

'''
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol'},
]
'''
print(rows)
rund1_table = ui.table(columns=columns_nicegui, rows=rows, row_key='Jahrgangstufe',pagination=5)

ui.run()