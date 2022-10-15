from flask import Flask 
from flask import request
from detect import run
app = Flask(__name__)

@app.post("/upload")
def test():
    print('a')
    lfile = request.files['file']
    lfile.save(lfile.filename)
    x = run(source=lfile.filename)
    return f"{x}"

@app.get('/')
def r():
    return """<form action="/upload" method="post" enctype=multipart/form-data>
  <input type="file" id="file" name="file">
  <input type="submit">
</form>"""
