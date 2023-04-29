import json
from datetime import datetime

def set_list(list_name):
    if (list_name == ''):
        print('Plese select a given list before this action')
    return list_name

def get_data(list_file_name):
    data = []
    with open(f'lists/{list_file_name}', 'r') as json_file:
        data = json.load(json_file)
    return data

def update_data(list_file_name, new_data):
    with open(f'lists/{list_file_name}', 'w') as json_file:
        json.dump(new_data, json_file, sort_key=True, indent=True)

def add_item(args):
    list_name = set_list(args[0])
    if(not list_name):
        return
    title = args[1]
    data = get_data(list_name)
    new_note = {
        'title': title,
        'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:S"),
        'completed': False
    }
    data.append(new_note)
    update_data(list_name, data)

def show_item(args):
    list_name = set_list(args[0])
    if(not list_name):
        return
    data = get_data(list_name)
    complete = 0
    if (len(data) ==0):
        print('No notes in the list, why dont you add one?')
    else:
        for index, note_item in enumerate(data):
            print(index + 1, note_item['title'])
            if (note_item['completed']):
                complete += 1
        print(f'{complete}/{len(data)} completed!')

def edit_item(args):
    list_name = set_list(args[0])
    if (not list_name):
        return
    item_id = int(args[1])
    new_title = args[2]
    data = get_data(list_name)
    updated_note ={
        'title': new_title,
        'create_at': datetime.now().strftime("%d/%m/%Y %H:%M:S"),
        'complete': False
    }
    data[item_id - 1] = updated_note
    update_data(list_name, data)

def remove_item(args):
    list_name = set_list(args[0])
    if (not list_name):
        return
    item_id = int(args[1])
    data = get_data(list_name)
    data.pop(item_id - 1)
    update_data(list_name, data)

def complete_item(args):
    list_name = set_list(args[0])
    if (not list_name):
        return
    item_id = int(args[1])
    data = get_data(list_name)
    data[item_id - 1]['completed'] = True
    update_data(list_name, data)

def incomplete_item(args):
    list_name = set_list(args[0])
    if (not list_name):
        return
    item_id = int(args[1])
    data = get_data(list_name)
    data[item_id - 1]['completed'] = False
    update_data(list_name, data)