from flask import Flask, request, render_template_string

app = Flask(__name__)

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
    return f"Username: {username}, Password: {password}"


if __name__ == "__main__":
    app.run(debug=True)
