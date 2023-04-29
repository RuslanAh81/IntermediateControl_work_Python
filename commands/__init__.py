import commands.lists
import commands.notes

commands_dict = {
    'show': lists.show_lists,
    'use': lists.use_list,
    'create': lists.create_list,
    'all': notes.show_items,
    'add': notes.add_item,
    'edit': notes.edit_item,
    'remove': notes.remove_item,
    'complete': notes.complete_item,
    'incomplete': notes.incomplete_item
}