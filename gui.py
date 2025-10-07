import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter Task")
add_button = sg.Button("Add")

print(label)
window = sg.Window('My Task Manager Application', layout=[[label], [input_box, add_button]])

# displays window
window.read()
window.close()
