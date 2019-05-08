import os
from flask_script import Manager, prompt_bool, Shell, Server
from termcolor import colored
from app import app
from app import app
from flask import render_template, request, url_for


manager = Manager(app)
#

manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080))
    )
                    )


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()
