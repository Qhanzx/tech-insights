from flask import Flask, jsonify, render_template, request

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
    'id': 3,
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


@app.route('/posts/<int:post_id>')
def post(post_id):
  post = TROVES[post_id - 1]
  if not post:
    return "Not Found", 404
  return render_template('postpage.html', post=post, tech='Qhanzx')


@app.route('/add')
def add_post():
  return render_template('morepost.html', tech='Qhanzx')


@app.route('/posts/add', methods=['POST'])
def post_added():
  data = request.form
  add_trove(data)
  return render_template('post_submit.html', tech='Qhanzx', posts=data, db=TROVES)

#@app.route('/add_trove', methods=['POST'])
def add_trove(data):
    # Find the maximum id value in the current list and add 1 to it for the new id
    new_id = max([entry['id'] for entry in TROVES], default=0) + 1

    new_entry = {
        'id': new_id,
        'title': data['title'],
        'content': data['content'],
        'author': data['author']
    }
    TROVES.append(new_entry)
    #return f"New entry added successfully with ID: {new_id}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
