from flask import Flask, render_template

app = Flask(__name__)

menu = ["first_page", "second_page"]


@app.route("/")
def main_page():
    return render_template('main_page.html', title="Barsa", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)