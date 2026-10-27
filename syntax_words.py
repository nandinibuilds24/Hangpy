syntax_questions = [

    # ============================================================
    # LEVEL 1 — PYTHON FUNDAMENTALS
    # ============================================================

    {
        "level": 1,
        "topic": "print()",
        "question": "What is the syntax of print?",
        "answer": "print()",
        "hint": "It is used to display information on the screen.",
        "explanation": "print is used to display information on the screen when we want to show text, values, or results to the user.",
        "memory_line": "I want Python to say something out loud on the screen, so I use print(). 🗣️💻"
    },

    {
        "level": 1,
        "topic": "Variable Declaration",
        "question": "What is the syntax of variable declaration?",
        "answer": "variable_name=value",
        "hint": "Give a name to the information you want to store.",
        "explanation": "We use a variable when we want to store some information and use it later in the program.",
        "memory_line": "I want to keep something safe for later, so I give it a name and store it in a variable. 📦💻"
    },

    {
        "level": 1,
        "topic": "input()",
        "question": "What is the syntax of input?",
        "answer": 'input("enter something")',
        "hint": "Python uses this to ask the user for information.",
        "explanation": "The input() function allows Python to ask the user something and receive an answer.",
        "memory_line": "Python asks, I answer. 🗣️💻"
    },

    {
        "level": 1,
        "topic": "Comments",
        "question": "What is the syntax of a single-line comment?",
        "answer": "#comment",
        "hint": "It starts with a special symbol and Python does not execute it.",
        "explanation": "Comments are used to add notes or explanations in the code when we want to make the code easier to understand.",
        "memory_line": "I have something to explain, but I don't want Python to execute it, so I write a comment. 📝💻"
    },

    {
        "level": 1,
        "topic": "If Statement",
        "question": "What is the basic syntax of an if statement?",
        "answer": """if condition:
    statement""",
        "hint": "It checks whether a condition is true.",
        "explanation": "An if statement is used to make a decision when we want Python to execute something only if a condition is true.",
        "memory_line": "I want to do something only when it feels right, so I check the condition first. 🤔💻"
},
{
        "level": 1,
        "topic": "If-Else Statement",
        "question": "What is the basic syntax of an if-else statement?",
        "answer": """if condition:
    statement
    else:
        statement""",
        "hint": "It gives Python two possible paths.",
        "explanation": "An if-else statement is used to choose between two actions when one should happen if the condition is true and another if it is false.",
        "memory_line": "If things go my way, I choose one path; otherwise, I take the other. 🛤️💻"
    },

    {
        "level": 1,
        "topic": "For Loop",
        "question": "What is the basic syntax of a for loop?",
        "answer": """for item in sequence:
    statement""",
        "hint": "It goes through items one by one.",
        "explanation": "A for loop is used to repeat a block of code for each item in a sequence when we want to go through items one by one.",
        "memory_line": "I have many things to check, so I tell Python to go through them one by one. 🔁💻"
    },

    {
        "level": 1,
        "topic": "While Loop",
        "question": "What is the basic syntax of a while loop?",
        "answer": """while condition:
    statement""",
        "hint": "It repeats while a condition remains true.",
        "explanation": "A while loop is used to repeat a block of code as long as a condition remains true.",
        "memory_line": "I’ll keep doing this as long as the situation is still okay. 🔄💻"
    },


    # ============================================================
    # LEVEL 2 — DECISION MAKING & LOOP CONTROL
    # ============================================================

    {
        "level": 2,
        "topic": "elif",
        "question": "What is the basic syntax of an elif statement?",
        "answer": """if condition:
    statement
    elif condition:
        statement""",
        "hint": "Use it when the first if condition is false.",
        "explanation": "An elif statement is used when we want Python to check another condition if the previous if condition is false.",
        "memory_line": "The first choice didn't work, so let me check another one. 🤔➡️💻"
    },

    {
        "level": 2,
        "topic": "If-Elif-Else",
        "question": "What is the basic syntax of an if-elif-else statement?",
        "answer": """if condition:
    statement
elif condition:
    statement
else:
    statement""",
        "hint": "It lets Python choose between multiple possibilities.",
        "explanation": "An if-elif-else statement is used when we want Python to choose between multiple possibilities.",
        "memory_line": "I have several choices, so I'll check them one by one until I find the right path. 🛤️💻"
    },

    {
        "level": 2,
        "topic": "Nested If",
        "question": "What is the basic syntax of a nested if statement?",
        "answer": """if condition:
    if condition:
        statement""",
        "hint": "Think of an if statement inside another if statement.",
        "explanation": "A nested if statement is an if statement placed inside another if statement when we need to check an additional condition.",
        "memory_line": "One condition is true, but I need to check one more thing before I continue. 🤔🔍"
    },

    {
        "level": 2,
        "topic": "break",
        "question": "What is the syntax of the break statement?",
        "answer": "break",
        "hint": "It immediately stops a loop.",
        "explanation": "The break statement is used to immediately stop a loop when we no longer want the loop to continue.",
        "memory_line": "I've found what I was looking for, so I don't need to continue. 🛑💻"
    },

    {
        "level": 2,
        "topic": "continue",
        "question": "What is the syntax of the continue statement?",
        "answer": "continue",
        "hint": "It skips the current loop iteration.",
        "explanation": "The continue statement is used to skip the current iteration of a loop and move to the next iteration.",
        "memory_line": "I don't want to do this one, but I still want to continue with the others. ⏭️💻"
    },

    {
        "level": 2,
        "topic": "pass",
        "question": "What is the syntax of the pass statement?",
        "answer": "pass",
        "hint": "It means Python should do nothing here.",
        "explanation": "The pass statement is used when we want Python to do nothing in a particular block of code, usually when we plan to add code later.",
        "memory_line": "I don't have anything to do here yet, but I want Python to keep the place ready. 📝💻"
    },

    {
        "level": 2,
        "topic": "range()",
        "question": "What is the basic syntax of the range() function?",
        "answer": "range(start, stop, step)",
        "hint": "It generates a sequence of numbers.",
        "explanation": "The range() function is used to generate a sequence of numbers, commonly when we want to repeat something a specific number of times.",
        "memory_line": "I want Python to count for me, so I give it a range. 🔢💻"
    },

    {
        "level": 2,
        "topic": "return",
        "question": "What is the syntax of the return statement?",
        "answer": "return value",
        "hint": "A function uses it to send a result back.",
        "explanation": "The return statement is used inside a function when we want to send a value back to the place where the function was called.",
        "memory_line": "I did the work, and now I want to send the result back. 📤💻"
    },


    # ============================================================
    # LEVEL 3 — FUNCTIONS
    # ============================================================

    {
        "level": 3,
        "topic": "Function Definition",
        "question": "What is the basic syntax of a function definition?",
        "answer": """def function_name():
    statement""",
        "hint": "A function definition starts with a Python keyword.",
        "explanation": "A function is a reusable block of code that performs a specific task, and we use def to define it.",
        "memory_line": "I have a task I may need again, so I create a function for it. 🔧💻"
    },

    {
        "level": 3,
        "topic": "Function Arguments",
        "question": "What is the syntax of passing an argument to a function?",
        "answer": """def function_name(argument):
    statement""",
        "hint": "Put the information inside the function's parentheses.",
        "explanation": "Function arguments are the values we pass to a function when we call it, so the function can work with different data.",
        "memory_line": "I want my function to work with the information I give it, so I pass an argument. 📦💻"
    },

    {
        "level": 3,
        "topic": "Default Arguments",
        "question": "What is the basic syntax of a default argument?",
        "answer": """def function_name(argument=default_value):
    statement""",
        "hint": "Give the parameter a value that is used automatically.",
        "explanation": "A default argument is used when we want a function parameter to have a value that is automatically used when no argument is provided.",
        "memory_line": "If you don't give me a value, I'll use my own default one. ⚙️💻"
    },

    {
        "level": 3,
        "topic": "*args",
        "question": "What is the syntax of *args in a function?",
        "answer": """def function_name(*args):
    statement""",
        "hint": "It allows many positional arguments.",
        "explanation": "*args is used when we want a function to accept any number of positional arguments.",
        "memory_line": "I don't know how many values I'll receive, so I'll let the function accept as many as needed. 📦📦💻"
    },

    {
        "level": 3,
        "topic": "**kwargs",
        "question": "What is the syntax of **kwargs in a function?",
        "answer": """def function_name(**kwargs):
    statement""",
        "hint": "It allows many named arguments.",
        "explanation": "**kwargs is used when we want a function to accept any number of keyword arguments.",
        "memory_line": "I don't know how many named values I'll receive, so I'll let the function accept as many as needed. 🏷️💻"
    },

    {
        "level": 3,
        "topic": "Lambda",
        "question": "What is the basic syntax of a lambda function?",
        "answer": "lambda arguments: expression",
        "hint": "It creates a small anonymous function in one line.",
        "explanation": "A lambda function is a small anonymous function that can be written in a single line using the lambda keyword.",
        "memory_line": "I need a small function for a quick task, so I can write it in one line. ⚡💻"
    },

    {
        "level": 3,
        "topic": "Global Variable",
        "question": "What is the syntax of declaring a global variable?",
        "answer": "global variable_name",
        "hint": "Create it outside the function.",
        "explanation": "A global variable is a variable created outside a function that can be accessed from different parts of the program.",
        "memory_line": "I want this information to be available throughout my program, so I keep it outside the function. 🌍💻"
    },

    {
        "level": 3,
        "topic": "Local Variable",
        "question": "What is the syntax of declaring a local variable inside a function?",
        "answer": """def function_name():
    variable_name=value""",
        "hint": "Create the variable inside the function.",
        "explanation": "A local variable is a variable created inside a function and is normally available only within that function.",
        "memory_line": "This information is needed only for my current task, so I keep it inside the function. 🔒💻"
    },


    # ============================================================
    # LEVEL 4 — SCOPE & OBJECT-ORIENTED PROGRAMMING
    # ============================================================

    {
        "level": 4,
        "topic": "global Keyword",
        "question": "What is the syntax of using the global keyword?",
        "answer": "global variable_name",
        "hint": "Use it inside a function to modify a global variable.",
        "explanation": "The global keyword is used inside a function when we want to modify a global variable.",
        "memory_line": "I want to change the information that belongs to the whole program, so I tell Python it's global. 🌍🔄💻"
    },

    {
        "level": 4,
        "topic": "nonlocal",
        "question": "What is the syntax of using the nonlocal keyword?",
        "answer": "nonlocal variable_name",
        "hint": "It is used with a variable from an outer function.",
        "explanation": "The nonlocal keyword is used inside a nested function when we want to modify a variable belonging to the outer function.",
        "memory_line": "This variable belongs to the function outside me, and I want to change it from inside. 🔗💻"
    },

    {
        "level": 4,
        "topic": "Class Definition",
        "question": "What is the basic syntax of defining a class?",
        "answer": """class ClassName:
    #class body""",
        "hint": "A class is a blueprint for objects.",
        "explanation": "A class is a blueprint used to create objects that contain data and functions.",
        "memory_line": "I want to create objects with their own data and behavior, so I first create a class. 🏗️💻"
    },

    {
        "level": 4,
        "topic": "Object Creation",
        "question": "What is the syntax of creating an object from a class?",
        "answer": "object_name=ClassName()",
        "hint": "Call the class like a function.",
        "explanation": "An object is an instance of a class, and we create it by calling the class like a function.",
        "memory_line": "I have a blueprint, now I want to create something from it. 🏗️➡️📦"
    },

    {
        "level": 4,
        "topic": "Constructor",
        "question": "What is the basic syntax of a constructor in Python?",
        "answer": """def __init__(self):
    statement""",
        "hint": "It is automatically called when an object is created.",
        "explanation": "A constructor is a special method that is automatically called when an object is created. In Python, the constructor is commonly written using __init__().",
        "memory_line": "When a new object is born, I want to give it its starting information. 🎁💻"
    },

    {
        "level": 4,
        "topic": "Instance Variable",
        "question": "What is the syntax of declaring an instance variable?",
        "answer": "self.variable_name=value",
        "hint": "It belongs to a particular object and usually uses self.",
        "explanation": "An instance variable is a variable that belongs to a particular object and is usually created using self.",
        "memory_line": "Every object can have its own information, so I store it using self. 👤💻"
    },

    {
        "level": 4,
        "topic": "Instance Method",
        "question": "What is the basic syntax of an instance method?",
        "answer": """def method_name(self):
    statement""",
        "hint": "The first parameter is usually self.",
        "explanation": "An instance method is a function defined inside a class that works with an object's data and uses self as its first parameter.",
        "memory_line": "I want my object to perform an action using its own information. ⚙️💻"
    },

    {
        "level": 4,
        "topic": "Class Variable",
        "question": "What is the syntax of declaring a class variable?",
        "answer": """class ClassName:
    variable_name = value""",
        "hint": "The variable is written directly inside the class.",
        "explanation": "A class variable is a variable that belongs to the class and is shared by all objects of that class.",
        "memory_line": "I want all my objects to share the same information, so I keep it at the class level. 👥💻"
    },


    # ============================================================
    # LEVEL 5 — OOP & MODULES
    # ============================================================

    {
        "level": 5,
        "topic": "Class Method",
        "question": "What is the basic syntax of a class method?",
        "answer": """@classmethod
def method_name(cls):
    statement""",
        "hint": "It uses a decorator and cls.",
        "explanation": "A class method is a method that works with the class rather than a particular object and uses cls as its first parameter.",
        "memory_line": "I want to work with information that belongs to the whole class. 🏫💻"
    },

    {
        "level": 5,
        "topic": "Static Method",
        "question": "What is the basic syntax of a static method?",
        "answer": """@staticmethod
def method_name():
    statement""",
        "hint": "It does not use self or cls.",
        "explanation": "A static method is a method inside a class that does not depend on the class or object data.",
        "memory_line": "I want a useful function inside my class, but it doesn't need any object or class information. ⚙️💻"
    },

    {
        "level": 5,
        "topic": "Inheritance",
        "question": "What is the basic syntax of inheritance?",
        "answer": """class ChildClass(ParentClass):
    statement""",
        "hint": "Put the parent class inside parentheses.",
        "explanation": "Inheritance is used when one class wants to reuse the properties and methods of another class.",
        "memory_line": "I already have a useful class, so instead of starting from zero, I'll reuse what it has. 🧬💻"
    },

    {
        "level": 5,
        "topic": "Method Overriding",
        "question": "What is the basic syntax of method overriding?",
        "answer": """class ChildClass(ParentClass):
    def method_name(self):
        statement""",
        "hint": "The child class defines the same method again.",
        "explanation": "Method overriding is used when a child class provides its own version of a method that already exists in the parent class.",
        "memory_line": "The parent already has this action, but I want my child class to perform it differently. 🔄💻"
    },

    {
        "level": 5,
        "topic": "super()",
        "question": "What is the basic syntax of using super()?",
        "answer": "super().method_name()",
        "hint": "It lets a child class access something from its parent.",
        "explanation": "The super() function is used to access methods or the constructor of the parent class from the child class.",
        "memory_line": "I want to use something from my parent class, so I call super(). 👨‍👦💻"
    },

    {
        "level": 5,
        "topic": "Import Module",
        "question": "What is the syntax of importing a module?",
        "answer": "import module_name",
        "hint": "Use this to bring another module into your program.",
        "explanation": "The import statement is used to bring a module into our Python program so we can use its functions, classes, or variables.",
        "memory_line": "Someone has already written useful code, so I'll bring it into my program instead of writing it again. 📦💻"
    },

    {
        "level": 5,
        "topic": "from ... import",
        "question": "What is the syntax of importing a specific item from a module?",
        "answer": "from module_name import item_name",
        "hint": "Use from and import together.",
        "explanation": "The from ... import statement is used when we want to import a specific function, class, or variable from a module.",
        "memory_line": "I don't need the whole toolbox; I just need one particular tool. 🧰💻"
    },

    {
        "level": 5,
        "topic": "Module Alias",
        "question": "What is the syntax of giving an imported module an alias?",
        "answer": "import module_name as alias",
        "hint": "Use the keyword as to create a shorter name.",
        "explanation": "A module alias is a shorter name given to an imported module using the as keyword.",
        "memory_line": "The original name is long, so I'll give it a shorter name to use easily. ✂️💻"
    },


    # ============================================================
    # LEVEL 6 — ERRORS & FILE HANDLING
    # ============================================================

    {
        "level": 6,
        "topic": "Exception Handling",
        "question": "What is the basic syntax of exception handling?",
        "answer": """try:
    #code
except Exception:
    statement""",
        "hint": "Use try and except to safely handle errors.",
        "explanation": "Exception handling is used to handle errors that occur while a Python program is running, so the program can respond instead of stopping unexpectedly.",
        "memory_line": "Something went wrong, but I don't want my program to suddenly stop. 🛡️💻"
    },

    {
        "level": 6,
        "topic": "try-except-else",
        "question": "What is the basic syntax of try-except-else?",
        "answer": """try:
    #code
except Exception:
    statement
else:
    statement""",
        "hint": "The else block runs when no error occurs.",
        "explanation": "The try-except-else structure is used to handle errors and execute the else block when no error occurs.",
        "memory_line": "I'll try the code; if something goes wrong, I'll handle it. If everything is fine, I'll continue normally. 🛡️💻"
    },

    {
        "level": 6,
        "topic": "finally",
        "question": "What is the basic syntax of finally?",
        "answer": """try:
    #code
finally:
    #code that always executes""",
        "hint": "This block runs whether an error occurs or not.",
        "explanation": "The finally block is used when we want a block of code to execute whether an error occurs or not.",
        "memory_line": "No matter what happens, I want this final task to be done. 🔒💻"
    },

    {
        "level": 6,
        "topic": "raise",
        "question": "What is the syntax of the raise statement?",
        "answer": 'raise Exception("error message")',
        "hint": "It intentionally generates an exception.",
        "explanation": "The raise statement is used to intentionally generate an exception when a specific condition occurs.",
        "memory_line": "I know something is wrong, so I'll tell Python to raise an error. ⚠️💻"
    },

    {
        "level": 6,
        "topic": "assert",
        "question": "What is the syntax of the assert statement?",
        "answer": "assert condition",
        "hint": "It checks whether a condition is true.",
        "explanation": "The assert statement is used to check whether a condition is true. If the condition is false, Python raises an AssertionError.",
        "memory_line": "I believe this condition should be true, so I'll ask Python to check it. 🔍💻"
    },

    {
        "level": 6,
        "topic": "open()",
        "question": "What is the syntax of the open() function?",
        "answer": 'open("filename","mode")',
        "hint": "Use it before reading or writing a file.",
        "explanation": "The open() function is used to open a file so that we can read from or write to it.",
        "memory_line": "I want to work with a file, so first I need to open it. 📂💻"
    },

    {
        "level": 6,
        "topic": "read()",
        "question": "What is the syntax of the read() method?",
        "answer": "file.read()",
        "hint": "Use it to see the contents of an opened file.",
        "explanation": "The read() method is used to read the contents of an opened file.",
        "memory_line": "I have opened the file, and now I want to see what's inside. 👀📂"
    },

    {
        "level": 6,
        "topic": "write()",
        "question": "What is the syntax of the write() method?",
        "answer": 'file.write("text")',
        "hint": "Use it to put text or data into a file.",
        "explanation": "The write() method is used to add text or data to a file opened in write or append mode.",
        "memory_line": "I have something I want to save inside a file, so I'll write it there. ✍️📂"
    },


    # ============================================================
    # LEVEL 7 — FILES, COMPREHENSIONS & STRINGS
    # ============================================================

    {
        "level": 7,
        "topic": "with open()",
        "question": "What is the basic syntax of with open()?",
        "answer": """with open("filename","mode") as file:
    statement""",
        "hint": "It safely works with a file and handles closing automatically.",
        "explanation": "The with open() statement is used to work with a file while automatically handling the file closing after the block is finished.",
        "memory_line": "I want to use the file safely without worrying about closing it manually. 🔐📂"
    },

    {
        "level": 7,
        "topic": "List Comprehension",
        "question": "What is the basic syntax of list comprehension?",
        "answer": "[expression for item in sequence]",
        "hint": "It creates a list using an expression and a loop.",
        "explanation": "List comprehension is a concise way to create a new list using an expression and a loop.",
        "memory_line": "I want to create a list quickly without writing a complete loop separately. ⚡📋💻"
    },

    {
        "level": 7,
        "topic": "Dictionary Comprehension",
        "question": "What is the basic syntax of dictionary comprehension?",
        "answer": "{key: value for item in sequence}",
        "hint": "It creates key-value pairs using a loop.",
        "explanation": "Dictionary comprehension is a concise way to create a dictionary using an expression and a loop.",
        "memory_line": "I want to build a dictionary quickly from a sequence of values. 🗂️💻"
    },

    {
        "level": 7,
        "topic": "Set Comprehension",
        "question": "What is the basic syntax of set comprehension?",
        "answer": "{expression for item in sequence}",
        "hint": "It creates a set using an expression and a loop.",
        "explanation": "Set comprehension is a concise way to create a set using an expression and a loop.",
        "memory_line": "I want to create a set quickly without writing the complete loop separately. ⚡📦💻"
    },

    {
        "level": 7,
        "topic": "Slicing",
        "question": "What is the basic syntax of slicing?",
        "answer": "sequence[start:stop:step]",
        "hint": "It extracts part of a sequence.",
        "explanation": "Slicing is used to get a specific part of a sequence such as a string, list, or tuple.",
        "memory_line": "I don't need the whole sequence; I only want a part of it. ✂️💻"
    },

    {
        "level": 7,
        "topic": "String Formatting",
        "question": "What is the syntax of string formatting using format()?",
        "answer": '"{}".format(value)',
        "hint": "Use curly brackets as placeholders.",
        "explanation": "String formatting is used to insert values into a string and create formatted text.",
        "memory_line": "I have some information and I want to place it neatly inside my message. 📝💻"
    },

    {
        "level": 7,
        "topic": "F-String",
        "question": "What is the basic syntax of an f-string?",
        "answer": 'f"{variable}"',
        "hint": "It starts with the letter f and uses curly brackets.",
        "explanation": "An f-string is a convenient way to insert variables or expressions directly inside a string using {}.",
        "memory_line": "I want to place my variables directly into my sentence. 💬💻"
    },

    {
        "level": 7,
        "topic": "Arithmetic Operators",
        "question": "What is the syntax of arithmetic operators?",
        "answer": "a+b,a-b,a*b,a/b,a%b,a**b,a//b",
        "hint": "Think about mathematical operations.",
        "explanation": "Arithmetic operators are used to perform mathematical calculations such as addition, subtraction, multiplication, and division.",
        "memory_line": "I want Python to do a calculation for me, so I use arithmetic operators. ➕➖💻"
    },


    # ============================================================
    # LEVEL 8 — OPERATORS & BUILT-IN FUNCTIONS
    # ============================================================

    {
        "level": 8,
        "topic": "Comparison Operators",
        "question": "What is the syntax of comparison operators?",
        "answer": "a==b,a!=b,a>b,a<b,a>=b,a<=b",
        "hint": "They compare two values.",
        "explanation": "Comparison operators are used to compare two values and produce a Boolean result (True or False).",
        "memory_line": "I want Python to tell me whether two values are equal, greater, or smaller. ⚖️💻"
    },

    {
        "level": 8,
        "topic": "Logical Operators",
        "question": "What is the syntax of logical operators?",
        "answer": "a and b,a or b,not a",
        "hint": "Python provides three main logical operators.",
        "explanation": "Logical operators are used to combine or modify conditions. Python provides and, or, and not.",
        "memory_line": "I have more than one condition, so I need Python to connect them. 🔗💻"
    },

    {
        "level": 8,
        "topic": "Membership in",
        "question": "What is the syntax of the in operator?",
        "answer": "item in sequence",
        "hint": "It checks whether a value exists inside a collection.",
        "explanation": "The in operator is used to check whether a value exists inside a sequence or collection.",
        "memory_line": "I want to know whether this item is inside the collection. 🔍💻"
    },

    {
        "level": 8,
        "topic": "Identity is",
        "question": "What is the syntax of the is operator?",
        "answer": "a is b",
        "hint": "It checks whether two variables refer to the same object.",
        "explanation": "The is operator is used to check whether two variables refer to the same object in memory.",
        "memory_line": "I don't just want to know if they look equal; I want to know if they are the very same object. 👥💻"
    },

    {
        "level": 8,
        "topic": "map()",
        "question": "What is the basic syntax of map()?",
        "answer": "map(function,iterable)",
        "hint": "It applies a function to every item.",
        "explanation": "The map() function is used to apply a function to every item in an iterable.",
        "memory_line": "I have many values and I want the same operation performed on each one. 🔄💻"
    },

    {
        "level": 8,
        "topic": "filter()",
        "question": "What is the basic syntax of filter()?",
        "answer": "filter(condition,iterable)",
        "hint": "It keeps items that satisfy a condition.",
        "explanation": "The filter() function is used to select items from an iterable based on a condition.",
        "memory_line": "I have many values, but I only want the ones that satisfy my condition. 🔎💻"
    },

    {
        "level": 8,
        "topic": "zip()",
        "question": "What is the basic syntax of zip()?",
        "answer": "zip(iterable1,iterable2)",
        "hint": "It pairs corresponding items from iterables.",
        "explanation": "The zip() function is used to combine items from two or more iterables together based on their positions.",
        "memory_line": "I have related values in different lists, so I want Python to pair them together. 🤝💻"
    },

    {
        "level": 8,
        "topic": "enumerate()",
        "question": "What is the basic syntax of enumerate()?",
        "answer": "enumerate(iterable)",
        "hint": "It gives you both the position and the value.",
        "explanation": "The enumerate() function is used to get both the index and the value while looping through an iterable.",
        "memory_line": "I want each item along with its position. 🔢💻"
    },


    # ============================================================
    # LEVEL 9 — ADVANCED SYNTAX
    # ============================================================

    {
        "level": 9,
        "topic": "yield",
        "question": "What is the basic syntax of yield?",
        "answer": """def function_name():
    yield value""",
        "hint": "It produces values one at a time from a generator.",
        "explanation": "The yield statement is used inside a generator function to produce a value one at a time instead of returning all values at once.",
        "memory_line": "I don't want to give everything at once; I'll give you one value whenever you need it. 🎁💻"
    },

    {
        "level": 9,
        "topic": "Assignment Operators",
        "question": "What is the syntax of assignment operators?",
        "answer": "x=value,x+=value,x-=value,x*=value,x/=value",
        "hint": "They assign or update values in variables.",
        "explanation": "Assignment operators are used to assign values to variables and update existing values.",
        "memory_line": "I want to store or update a value, so I use an assignment operator. 📝💻"
    },

    {
        "level": 9,
        "topic": "Bitwise Operators",
        "question": "What is the syntax of bitwise operators?",
        "answer": "a&b,a|b,a^b,~a,a<<b,a>>b",
        "hint": "They operate on the binary bits of numbers.",
        "explanation": "Bitwise operators are used to perform operations directly on the binary representation of integers.",
        "memory_line": "I want Python to work directly with the bits, so I use bitwise operators. 0️⃣1️⃣💻"
    },

    {
        "level": 9,
        "topic": "Ternary / Conditional Expression",
        "question": "What is the basic syntax of a ternary conditional expression?",
        "answer": "value_if_true if condition else value_if_false",
        "hint": "It is a short one-line version of if-else.",
        "explanation": "A ternary or conditional expression is used to choose between two values based on a condition in a single line.",
        "memory_line": "I have two choices and one condition, so I'll make the decision in one line. 🔀💻"
    },

    {
        "level": 9,
        "topic": "Multiple Assignment / Unpacking",
        "question": "What is the syntax of multiple assignment?",
        "answer": "a,b,c=1,2,3",
        "hint": "Assign multiple values to multiple variables in one statement.",
        "explanation": "Multiple assignment allows us to assign multiple values to multiple variables in a single statement.",
        "memory_line": "I have several values, so I'll give each one its own variable at the same time. 📦📦💻"
    },

    {
        "level": 9,
        "topic": "List Methods",
        "question": "What is the basic syntax of using a list method?",
        "answer": "list_name.method()",
        "hint": "Call a method using the list name followed by a dot.",
        "explanation": "List methods are functions provided by Python to perform common operations on lists, such as adding, removing, or sorting items.",
        "memory_line": "I have a list and I want it to perform an action, so I call its method. 📋💻"
    },

    {
        "level": 9,
        "topic": "Tuple Unpacking",
        "question": "What is the syntax of tuple unpacking?",
        "answer": "a,b,c=tuple_name",
        "hint": "Take values from a tuple and assign them to separate variables.",
        "explanation": "Tuple unpacking is used to assign the individual values of a tuple to separate variables.",
        "memory_line": "The values are packed together, so I'll unpack them into separate names. 📦➡️📦"
    },

    {
        "level": 9,
        "topic": "Dictionary Methods",
        "question": "What is the basic syntax of using a dictionary method?",
        "answer": "dictionary_name.method_name()",
        "hint": "Call a method using the dictionary name and a dot.",
        "explanation": "Dictionary methods are built-in operations used to work with dictionary keys, values, and key-value pairs.",
        "memory_line": "I have a dictionary and I want to work with its data, so I use its methods. 🗂️💻"
    },


    # ============================================================
    # LEVEL 10 — FINAL PYTHON SYNTAX
    # ============================================================

    {
        "level": 10,
        "topic": "Set Methods",
        "question": "What is the basic syntax of using a set method?",
        "answer": "set_name.method_name()",
        "hint": "Call the method using the set name followed by a dot.",
        "explanation": "Set methods are built-in operations used to add, remove, combine, or compare set elements.",
        "memory_line": "I have a set and I want to perform an operation on it, so I use its method. 📦💻"
    },

    {
        "level": 10,
        "topic": "type()",
        "question": "What is the syntax of the type() function?",
        "answer": "type(value)",
        "hint": "It tells you what kind of data a value is.",
        "explanation": "The type() function is used to determine the data type of a value or object.",
        "memory_line": "I want Python to tell me what kind of value this is, so I use type(). 🔍💻"
    },

    {
        "level": 10,
        "topic": "len()",
        "question": "What is the syntax of the len() function?",
        "answer": "len(object)",
        "hint": "It tells you how many items are inside an object.",
        "explanation": "The len() function is used to find the number of items in a sequence or collection.",
        "memory_line": "I want to know how many things are here, so I use len(). 🔢💻"
    },

    {
        "level": 10,
        "topic": "isinstance()",
        "question": "What is the syntax of the isinstance() function?",
        "answer": "isinstance(object,class)",
        "hint": "It checks whether an object belongs to a particular class or type.",
        "explanation": "The isinstance() function is used to check whether an object is an instance of a specified class or type.",
        "memory_line": "I want Python to check what kind of object this belongs to, so I use isinstance(). 🔍🐍"
    },

    {
        "level": 10,
        "topic": "sorted()",
        "question": "What is the syntax of the sorted() function?",
        "answer": "sorted(iterable)",
        "hint": "It returns items in sorted order.",
        "explanation": "The sorted() function is used to return a new sorted list from an iterable.",
        "memory_line": "I want Python to arrange these items neatly, so I use sorted(). 📋💻"
    },

    {
        "level": 10,
        "topic": "* Unpacking",
        "question": "What is the syntax of * unpacking?",
        "answer": "*iterable",
        "hint": "A single star can unpack the values of an iterable.",
        "explanation": "The * operator can be used to unpack the individual items of an iterable into separate values or function arguments.",
        "memory_line": "These values are packed together, so I'll unpack them one by one. 📦➡️🐍"
    },

    {
        "level": 10,
        "topic": "** Dictionary Unpacking",
        "question": "What is the syntax of ** dictionary unpacking?",
        "answer": "**dictionary",
        "hint": "Two stars are used to unpack key-value pairs from a dictionary.",
        "explanation": "The ** operator is used to unpack the key-value pairs of a dictionary, commonly when passing keyword arguments to a function.",
        "memory_line": "I have named values packed inside a dictionary, so I'll unpack them as keyword arguments. 🗂️➡️🐍"
    },

    {
        "level": 10,
        "topic": "if __name__ == '__main__'",
        "question": "What is the syntax used to run code only when a Python file is executed directly?",
        "answer": """if __name__ == "__main__":
    statement""",
        "hint": "It checks whether the file is being run directly.",
        "explanation": "The if __name__ == '__main__' statement is used to make certain code run only when the Python file is executed directly, rather than when it is imported as a module.",
        "memory_line": "I want this code to run only when I start this file directly. ▶️🐍"
    }
]