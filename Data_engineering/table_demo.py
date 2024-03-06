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

plotly = ui.plotly(fig).classes('w-full h-40')
def change(value):
    fig = {
    'data': [
        {
            'type': 'lines',
            'name': 'Runde 1',
            'x': ["2023", "2022", "2021", "2020"],
            'y': [onerow[value] for onerow in rows if onerow["Runde"] == "1"],
            "line": {"color": 'rgb(0, 0, 255)'}
        },
        {
            'type': 'lines',
            'name': 'Runde 2',
            'x': ["2023", "2022", "2021", "2020"],
            'y': [onerow[value] for onerow in rows if onerow["Runde"] == "2"],
            "line": {"color": 'rgb(255, 0, 0)'}
        },
        {
            'type': 'lines',
            'name': 'Runde 3',
            'x': ["2023", "2022", "2021", "2020"],
            'y': [onerow[value] for onerow in rows if onerow["Runde"] == "3"],
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
    plotly.update_figure(fig)
select1 = ui.select(["Gesamt","1.Preis","2.Preis","Auszeichnung","Anerkennung","Teilnahme"], value = "Gesamt",on_change= lambda i: change(i.value),)
rows.sort(key=lambda x: x['Jahrgang'] , reverse=True)
print("rows after sort: " ,rows)
#rund1_table = ui.table(columns=columns_nicegui, rows=rows, row_key='Jahrgangstufe',pagination=5)


ui.run()
