from pyscript import display, document


def search_game(e):
    document.getElementById("output").innerHTML = " "
    fav_game = document.getElementById("dictionary").value

    gdev = {
        'roblox' : 'David Baszucki',
        'codm' : 'TIMI Studio',
        'fnaf' : 'Scott Cawthon',
        'minecraft' : 'Notch'
    } #definie ditator

    g_check = fav_game in gdev

    display_message = ("sorry lol loll", f'{gdev[fav_game]}')

    display(display_message[g_check], target="output")

    gdev['genshin impact'] = 'Hoyoverse'
    display(gdev, target="output")

    list_tuple = [(1, 'a'), (2, 'b'), (3, 'c')]
    tuple_strings = ('ab', 'cd', 'ef')
    list_strings = ['ax', 'by', 'cz']

    display(dict(list_tuple), target="output")
    display(dict(tuple_strings), target="output")
    display(dict(list_strings), target="output")

    keywords = ['say', 'jm', 'jay', 'mace']
    values = ['esguerra', 'piansay', 'estrada', 'panela']
    students_nick = dict(zip(keywords, values))

    display(students_nick, target="output")

    philadelphia = {
        'center' : 'Joel Embiid',
        'pf' : 'LeBron James',
        'sf' : 'Jaylen Brown',
        'sg' : 'VJ Edgecombe',
        'pg' : 'Tyrese Maxey'
    }

    philadelphia['pg'] = 'Stephen Curry'
    del philadelphia['sg']
    display(philadelphia, target="output")

    dict1 = {'x':1, 'y':2, 'z':3}
    dict2 = {'a':4, 'b':5, 'c':6}

    display(dict1 | dict2, target="output")
    merged_dic = {**dict1, **dict2}

    display(merged_dic, target="output")

    display(len(merged_dic), target="output")

    ai = {
            'tony stark' : 'creator',
            'JARVIS' : 'AI1',
            'FRIDAY' : 'AI2',
            'Edith' : 'AI3',
            'Vision' : 'AI4'
    }

    display("Vision" in ai, target="output")
    display(ai.get('JARVIS'), target="output")
    display(ai.keys(), target="output")
    display(ai.values(), target="output")
    display(ai['tony stark'], target="output")