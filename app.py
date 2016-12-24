from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__, static_url_path='/static')
import re
from jinja2 import evalcontextfilter, Markup, escape

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result

@app.route("/", methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        content=""
        date=request.form['date']
        content=""""""+request.form['content']
        sub=request.form['sub']

        return render_template('generate.html', date=date, sub=sub, content=content)
        
    else:
        return render_template('home.html')

    

app.run(debug=True)