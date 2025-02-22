import flask
from models import models
from forms import forms
from auth import acl

from flask_login import login_required, login_user, logout_user, current_user


app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "This is secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" 

models.init_app(app)

@app.route("/about_me")
def about_me():
    return flask.render_template("about_me.html")

@app.route("/")
def main():
    return flask.render_template("main.html")

@app.route("/ports")
def ports():
    return flask.render_template("ports.html")

@app.route("/port_1")
def port_1():
    db = models.db
    notes = db.session.execute(db.select(models.Note).order_by(models.Note.title)).scalars()
    return flask.render_template("port_1.html", notes=notes)

@app.route("/port_2")
def port_2():
    db = models.db
    notes = db.session.execute(db.select(models.Note).order_by(models.Note.title)).scalars()
    return flask.render_template("port_2.html", notes=notes)

@app.route("/port_3")
def port_3():
    db = models.db
    notes = db.session.execute(db.select(models.Note).order_by(models.Note.title)).scalars()
    return flask.render_template("port_3.html", notes=notes)

@app.route("/port_4")
def port_4():
    db = models.db
    notes = db.session.execute(db.select(models.Note).order_by(models.Note.title)).scalars()
    return flask.render_template("port_4.html", notes=notes)

@app.route("/login", methods=["GET","POST"])
def login():

    # ถ้าผู้ใช้ล็อกอินแล้ว, เปลี่ยนเส้นทางไปหน้า index
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('main'))
    
    form = forms.LoginForm()
    if not form.validate_on_submit():
        return flask.render_template(
            "login.html",
            form=form
        )
    
    user = models.User.query.filter_by(username=form.username.data).first()

    if user and user.authenticate(form.password.data):
        login_user(user)
        return flask.redirect(flask.url_for("main"))
    
    return flask.redirect(flask.url_for("login", error="Invalud username or password"))
    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for("main"))

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

    return flask.redirect(flask.url_for("login"))

#TAGS AND NOTES

@app.route("/tags/<tag_views>")
def tags_view(tag_views):
    db = models.db
    tag = (
        db.session.execute(db.select(models.Tag).where(models.Tag.name == tag_views))
        .scalars()
        .first()
    )

    if not tag:
        # Handle case when tag doesn't exist
        return flask.render_template("tags_view.html", tag_views=tag_views, notes=[])

    notes = db.session.execute(
        db.select(models.Note).where(models.Note.tags.any(id=tag.id))
    ).scalars()

    return flask.render_template(
        "tags_view.html",
        tag_views=tag_views,
        notes=notes,
        tag=tag  # Make sure to pass the tag object to the template
    )


@app.route("/tags/<tag_id>/update_tags", methods=["GET", "POST"])
def update_tags(tag_id): #แก้ไข Tags ได้
    db = models.db
    tag = (
        db.session.execute(db.select(models.Tag).where(models.Tag.id == tag_id))
        .scalars()
        .first()
    )

    form = forms.TagForm()
    form_name = tag.name

    if not form.validate_on_submit():
        print(form.errors)
        return flask.render_template(
            "update_tags.html",
            form=form,
            form_name=form_name
            )

    note = models.Note(id=tag_id)
    form.populate_obj(note)
    tag.name = form.name.data
    db.session.commit()

    return flask.redirect(flask.url_for("index"))

@app.route("/tags/<tag_id>/delete_tags", methods=["GET", "POST"])
def delete_tags(tag_id):
    db = models.db
    tag = (
        db.session.execute(db.select(models.Tag).where(models.Tag.id == tag_id))
        .scalars()
        .first()
    )

    tag.name = ""
    db.session.commit()

    return flask.redirect(flask.url_for("index"))

@app.route("/notes/create_note", methods=["GET", "POST"])
def create_note():
    port_id = flask.request.args.get('port_id')  # Get port_id from the query string
    form = forms.NoteForm()

    if not form.validate_on_submit():
        print("error", form.errors)
        return flask.render_template(
            "create_note.html",
            form=form,
            port_id=port_id
        )

    # Create a new Note object
    note = models.Note()
    form.populate_obj(note)
    note.tags = []

    # Set the portfolio_id from the query string
    note.portfolio_id = port_id

    # Set the user_id from the current logged-in user
    if current_user.is_authenticated:
        note.user_id = current_user.id
    else:
        # Handle case when the user is not authenticated (e.g., redirect or error)
        return flask.redirect(flask.url_for('login'))  # Assuming you have a login route

    db = models.db
    for tag_name in form.tags.data:
        tag = (
            db.session.execute(db.select(models.Tag).where(models.Tag.name == tag_name))
            .scalars()
            .first()
        )

        if not tag:
            tag = models.Tag(name=tag_name)
            db.session.add(tag)

        note.tags.append(tag)

    db.session.add(note)
    db.session.commit()

    return flask.redirect(flask.url_for(f"port_{port_id}"))


@app.route("/tags/<tag_id>/update_note", methods=["GET", "POST"])
def update_note(tag_id):
    db = models.db
    notes = (
        db.session.execute(
            db.select(models.Note).where(models.Note.tags.any(id=tag_id)))
            .scalars()
            .first()
    )

    form = forms.NoteForm()
    form_title = notes.title
    form_description = notes.description
    if not form.validate_on_submit():
        print(form.errors)
        return flask.render_template(
            "update_note.html",
            form=form,
            form_title=form_title,
            form_description=form_description
        )
    
    note = models.Note(id=tag_id)
    form.populate_obj(note)
    notes.description = form.description.data
    notes.title = form.title.data
    db.session.commit()

    return flask.redirect(flask.url_for("index"))

@app.route("/tags/<tag_id>/delete_note", methods=["GET", "POST"])
def delete_note(tag_id):
    db = models.db
    notes = (
        db.session.execute(
            db.select(models.Note).where(models.Note.tags.any(id=tag_id))
        )
        .scalars()
        .first()
    )

    notes.description = ""
    db.session.commit()

    return flask.redirect(flask.url_for("index"))

@app.route("/tags/<tag_id>/delete", methods=["GET", "POST"])
def delete(tag_id):
    db = models.db

    notes = (
        db.session.execute(
            db.select(models.Note).where(models.Note.tags.any(id=tag_id))
        )
        .scalars()
        .first()
    )

    db.session.delete(notes)
    db.session.commit()
    return flask.redirect(flask.url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
