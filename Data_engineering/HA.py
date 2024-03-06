import plotly.graph_objects as go
from nicegui import ui


def calculate_driving_distance(driving_time_seconds,accel,max):
    acceleration = (accel * 1000) / 3600  # km/h to m/s
    max_speed = (max * 1000) / 3600  # km/h to m/s
    distance = 0
    current_speed = 0
    for t in range(1, driving_time_seconds):

        if current_speed < max_speed:
            current_speed += acceleration
            if current_speed > max_speed:
                current_speed = max_speed
        distance += current_speed
        print(current_speed)
    return distance

# first car
data_pointscar1 = [(t, calculate_driving_distance(t,10,250)) for t in range(1, 101)]
fig = go.Figure(go.Scatter(x=[i[0] for i in data_pointscar1], y=[i[1] for i in data_pointscar1],name="Volkswagen Golf"))
# second car
data_pointscar2 = [(t, calculate_driving_distance(t,7.5,300)) for t in range(1, 201)]
fig.add_trace(go.Scatter(x=[i[0] / 2  for i in data_pointscar2], y=[i[1] for i in data_pointscar2],name="Mercedes GLC"))
fig.update_layout(margin=dict(l=0, r=700, t=0, b=0))
ui.plotly(fig).classes('w-full h-40')
ui.run()