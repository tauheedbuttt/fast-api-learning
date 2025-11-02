Learning FastAPI from python

# Setting up virtual environment

1 - python -m venv .venv (creates)
2 - source .venv/bin/activate (activates)
3 - which python ( optional to check status )

# Creating server

1 - pip install "fastapi[standard]" (install packages)
2 - pip install -r requirements.txt ( uses existing configuration to setup server, optional )
3 - create main.py, import fast api and create app = FastAPI() just like express
4 - use @app.get to define endpoint

# Types

1 - use typing package
2 - almost same as js
3 - define and document fields using annotated
4 - Optional and Union are almost the same things

# Basics

1 - Enums - uses base class and inheritance
2 - {path_string:path} pass strings as /path/to/file
3 - query params bool: 1, True, true, on, yes
4 - query further validation with Annotated
5 - AfterValidator for custom validation function
6 - Passing json as query and using class base validation for querys
7 - use Annotated[data type, request part (query, body etc.)]
9 - return type with -> data_type
10 - FOrm() for formdata
11 - File() for files
12 - Error handling with raise
