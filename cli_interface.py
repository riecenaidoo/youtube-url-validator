import re

import main


def display_splash_message():
    print("""
----------------------------
    YouTube URL Validator   
----------------------------

    Type 'help' for Help,
            or
    'quit' || 'q' to Exit.

----------------------------
    """)


def display_help_message():
    print("""
Usage:
    - Paste YouTube video links, individually, into the terminal.
    - Press Enter on an empty line to submit the links for validation.


Status Messages:
    - [BAD]     : Input was not recognisable.
    - [OK]      : Input was a parsable URL.
    - [COMMAND] : Input was a recognised Command.
    - [SUBMIT]  : Input was an empty line, for Submission.


Valid Commands:
    - 'quit' || 'q' : Exit the Program.
    - 'help'        : Display Help information (i.e this screen)
    """)


def display_quit_message():
    print("""
Cancelling...

Have a Lovely Day!
    """)


def submit(link_ids: set):
    main.final_validation(link_ids)


def run():
    display_splash_message()

    switch = {
        "help": display_help_message,
        "quit": display_quit_message,
        " ": submit
    }

    link_ids = set()
    running = True
    while running:
        user_input = input("> ")

        if user_input is None:
            continue

        command = switch.get(user_input.lower())
        if command is not None:
            print("[COMMAND]")

            if command == submit:
                command(link_ids)
                break
            else:
                command()  # Call corresponding function.

            if command == "quit":
                break

            continue

        pattern = re.compile("(v=[_0-9A-Za-z]{11})")
        matcher = re.search(pattern, user_input)
        if matcher is not None:
            link_ids.add(matcher.group(1)[2:])
            print("[OK]")
        else:
            print("[BAD]")

    # httplib2.error.ServerNotFoundError <---- Error to catch for submitting failure


if __name__ == '__main__':
    run()
