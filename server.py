from flask import Flask, jsonify, request
from datetime import datetime
from db_connect import create_table, get_all_movies, add_movie, get_all_watched_movies, get_all_upcoming_movies, update_watched_movies

PORT=8080

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_all():
    movies = get_all_movies()
    return jsonify(movies)

@app.route('/movies/upcoming', methods=['GET'])
def get_upcoming_movies():
    movies = get_all_upcoming_movies()
    return jsonify(movies)

@app.route('/movies/watched', methods=['GET'])
def get_watched_movies():
    movies = get_all_watched_movies()
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def create_new_movie():
    data = request.get_json()
    name = data['title']
    date = datetime.now().timestamp()
    add_movie((name,date))
    return jsonify({'status':200, 'message':'Movie created with success.'})

@app.route('/movies/<str:title>', methods=['UPDATE'])
def update_movie_status():
    title = request.args.get('title')
    update_watched_movies(title)
    return jsonify({'status': 200, 'message':'Movie Updated with success.'})

# Starting the service
print("Starting Server...")
if __name__ == '__main__':
    create_table()
    app.run(debug=True, host="0.0.0.0", port=PORT)
    print(f"Running on ${PORT}...")
