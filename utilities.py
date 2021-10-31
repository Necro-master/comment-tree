import json

def get_comment(id, dir_name):
    try:
        with open(f'{dir_name}/{id}.txt', "r") as file:
            comment = file.read()
            return comment
    except FileNotFoundError:
        return 1

def add_comments(data, dir_name):
    data['content'] = get_comment(data['id'], dir_name)
    if data['content'] == 1:
        return 1
    for e in data['replies']:
        add_comments(e, dir_name)


def comment_tree(tree: str, dir_name: str):
    data = json.loads(tree)
    status = add_comments(data, dir_name)
    if status == 1:
        return 1
    return json.dumps(data, indent=4, sort_keys=True)