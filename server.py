from flask import Flask, jsonify, request
from datetime import datetime
from db_connect import create_table, get_all_movies, add_movie, get_all_watched_movies, get_all_upcoming_movies, update_watched_movies, delete_movie, delete_watched

PORT=8080

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_all():
    movies = get_all_movies()
    return jsonify(movies)

@app.route('/movies/upcoming', methods=['GET'])
def get_upcoming():
    movies = get_all_upcoming_movies()
    return jsonify(movies)

@app.route('/movies/watched', methods=['GET'])
def get_watched():
    data = request.get_json()
    user_name = data['user_name']
    movies = get_all_watched_movies(user_name)
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def create_new():
    data = request.get_json()
    name = data['title']
    release_date = data['release_date']
    # TODO: Change implementation to enable user to add the release date as dd-mm-yyyy format
    date = datetime.strptime(release_date, "%d-%m-%Y")
    add_movie((name,date))
    return jsonify({'status':200, 'message':'Movie created with success.'})

@app.route('/movies/<string:title>/watch', methods=['POST'])
def add_to_watch_list(title):
    data = request.get_json()
    user_username = data['user_name']
    update_watched_movies(title, user_username)

    return jsonify({'status': 200, 'message':'Movie Updated with success.'})

@app.route('/movies/<string:title>/unwatch', methods=['DELETE'])
def unwatch_movie(title):
    data = request.get_json()
    user_username = data['user_name']
    delete_watched(title, user_username)

    return jsonify({'status': 200, 'message':'Movie Updated with success.'})

@app.route('/movies/<string:title>', methods=['DELETE'])
def delete(title):
    delete_movie(title)
    return jsonify({'status': 200, 'message':'Movie Deleted with success.'})

# Starting the service
print("Starting Server...")
if __name__ == '__main__':
    create_table()
    app.run(debug=True, host="0.0.0.0", port=PORT)
    print(f"Running on ${PORT}...")
