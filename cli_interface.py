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


def run():
    display_splash_message()

    switch = {
        "help": display_help_message,
        "quit": display_quit_message
    }

    running = True
    while running:
        user_input = input("> ")

        command = switch.get(user_input.lower())
        if command is not None:
            print("[COMMAND]")
            command()  # Call corresponding function.

            if user_input.lower() == "quit":
                break

            continue


if __name__ == '__main__':
    run()
