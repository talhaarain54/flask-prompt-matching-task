from flask import Flask
from views.prompt_view import prompt_blueprint

app = Flask(__name__)

app.register_blueprint(prompt_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
