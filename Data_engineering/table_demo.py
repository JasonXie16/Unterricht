import plotly.graph_objects as go

from nicegui import ui

import os
current_folder = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_folder, 'Jugendwettbewerb2020-2023.csv')
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
    rows[Stufen]['Gesamt'] = newline[0]
    rows[Stufen]['1.Preis'] = newline[1]
    rows[Stufen]['2.Preis'] = newline[2]
    rows[Stufen]['Auszeichnung'] = newline[3]
    rows[Stufen]['Anerkennung'] = newline[4]
    rows[Stufen]['Teilnahme'] = newline[5]
    rows[Stufen]['Jahrgang'] = newline[6]
    rows[Stufen]['Runde'] = newline[7]
    


    

'''
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol'},
]
'''

teilenhmer1 = []
teilenhmer2 = []
teilenhmer3 = []
'''
for oneRow in rows:	
    teilnehmer = 0
    for oneitem in oneRow:
        if oneitem == '1.Preis' or oneitem == '2.Preis' or oneitem == 'Auszeichnung' or oneitem == "Anerkennung":
            if oneRow[oneitem].isnumeric() == True:
                teilnehmer += int(oneRow[oneitem])
    if oneRow['Runde'] == '1':
        teilenhmer1.append(teilnehmer)
    elif oneRow['Runde'] == '2':
        teilenhmer2.append(teilnehmer)
    elif oneRow['Runde'] == '3':
        teilenhmer3.append(teilnehmer)
sums1 = []
sums2 = []
sums3 = []
print(teilenhmer1)
for i in range(0, len(teilenhmer1), 5):
    current_sum = sum(teilenhmer1[i:i+5])
    sums1.append(current_sum)
for i in range(0, len(teilenhmer2), 5):
    current_sum = sum(teilenhmer2[i:i+5])
    sums2.append(current_sum)
for i in range(0, len(teilenhmer3), 3):
    current_sum = sum(teilenhmer3[i:i+3])
    sums3.append(current_sum)
'''

rows.sort(key=lambda x: x['Jahrgang'] , reverse=True)
print("rows after sort: " ,rows)
#rund1_table = ui.table(columns=columns_nicegui, rows=rows, row_key='Jahrgangstufe',pagination=5)
fig = {
    'data': [
        {
            'type': 'lines',
            'name': 'Runde 1',
            'x': ["2023", "2022", "2021", "2020"],
            'y': [onerow["Gesamt"] for onerow in rows if onerow["Runde"] == "1"],
            "line": {"color": 'rgb(0, 0, 255)'}
        },
        {
            'type': 'lines',
            'name': 'Runde 2',
            'x': ["2023", "2022", "2021", "2020"],
            'y': [onerow["Gesamt"] for onerow in rows if onerow["Runde"] == "2"],
            "line": {"color": 'rgb(255, 0, 0)'}
        },
        {
            'type': 'lines',
            'name': 'Runde 3',
            'x': ["2023", "2022", "2021", "2020"],
            'y': [onerow["Gesamt"] for onerow in rows if onerow["Runde"] == "3"],
            "line": {"color": 'rgb(0, 255, 0)'}
        },
    ],
    'layout': {
        'margin': {'l': 30, 'r': 30, 't': 30, 'b': 30},
        'plot_bgcolor': '#E5ECF6',
        'xaxis': {'gridcolor': 'white'},
        'yaxis': {'gridcolor': 'white'},
    },
}
ui.plotly(fig).classes('w-full h-40')
ui.run()