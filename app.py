from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    products = [
        {"name":"Laptop","price":50000},
        {"name":"Mouse","price":500},
        {"name":"Keyboard","price":1000},
        {"name":"Monitor","price":15000}
    ]
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run()
