from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG']=True



form = '''<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action='/rotate' method='post'>
      <label for='rot'>Rotate by: </label><br>
      <input type='text' id='rot' name='rot' value="{0}" /><br>
      <textarea id='text' name='text'>{1} </textarea>
      <input type='submit' value='submit'/> 
    </body>
</html>'''
def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_string_13(text):

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]

    return rotated

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]

def rotate_string(text, rot):

    rotated = ''

    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated

@app.route("/rotate", methods=["POST"])

def encrypt():
    text = request.form["text"]
    rot = int(request.form["rot"])
    final = rotate_string(text, rot)
    return form.format(rot, final)




@app.route("/")
def index():
    return form.format(0, " ")

app.run()