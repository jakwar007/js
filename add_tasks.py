import os
import re
from bs4 import BeautifulSoup

main_file = os.path.join(os.getcwd(), 'wark_z4.html')

task_regex = re.compile(r'^wark_z(\d+)(_kod)?\.html$')

with open(main_file, 'r+', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

div_tasks = soup.find('div', {'id': 'zadania'})
div_tasks_code = soup.find('div', {'id': 'zadania-kody'})

for root, _, files in os.walk(os.getcwd()):
    for file in files:
        match = task_regex.match(file)
        if match:
            file_name = os.path.splitext(file)[0]
            if match.group(2):
                button = soup.new_tag('input', type='button', value=f"{file_name} kod-warkusz", name_attr=file_name, onclick=f"WinOpen('{file_name}')")
                if div_tasks_code:
                    div_tasks_code.append(button)
            else:
                button = soup.new_tag('input', type='button', value=f"{file_name}-warkusz", name_attr=file_name, onclick=f"WinOpen('{file_name}')")
                if div_tasks:
                    div_tasks.append(button)

with open(main_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("HTML file updated successfully.")
