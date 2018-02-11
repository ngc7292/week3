from flask import *

app = Flask(__name__)

@app.route('/')
@app.route('/ngc')
@app.route('/admin')
@app.route('/login')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='ngc'):
    return render_template('index.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    template = '''
{%% block body %%}
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>
    </div>
{%% endblock %%}
''' % (request.url)
    return render_template_string(template), 404

if __name__ == "__main__":
    app.run()