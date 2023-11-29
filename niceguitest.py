from nicegui import ui
ui.markdown('# Microsoft')
name = ui.input(label='Name')
email = ui.input(label='Email')
emails = []
ui.query('body').classes('h-screen w-full bg-cyan-200 justify-between')
def validate(name,email):
    if email:
        ui.label("Already Signed Up with" + str(email))
    else:
        ui.label("Welcome" + str(name))
    return email
ui.button("Validate",on_click=validate(name,email))



ui.run()