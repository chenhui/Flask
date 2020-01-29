from app import app
from .forms import LoginForm
from flask import render_template,flash,redirect
@app.route("/hello")
def hello_world():
    return "Hello world!!!"

@app.route("/index")
def index():
    user={"name":"chenlaoshi"}
    posts=[{'author':'Tom','body':'Beautiful'},
            {'author':'John','body':"Cool movie"}]
    return render_template("index.html",
                            title='Home',
                            user=user,
                            posts=posts
                           )

@app.route('/login',methods=['GET','POST'])                           
def login():
    my_form=LoginForm()
    if my_form.validate_on_submit():
        flash("form submit of openid:="+my_form.openid.data+" \br form submit of remember me := "+str(my_form.remember_me.data))
        return redirect("/index")
    return render_template('login.html',
        title='Sign in',
        iform=my_form,
        providers=app.config['OPENID_PROVIDERS'])