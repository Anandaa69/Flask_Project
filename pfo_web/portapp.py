import flask
from models import models
from forms import forms
app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" 
models.init_app(app)

@app.route("/")
def index():
    db = models.db
    notes = db.session.execute(db.select(models.Note).order_by(models.Note.title)).scalars()
    return flask.render_template("index.html", notes=notes,)

if __name__ == "__main__":
    app.run(debug=True)