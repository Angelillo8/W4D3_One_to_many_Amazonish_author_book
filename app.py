from flask import Flask, render_template

from controllers.books_controller import tasks_blueprint

app = Flask(__name__)

app.register_blueprint(tasks_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)