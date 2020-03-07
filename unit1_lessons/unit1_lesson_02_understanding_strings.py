__author__ = 'Kalyan'

from placeholders import *

notes = """
 string is one of the most commonly used data types, it used to represent textual data.
 It has different behavior than a char* in C. 

 I recommend you to do this lesson by experimenting in the console.  Run each test individually in 
 py.test and fix each one, one assert at a time.
 
 Start reading online documentation/resources only if you are not able to figure it out by experiment.
"""

def test_string_type():
    assert __ == type("Hello World").__name__
    assert __ == isinstance("Hello World", str)

def test_single_quoted_strings_are_strings():
    assert __ == isinstance('Hello World', str)

def test_double_quoted_strings_are_strings():
    assert __ == isinstance("Hello World", str)

def test_triple_quoted_strings_are_strings():
    assert __ == isinstance("""Hello World""", str)

def test_triple_single_quoted_strings_are_strings():
    assert __ == isinstance('''Hello World''', str)

def test_raw_strings_are_strings():
    # raw string literals are specified using the r before the first quote
    # raw strings are used to avoid escaping backslashes, usually useful
    # when specifying things like window's paths which use backslash. e.g. r"c:\work\myfile.ini"

    assert __ == isinstance(r"Hello \n World", str)
    assert __ == len("\n")
    assert __ == len(r"\n")

    # write a non-raw string in the ___ to make both strings equal.
    assert ___ == r"Hello\n"

def test_single_quoted_strings_can_embed_double_quotes():
    first = 'The pilot said "Jump"'
    #ability to embed the other quote avoids the hassle of escaping quotes in strings
    second = "The pilot said \"Jump\""  #note back slash escaping of "
    are_equal = (first == second)
    assert __ == are_equal

def test_double_quoted_strings_can_embed_single_quotes():
    first = "The pilot said 'Jump'"
    second = 'The pilot said \'Jump\''  #note back slash escaping of '
    are_equal = (first == second)
    assert __ == are_equal

def test_triple_quoted_strings_can_have_both_single_and_double_quotes():
    """ Edit tq_str to make are_equal True """
    tq_str = """ Isn't the "Hobbit" great? """
    dq_str = "Isn't the \"Hobbit\" great?"
    are_equal = (tq_str == dq_str)
    assert __ == are_equal

def test_triple_quoted_strings_can_span_lines():
    tq_str = """Hello
World"""
    dq_str = "__"   # what is the double quoted form of tq_str
    assert (tq_str == dq_str)

def test_string_len():
    assert __ == len("Hello 'world'")
    assert __ == len('Hello \'world\'')

def test_triple_quoted_strings_can_span_lines2():
    string = """Hello
    World"""
    assert __ == isinstance(string, str)
    assert __ == len(string)

def test_strings_can_be_indexed():
    string = "Hello"
    assert __ == string[0]
    assert __ == string[1]
    assert __ == string[2]
    assert __ == string[3]
    assert __ == string[4]
    assert __ == string[-1]  # solves the common use case to iterate from end
    assert __ == string[-2]
    assert __ == string[-3]
    assert __ == string[-4]
    assert __ == string[-5]
    assert __ == string[-0]  # hint -0 is 0
    assert __ == len(string)
    try:
        out_of_bounds = string[5] #raises an error, we will revisit exceptions later
    except IndexError as ie:
        print(ie)
        assert ___  #make this True to proceed.

def test_chars_are_strings_too():
    string = "Hello"
    first_char = string[0]
    assert __ == type(first_char).__name__
    assert __ == type('a').__name__
    assert __ == type("a").__name__

def test_strings_are_immutable():
    """ strings in python cannot be modified unlike in C """
    string = "Hello"
    try:
        string[0] = "M"
    except TypeError as te:
        # run this test alone in py.test and observe the  'FAILURES' section and 'Captured stdout call' section
        # at the end. see the error messages in FAILURES and the print statements in "Captured stdout call"
        # Print statements can be added to failing tests and can be  observed in a similar manner
        print("Can you see me in pytest output?")
        print(te)
        assert ___    # after you observe, make this True to proceed.

def test_string_concat():
    assert __ == "Hello " + " world"
    assert __ == """Hello """ + 'world'
    assert __ == 'Hello ' + "world"


def test_string_slicing():
    """ Slicing creates new strings """
    string = "Hello world"
    #with begin : end
    assert __ == string[0:0]

    assert __ == string[0:2]
    assert __ == string[1:5]
    assert __ == string[1:-1]
    assert __ == string[2:-2]

    #with :end, note usage of negative indices as well.
    assert __ == string[:0]
    assert __ == string[:4]
    assert __ == string[:-1]

    #with begin:
    assert __ == string[0:]
    assert __ == string[4:]
    assert __ == string[-1:]

    #observe the invariant
    assert __ == string[:0] + string[0:]
    assert __ == string[:1] + string[1:]
    assert __ == string[:2] + string[2:]
    assert __ == string[:3] + string[3:]


def test_string_repeat():
    assert __ == "Hello" * 3
    assert __ == len("Hello " * 2)

def test_string_combine():
    """
    Use slicing to pass the assert.
    """
    hello = "Hello World"
    bye = "Goodbye moon"
    assert  bye[___] + hello[___]  == "Goodbye World"

def test_string_formatting():
    greeting = "Hello '{0}'".format("learner")
    assert __ == greeting

    truth = "{1} plus {1} makes {0}".format(__)
    assert truth == "one plus one makes two"

    stmt = "{name} is {age} years old".format(name="Ravi", age=25)
    assert __ == stmt

def test_string_formatting_literals():
    """
    literals which start with f are implicitly treated as expressions which are evaluated at runtime.
    This makes formatting a little more easier to understand.
    The full details are at: https://www.python.org/dev/peps/pep-0498/, read it to get an idea of how a feature
    is introduced into python.
    """
    value = 10
    assert ___ == f"value is: {value}"
    value = 20
    assert ___ == f"value is: {value + 10}"
    name, age = "Ramu", 20
    assert ___ == f"{name} is {age} years old!"

def test_string_membership():
    assert __ == 'c' in 'apple'  #is there a precedence issue here or something else?
    assert __ == 'a' in 'apple'
    assert __ == 'app' in 'apple'

def test_string_methods():
    word = "hello"
    assert ___ == word.capitalize()
    assert ___ == word.center(10)
    assert ___ == word.zfill(10)
    assert ___ == word.replace("l", "zebra")
    # you can experiment with all methods on string in console
    # by entering "something". (enter the dot too) to pop up all the available methods.



#Now apply what you have learnt above.
def rotate_right(input, count):
    """
    write a single line of code using what you have learnt in this lesson - slicing and concat
    assume 0 <= count <= len(input)
    """
    return __ # replace __ with the code

def test_rotate():
    assert 'hello' == rotate_right("hello", 0)
    assert 'ohell' == rotate_right("hello", 1)
    assert 'lohel' == rotate_right("hello", 2)
    assert 'llohe' == rotate_right("hello", 3)
    assert 'elloh' == rotate_right("hello", 4)
    assert 'hello' == rotate_right("hello", 5)

notes2 = '''
Read this after you finish the lesson:
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
'''

three_things_i_learnt = """
-
-
-
"""
