
import string
import random

"""This module contains the dictionary of translations
and the functions that make the translator run properly
"""

# List of commands and dictionary of translations
command_list = ["list_terms", "list_commands", "random_definition", "quit"]

translations = {"print" : "System.out.println(thing to print)", "add" : "+",
"subtract" : "-", "multiply" : "*", "divide" : "/", "modulus" : "%",
"integer" : "byte/short/int/long 'name' = value", "string" :
'String "name" = "text"', "boolean" : "boolean 'name' = true/false",
"decimal" : "float/double 'name' = value", "and" : "&&", "or" : "||",
"greater_than" : "a >/>= b", "less_than" : "a </<= b",
"equality" : "==/!=", "comment" : "//", "if/elif/else" :
"if(boolean) {code} else if(boolean) {code} else {code}",
"list" :
"Java uses ArrayList for this, but it must be imported so it isn't listed",
"tuple" : "variable_type[] 'name' = new variable_type[size]",
"dictionary" :
"Java uses Map for this, but it must be imported so it isn't listed",
"Java_for_loop" :
"for(initial code; boolean; code run after every loop) {code}",
"while_loop" : "while(boolean) {code}", "+=" : "+=", "-=" : "-=",
"list_length" : "array_name.length",
"typecast" : "(new_type)value", "function" :
"<access_modifier> <return_type> 'name'(parameters) {code}",
"return" : "return", "multi-line_comment" : "/* */",
"Python_for_loop" :
"for('name' : list/array) {code} **this is called a for-each loop in Java**",
"class" : "<access_modifier> class 'name' {code}",
"inherit" : "<access_modifier> class 'name1' extends 'name2' {code}",
"super" : "super(parameters)", "string_length" : "string_name.length()",
"exponent" : "Java has no basic operator for exponents"}

# Add each key from translations into a term list
term_list = []
for key in translations.keys():
    term_list.append(key)

#Functions from the Chatbot assignment
def prepare_text(input):
    """Makes all user input lowercase for easier interpretation

    Parameters
    ----------
    input: string
        The string that the user input

    Returns
    -------
    lower_string: string
        The string that the user input but all lowercase
    """

    lower_string = input.lower()
    return lower_string

def end_chat(input):
    """Stops the translator if the user inputs 'quit'

    Parameters
    ----------
    input: string
        The string that the user input

    Returns
    -------
    output: boolean
        True if the user inputs "quit", False otherwise
    """

    if input == "quit":
        output = True
    else:
        output = False
    return output

# Self-written functions for the translator
def list_commands():
    """Lists all available commands

    Returns
    -------
    command_list_string: string
        String containing every command separated by spaces
    """

    # Add each command to a single command list string
    command_list_string = ""
    for command in command_list:
        command_list_string += command
        command_list_string += " "
    return command_list_string

def list_terms():
    """Lists all available terms

    Returns
    -------
    term_list_string: string
        String containing every term separated by spaces
    """

    # Add each term to a single term list string
    term_list_string = ""
    for term in term_list:
        term_list_string += term
        term_list_string += " "
    return term_list_string

def random_definition():
    """Provides the user with a random term and its definition

    Returns
    -------
    rand: string
        String that combines a random term and its definition
    """
    # Get a random term and create rand string
    rand_term = term_list[random.randint(0, len(term_list) - 1)]
    placeholder_term = rand_term
    rand_def =  translations[placeholder_term]
    rand = "'" + rand_term + "' in Java is: " + rand_def
    return rand


def start_translator():
    """Main function to run the translator."""

    print("Welcome to my Python-to-Java translator!")
    print("Try typing in a basic Python command to get started,")
    print("or type 'list_terms' for a list of available Python commands.")
    running = True
    while running:

        # Get a message from the user
        msg = input("Type here: ")
        msg = prepare_text(msg)
        out_msg = "out_msg is blank"

        # Output that prints if the user inputs a nonexistent command
        if msg not in command_list:
            out_msg = "This command/term does not exist, sorry!"
            out_msg += " If you are unsure, try 'list_commands' "
            out_msg += "or 'list_terms' for lists of available inputs."

        # Close the translator
        if end_chat(msg):
            out_msg = "Goodbye!"
            running = False

        # Print term list if user requests
        if msg == "list_terms":
            out_msg = "Available terms: " + list_terms()

        # Print command list if user requests
        if msg == "list_commands":
            out_msg = "Available commands: " + list_commands()

        # Print a definition for a random term
        if msg == "random_definition":
            out_msg = random_definition()

        # Print the definition of the term the user inputs
        if msg in term_list:
            out_msg = "In Java, '" + msg + "' is: " + translations[msg]

        # Print the next line of translator output
        print(out_msg)
