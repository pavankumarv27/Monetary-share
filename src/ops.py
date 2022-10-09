import json


def convert_string_to_dict(data):
    data = '"' + data.split(':')[0] + '"' + ":" + data.split(':')[-1]
    data = '{' + data + '}'
    return json.loads(data)


if __name__ == "__main__":
    print(convert_string_to_dict('Ash:20'))
