import numpy as np
import math 
from matplotlib import pyplot as plt
from nicegui import ui
x = range(-360,360,20)
with ui.pyplot(figsize=(3, 2)):
    print(x)
    y = [math.sin(i) for i in x]
    ui.label("sin")
    plt.plot(x, y, '-',color="green")
    plt.legend(["sin"])
with ui.pyplot(figsize=(3, 2)):
    y = [math.cos(i) for i in x]
    ui.label("cos")
    plt.plot(x, y, '-',color="red")
    plt.legend(["cos"])
with ui.pyplot(figsize=(3, 2)):
    y = [math.tan(i) for i in x]
    ui.label("tan")
    plt.plot(x, y, '-',color="blue")
    plt.legend(["tan"])
with ui.pyplot(figsize=(3, 2)):
    y = [1 / math.tan(i) for i in x if math.tan(i) != 0]
    ui.label("cot")
    plt.plot([i for i in x if math.tan(i) != 0], y, '-',color="black")
    plt.legend(["cot"])
    

    
ui.run()