import flask
from models import models
from forms import forms
from auth import acl

from flask_login import login_required, login_user, logout_user



app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "This is secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" 

models.init_app(app)

@app.route("/")
def index():
    db = models.db
    notes = db.session.execute(db.select(models.Note).order_by(models.Note.title)).scalars()
    return flask.render_template("index.html", notes=notes,)

@app.route("/login", methods=["GET","POST"])
def login():
    form = forms.LoginForm()

    if not form.validate_on_submit():
        return flask.render_template(
            "login.html",
            form=form
        )
    
    user = models.User.query.filter_by(username=form.username.data).first()

    if user and user.authenticate(form.password.data):
        login_user(user)
        return flask.redirect(flask.url_for("index"))
    
    return flask.redirect(flask.url_for("login", error="Invalud username or password"))
    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for("login"))

@app.route("/register", methods=["GET","POST"])
def register():
    form = forms.RegisterForm()
    if not form.validate_on_submit():
        return flask.render_template(
            "register.html",
            form=form,
        )
    user = models.User()
    form.populate_obj(user)

    role = models.Role.query.filter_by(name="user").first()
    if not role:
        role = models.Role(name="user")
        models.db.session.add(role)

    user.roles.append(role)
    user.password_hash = form.password.data
    models.db.session.add(user)
    models.db.session.commit()

    return flask.redirect(flask.url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)