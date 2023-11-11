from flask import Flask, render_template, jsonify

app = Flask(__name__)

TROVES = [{
    'id': 1,
    'title': 'Java',
    'content': 'This site offers a vast selection of Java Essentials',
    'author': 'Matt'
}, {
    'id': 2,
    'title': 'Python',
    'content': 'This site offers a vast selection of Python Essentials',
    'author': 'Sam'
}, {
    'id': 1,
    'title': 'Cisco',
    'content': 'This site offers a vast selection of Cisco Essentials',
    'author': 'Vahid'
}]


@app.route('/')
def index():
  return render_template('index.html', posts=TROVES, tech='Qhanzx')


@app.route('/api/posts')
def troves():
  return jsonify(TROVES)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
