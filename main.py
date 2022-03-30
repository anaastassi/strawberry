from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def mainhtml():
    return render_template('mainhtml.html')
@app.route('/recipe1')
def recipe1():
    return render_template('recipe1.html')
if __name__ == '__main__':
    app.run(debug=True)