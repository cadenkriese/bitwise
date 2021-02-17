from inquirer import themes


def theme():
    return themes.load_theme_from_dict({
        'Question': {
            'mark_color': 'bright_blue',
            'brackets_color': 'bright_white',
            'default_color': 'bright_white',
        },
        'Editor': {
            'opening_prompt_color': 'bright_black',
        },
        'Checkbox': {
            'selection_color': 'bright_blue',
            'selection_icon': '→',
            'selected_icon': '✅',
            'selected_color': 'bright_blue',
            'unselected_color': 'bright_white',
            'unselected_icon': '❎',
        },
        'List': {
            'selection_color': 'bright_blue',
            'selection_cursor': '→',
            'unselected_color': 'bright_white',
        }
    }
    )
