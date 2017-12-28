# clothing_restock
This is a simple web app that notifies a user of a restock of a particular clothing item specified by the user. Flask was used to generate the appropriate form, Selenium was used to interact with web URLs and collect meaningful data, and the OAuth2 client was used to send secure emails via GMail.

## How to Use
To use the app, simply modify the fields in `config.py`. Note: the default website is Urban Outfitters, although any can be used. To run the application, simply run `python app.py` and connect to localhost:5000 if you are on a Mac.

## Things to Note
Because Selenium interacts with HTML data and every website is unique, some level of research is involved to find the correct tags/names of HTML elements (use the inspect tool). Also, although this app was made with generality in mind note that certain sites behave differently from others. For example, some websites don't use dropdown menus for size selection but rather a grid system.
