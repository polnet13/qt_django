import os

main ='pyside6-uic untitled.ui -o untitled_ui.py'
vtt = 'pyside6-uic vtt.ui -o vtt_ui.py'
search = 'pyside6-uic search.ui -o search_ui.py'

texts = [main]

import os 

parent = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ui_path = os.path.join(parent, 'rsc', 'ui')
os.chdir(ui_path)

for row in texts:
    print(row)
    os.system(row)
 
# os.system('C:/Users/prude/anaconda3/envs/pol/python.exe c:/Users/prude/kimAI/main.py')