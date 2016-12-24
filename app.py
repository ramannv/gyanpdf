from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        date=str(request.form['date'])
        content=str(request.form['content'])
        sub=str(request.form['sub'])

        return render_template('generate.html', date=date, sub=sub, content=content)
    else:
        return render_template('home.html')

app.run(debug=True)