from my_module.functions import *

"""This module contains the test functions that make sure
that the translator is running properly
"""

# All test functions
def all_terms_and_commands_printable():
    """Assert that all terms can be printed"""
    for term in term_list:
        assert isinstance(term, str)
    for command in command_list:
        assert isinstance(command, str)

def all_lists_are_lists():
    """Assert that all lists are lists"""
    assert isinstance(term_list, list)
    assert isinstance(command_list, list)

def translations_is_correct():
    """Assert that translations is dictionary of proper length"""
    assert isinstance(translations, dict)
    assert len(translations) == 35

def prepare_text_works():
    """Assert that prepare_text() works"""
    assert callable(prepare_text)
    assert prepare_text("HELLO") == "hello"
    assert prepare_text("") == ""
    assert prepare_text(" ") == " "

def end_chat_works():
    """Assert that end_chat() works"""
    assert callable(end_chat)
    assert end_chat("quit") == True
    assert end_chat("") == False
    assert end_chat("test") == False

def list_commands_works():
    """Assert that list_commands() works"""
    assert callable(list_commands)
    assert len(command_list) == 4

def list_terms_works():
    """Assert that list_terms() works"""
    assert callable(list_terms)
    assert len(term_list) == 35

def random_definition_works():
    """Assert that random_definition() works
    This test should fail 1 in every 35 times because two random
    definitions could still be the same definition"""
    assert callable(random_definition)
    random1 = random_definition()
    random2 = random_definition()
    assert random1 != random2

def start_translator_works():
    """Assert that start_translator() works"""
    assert callable(start_translator)

def run_all_tests():
    """Run all test functions"""
    all_terms_and_commands_printable()
    all_lists_are_lists()
    translations_is_correct()
    prepare_text_works()
    end_chat_works()
    list_commands_works()
    list_terms_works()
    random_definition_works()
    start_translator_works()
    print("All tests have run successfully!")
