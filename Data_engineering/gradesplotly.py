import plotly.graph_objects as go
from nicegui import ui

xyear = ["2022Semester1", "2022Semester2", "2023Semester1", "2023Semester2", "2024Semester1", "2024Semester2"]
y_math = [1.5, 1, 1.25, 1, 1.75, 1]
y_german = [1.5, 1, 3, 6, 1.75, 2]
y_sport = [3, 3, 2, 1, 1.75, 1]
fig = go.Figure(go.Scatter(x=xyear, y=y_sport,name="sport"))
#add a new trace to fig
fig.add_trace(go.Scatter(x=xyear, y=y_german,name="german"))
fig.add_trace(go.Scatter(x=xyear, y=y_math,name="math"))
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
ui.plotly(fig).classes('w-full h-40')


def change(selected):
    global fig
    if selected == "all":
        fig = go.Figure(go.Scatter(x=xyear, y=y_sport, name="sport"))
        fig.add_trace(go.Scatter(x=xyear, y=y_german, name="german"))
        fig.add_trace(go.Scatter(x=xyear, y=y_math, name="math"))
    else: 
        fig = go.Figure(go.Scatter(x=xyear, y="selected"))
    fig.update()
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    ui.plotly(fig).classes('w-full h-40')
    ui.update()

select1 = ui.select(["all",'sport', 'german', 'math'],value="all",on_change= lambda i: change(i.value))

ui.run()