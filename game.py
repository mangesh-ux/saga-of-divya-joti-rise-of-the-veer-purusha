from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    session['player_name'] = request.form.get('player_name')
    return redirect(url_for('game'))

@app.route('/game')
def game():
    player_name = session.get('player_name')
    if not player_name:
        return redirect(url_for('index'))
    return render_template('game.html', player_name=player_name)

if __name__ == '__main__':
    app.run(debug=True)
