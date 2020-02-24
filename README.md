# Brief
A program that prompts the user for an input with How can I help you? <br/>
User input should be one of three possible kinds:
+ Please convert ***
+ Please convert *** using ***
+ Please convert *** minimally <br/>

If user input is not of this form, with any occurrence of *** an arbitrary nonempty sequence of nonspace
symbols, then the program should print out:
+ Sorry, I don\'t get what you want. <br/>
and stop.
# First Input Type
In case the user inputs Please convert ***, then *** should be either a strictly
positive integer (whose representation should not start with 0) that can be converted to a Roman number (hence
be at most equal to 3999), or a valid Roman number; otherwise, the program should print out:
+ Hey, ask me something that\'s possible to do! <br/>

and stop .If the input is as expected, then the program should perform the conversion, from Arabic to Roman
or from Roman to Arabic, and print out the result in the form:
+ Sure! It is *** <br/>
# Second Input Type
In case the user inputs Please convert *** using ***, then the first ***
should be a strictly positive integer (whose representation should not start with 0) or a sequence of (lowercase
or uppercase) letters and the second *** should be a sequence of distinct (lowercase or uppercase) letters.
Moreover,
+ the second *** is intended to represent a sequence of so-called generalised Roman symbols, the classical
Roman symbols corresponding to the sequence MDCLXVI, whose rightmost element is meant to represent
1, the second rightmost element, 5, the third rightmost element, 10, etc.;
+ if it is not an integer, the first *** is intended to represent a so-called generalised Roman number,
that is, a sequence of generalised Roman symbols that can be decoded using the provided sequence of
generalised Roman symbols similarly to the way Roman numbers are represented. <br/>

If that is not the case, of if it is not possible to convert the first *** from Arabic to generalised Roman or from
generalised Roman to Arabic, then the program should print out:
+ Hey, ask me something that\'s possible to do! <br/>

and stop. If the input is as expected and the conversion can be performed, then the program should indeed
perform the conversion, from Arabic to generalised Roman or from generalised Roman to Arabic, and print out
the result in the form:
+ Sure! It is *** <br/>
# Third Input Type
In case the user inputs Please convert *** minimally, then *** should be a
sequence of (lowercase or uppercase) letters. The program will try and view *** as a generalised Roman number
with respect to some sequence of generalised Roman symbols. If that is not possible, then the program should
print out:
+ Hey, ask me something that's not impossible to do!<br/>

and stop. Otherwise, the program should find the smallest integer that could be converted from ***, viewed
as some generalised Roman number, to Arabic, and output a message of the form:
+ Sure! It is *** using ***

# Examples
+ $ python3 roman_arabic.py <br/>
How can I help you? please convert 35 <br/>
Sorry, I don't get what you want. <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert 4000 <br/>
Hey, ask me something that's possible to do! <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert IIII <br/>
Hey, ask me something that's possible to do! <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert 035 <br/>
Hey, ask me something that's possible to do! <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert 35 <br/>
Sure! It is XXXV <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert 1982 <br/>
Sure! It is MCMLXXXII <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert MCMLXXXII <br/>
Sure! It is 1982 <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? please convert 123 ussing ABC<br/>
Sorry, I don't get what you want. <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert XXXVI using IVX <br/>
Hey, ask me something that's possible to do! <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert XXXVI using XWVI <br/>
Hey, ask me something that's possible to do! <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert XXXVI using XABVI <br/>
Sure! It is 306 <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert ABCDEFGHIJKLMNOPQRST using AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStT <br/>
Sure! It is 11111111111111111111 <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert 1900604 using LAQMPVXYZIRSGN <br/>
Sure! It is AMAZING <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert ABAA minimally <br/>
Hey, ask me something that's possible to do! <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert ABCDEFA minimally <br/>
Hey, ask me something that's possible to do! <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert VI minimally <br/>
Sure! It is 4 using IV <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert MDCCLXXXVII minimally <br/>
Sure! It is 1787 using MDCLXVI <br/>
+ $ python3 roman_arabic.py <br/>
How can I help you? Please convert ABCADDEFGF minimally <br/>
Sure! It is 49269 using BA_C_DEF_G <br/>
