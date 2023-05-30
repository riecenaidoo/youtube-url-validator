import re
from main import final_validation

ids_to_check = set()


def validate_then_add_to_list(text):
    pattern = re.compile("(v=[_0-9A-Za-z]{11})")
    m = re.search(pattern, text)
    if m:
        ids_to_check.add(m.group(1)[2:])
    print(ids_to_check)


def run():
    while True:
        url = input("Enter your url: ")
        global ids_to_check
        if url.lower() == 'validate':
            final_validation(ids_to_check)
            ids_to_check = set()
        elif url.lower() == 'quit' or url.lower() == 'exit':
            print('Goodbye! ')
            break
        else:
            validate_then_add_to_list(url)


if __name__ == "__main__":
    run()
