from flask import Flask, render_template, request

import random
import string

app = Flask(__name__)

# Generate encryption/decryption key
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

@app.route("/")
def index():ls
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    plain_text = request.form["plain_text"]
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    return render_template("index.html", encrypted_message=cipher_text, decrypted_message=None)

@app.route("/decrypt", methods=["POST"])
def decrypt():
    cipher_text = request.form["cipher_text"]
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    return render_template("index.html", encrypted_message=None, decrypted_message=plain_text)

if __name__ == "__main__":
    app.run(debug=True)
