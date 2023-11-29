from nicegui import ui
with ui.grid(columns=3):
    ui.label("Hello, world!")
    ui.button("Click me", on_click=lambda: ui.notify("You clicked me!"))
    ui.button("Close")
ui.run()
