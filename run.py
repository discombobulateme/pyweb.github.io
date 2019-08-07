#!flask/bin/python
from app import app
HOST='127.0.0.1'
# Your ip address may be different
app.run(host=HOST, debug=True)
