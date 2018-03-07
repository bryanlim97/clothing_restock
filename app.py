"""Main file that calls upon all other files.""" 

from flask import Flask, request, redirect, render_template, url_for
from form import SignupForm
import crawler

app = Flask(__name__)
app.secret_key = "PLACEHOLDER"

@app.route('/', methods=['GET', 'POST'])
def index():
	"""Renders the homepage which is a form.
	
	If the action to the form is a POST: set the variables,
	call crawler, and redirect to the 'success' view once 
	execution is completed.
	
	"""
	form = SignupForm(request.form)
	if request.method == 'POST':
		product_name = request.form['product_name']
		size = request.form['size']
		product_url = request.form['product_url']
		crawler.crawl(product_name, size, product_url)
		return redirect(url_for('success'))	

	return render_template('index.html', form = form)

@app.route('/success', methods=['GET'])
def success():
	"""Render page once crawler is done executing."""
	return "Success! You should receive an email shortly."

if __name__ == "__main__":
    app.run(debug=True)
