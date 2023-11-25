from nicegui import ui
ui.label('Microsoft')
name = ui.input(label='Name')
email = ui.input(label='Email')
emails = []
ui.query('body').classes('h-screen w-full bg-cyan-200 justify-between')
def validate(name,email,emails):
    if email == savedemail:
        ui.label("Already Signed Up with" + str(savedemail))
    else:
        ui.label("Welcome" + str(name))
    return email
ui.button("Validate",on_click=validate(name,email))




ui.run()