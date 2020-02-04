@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)
