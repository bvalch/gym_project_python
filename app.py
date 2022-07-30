from flask import Flask,render_template
from controllers.gymclass_controller import gymclasses_blueprint
from controllers.gymsession_controller import gymsessions_blueprint
from controllers.member_controller import members_blueprint
app=Flask(__name__)
app.register_blueprint(gymclasses_blueprint)
app.register_blueprint(gymsessions_blueprint)
app.register_blueprint(members_blueprint)


@app.route('/')
def home():
    return render_template('homepage.html')

if __name__==('__main__'):
    app.run(debug=True)
