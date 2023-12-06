from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

from blog.views import blog_blueprint
app.register_blueprint(blog_blueprint)

from main.views import main_blueprint
app.register_blueprint(main_blueprint)

from users.views import users_blueprint
app.register_blueprint(users_blueprint)


if __name__ == '__main__':
    app.run()

@app.errorhandler(404)
def function_name(not_found):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def function_name(internal_server_error):
    return render_template('errors/500.html'), 500