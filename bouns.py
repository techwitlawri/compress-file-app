import FreeSimpleGUI as sg
from zip_creator import make_archive


sg.theme('Black')

label1= sg.Text('select files to compress: ')
input1= sg.Input()

choose_button1= sg.FilesBrowse('choose', key= 'files')

label2= sg.Text('selectb destination folder: ')
input2= sg.Input()

choose_button2= sg.FolderBrowse('choose', key= 'folder')

compress_button = sg.Button("compress")
output_label = sg.Text(key= 'output', text_color='green')
window= sg.Window('file Compressor', layout= [[label1, input1,choose_button1],
                                              [label2, input2,choose_button2],
                                              [compress_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(' ; ')
    folder = values['folder']
    make_archive(filepaths, folder)
    window["output"].update(value="compression completed")

    sg.WIN_CLOSED
    break
window.close()