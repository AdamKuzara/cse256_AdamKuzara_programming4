from flask import Flask, request, render_template_string
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def login_form():
    form_html = """
     <form method="POST" action="/login">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <input type="submit" value="Login">
    </form>
    """
    return render_template_string(form_html)

@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # If statements for input validation.
    if len(password) < 8:
        return "Invalid password. Must be at least 8 characters long."
    if not any(char.isalpha() for char in password):
        return "Invalid password. Must include letters."
    if not any(char.isdigit() for char in password):
        return "Invalid password. Must include numbers."
    # Encrypted password is stored - I tried to use generate_password_hash but I kept getting an error.
    # I looked up a different way to do salting (https://heynode.com/blog/2020-04/salt-and-hash-passwords-bcrypt) but decided not to try and do it.
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    # Feedback for validation when comparing the plain-text password to the hashed/encrypted password
    if bcrypt.check_password_hash(hashed_password, password):
        validation_message = "Password is valid!"
    else:
        validation_message = "Invalid password."
    return (f"Username: {username}, Password: {password}<br>"
            f"{validation_message}")

if __name__ == "__main__":
    app.run(debug=True)
