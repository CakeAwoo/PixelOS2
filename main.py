

from flask import Flask
app = Flask(__name__)

@app.route('/')

def bootscreen():
  
	
	data = '<title>PixelOS</title><style>body {background: black;}img { position: fixed;  top: 50%;  left: 55%;  margin-top: -50px;  margin-left: -100px; }    </style>    <img src="http://localhost:8000/logo.png"></img> <script>setTimeout(myFunction, 9000);function myFunction() {window.location.replace("http://localhost:5000/desktop/");}</script>'

	return (data)

@app.route('/desktop/')

def homescreen():
  

	data = '<title>PixelOS</title>  <style> body { background-image: url("https://cdn.discordapp.com/attachments/601626775554097162/656038768037593130/unknown.png");   -webkit-background-size: cover;  -moz-background-size: cover;  -o-background-size: cover;  background-size: cover;  margin: 0;  font-family: Arial, Helvetica, sans-serif;}.navbar {  overflow: hidden;  background-color: #235edc;  position: fixed;  bottom: 0;  width: 100%;}.navbar a {  float: left;  display: block;  color: #235edc;  text-align: center;  padding: 14px 16px;  text-decoration: none;  font-size: 17px;}.navbar a:hover {  background: #f1f1f1;  color: black;}.navbar a.active {  background-color: #3C983E;  color: white;}.main {  padding: 16px;  margin-bottom: 30px;}</style></head><body><div class="navbar">  <a href="#home" class="active">Start</a></div>'

	return (data)

if __name__ == '__main__':
    app.run(debug=True)
