#!/usr/bin/python3

from flask import Flask, render_template
import ssl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')



if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations('ca-crt.pem')
    context.load_cert_chain('server.crt', 'server.key')
    app.run(host = '0.0.0.0', port=8080, ssl_context=context)
