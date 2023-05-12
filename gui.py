import re
from main import final_validation

ids_to_check = set()


def validate_then_add_to_list(text):
    pattern = re.compile("v=([0-9A-Za-z]{11})*")
    m = re.search(pattern, text)
    if m:
        ids_to_check.add(m.group(0)[2:])
    print(ids_to_check)


def run():
    while True:
        url = input("Enter your url: ").lower()
        global ids_to_check
        if url == 'validate':
            final_validation(ids_to_check)
            ids_to_check = set()
        elif url == 'quit':
            print('Goodbye! ')
            break
        else:
            ids_to_check.add(url)
            print(ids_to_check)


if __name__ == "__main__":
    run()
