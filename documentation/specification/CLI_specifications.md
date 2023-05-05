# Command Line Interface Specifications

A breakdown of what the Command Line Interface for this program should look like.

For use as guidance on how the program should handle and display different states.

## Splash
Splash screens are usually displayed the startup of a program.

    ----------------------------
        YouTube URL Validator   
    ----------------------------

        Type 'help' for Help,
                or
        'quit' || 'q' to Exit.

    ----------------------------

    >   ...

## Input
The program receives user input via the command line.
It should communicate different states to the user, as they are inputting links,
and once they've submitted them for validation.

### Input Command
The input was a valid command:

    >   ...
    [COMMAND]
    >   ...
    
### Input URL OK
The input was a recognisable YouTube URL:

*Note: This doesn't mean it is a valid, watchable URL yet,
it just means the program can parse the input string to find the video ID.
In a YouTube link, it is usually appended at the end in a format such as, **"...id="***

    >   ...
    [OK]
    >   ...

### Input BAD
The Input could not be recognised:

*i.e. Not a valid program command, or not a valid/parsable YouTube link (see above).*

    >   ...
    [BAD]
    >   ...

## Help Command

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


## Submitting
Once the user has submitted all their links for validation,
and have entered an empty line (which is treated as the Submission Command),
the program will send these links for validation and receive a **Response**
from the YouTube Data API.

Using this response, we can determine which links were valid, 
watchable videos and display this information to the user.

### Valid Links
In the case that all links are valid:

    >   ...
    >
    [SUBMIT] --->
    <--- [RECEIVED]
    
    Status:
        20  Links Submitted.
        20  Links OK.

    Links are healthy.

### Invalid Links
In the case that some, or all links are valid:

    >   ...
    >
    [SUBMIT] --->
    <--- [RECEIVED]
    
    Status:
        20  Links Submitted.
        14  Links OK.
        6   Links BAD.

    The following URLs are invalid:
        [1] ...
        [2] ...

### Request Error
In the case that the program could not reach the API (*most likely due to network failures*):

    >   ...
    >
    [SUBMIT] ---X

    There was a problem submitting this Request.

    Status:
        "..."

### Response Error
In the case that the **Response** received was an Error message 
(*most likely due to an authentication failure*):

    >   ...
    >
    [SUBMIT] --->
    X--- [RECEIVED]

    There was a problem receiving a Response.

    Status:
        "..."

## Quit Command
The program should have a way to exit gracefully, 
this is the purpose of the `quit` command.
For aesthetics, we can have a different quit message displayed depending on how/when the program quit.

### Cancelled Mid-Loop
If quit before receiving a Response (*see above*):

    Cancelling...

    Have a Lovely Day!

### Exiting
If quit after receiving a Response (*see above*):

    Thank you for using YouTube-URL-Validator.

    Have a Lovely Day!