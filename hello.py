from flask import Flask, render_template
app = Flask(__name__)


class item:
    def __init__(self, name):
        self.name = name


nimi = "Heikki Pulli"

lista = [3, "moi", 4]

esineet = []
esineet.append(item("pekka"))
esineet.append(item("juha"))
esineet.append(item("eetu"))


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)


if __name__ == "__main__":
    app.run(debug=True)
