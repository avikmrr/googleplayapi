# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "en_IN" # can be en_US, fr_FR, ...
ANDROID_ID      = "3b5b07b71d80309d" # "xxxxxxxxxxxxxxxx"
GOOGLE_LOGIN    = "dstsecacc@gmail.com" # "username@gmail.com"
GOOGLE_PASSWORD = "Securityresearchers"
AUTH_TOKEN      = None # "yyyyyyyyy"

# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

