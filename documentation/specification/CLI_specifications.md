# Command Line Interface Specifications

A breakdown of what the Command Line Interface for this program should look like.

Guidance for how the program should handle different states.

## Splash

    ----------------------------
        YouTube URL Validator   
    ----------------------------

        Type 'help' for Help,
                or
        'quit' || 'q' to Exit.

    ----------------------------

    >   ...

## Input

The Program should display the input loop in the following ways.

### Input Command
The input was a valid command:

    >   ...
    [COMMAND]
    >   ...
    
### Input URL OK
The input was a valid YouTube URL:

    >   ...
    [OK]
    >   ...

### Input BAD
The Input could not be recognised:
    i.e. Not a valid command, or not a valid/parsable YouTube link.

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
        - 'quit' || 'q'
        - 'help'

## Quit Command

### Cancelled Mid-Loop
During an input request

    Cancelling...

    Have a Lovely Day!

### Exiting
After finishing a request.

    Thank you for using YouTube-URL-Validator.

    Have a Lovely Day!

## Submitting

### Valid Links

    >   ...
    >
    [SUBMIT] --->
    <--- [RECIEVED]
    
    Status:
        20  Links Submitted.
        20  Links OK.

    Links are healthy.

### Invalid Links

    >   ...
    >
    [SUBMIT] --->
    <--- [RECIEVED]
    
    Status:
        20  Links Submitted.
        14  Links OK.
        6   Links BAD.

    The following URLs are invalid:
        [1] ...
        [2] ...

### Request Error

    >   ...
    >
    [SUBMIT] ---X

    There was a problem submitting this Request.

    Status:
        "..."

### Response Error

    >   ...
    >
    [SUBMIT] --->
    X--- [RECIEVED]

    There was a problem receving a Response.

    Status:
        "..."
