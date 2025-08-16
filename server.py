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
    # Check if there is a body in the request
    if request.content_type != 'application/json':
        return jsonify({'status': 415, 'message': 'Content-Type must be application/json'}), 415
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'status': 400, 'message': 'Invalid JSON in request body'}), 400
    user_name = data.get('user_name')
    if not user_name:
        return jsonify({'status': 400, 'message': 'user_name is required'}), 400
    movies = get_all_watched_movies(user_name)
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def create_new():
    data = request.get_json()
    movie_title = data['title']
    release_date = data['release_date']
    date = datetime.strptime(release_date, "%d-%m-%Y")
    add_movie((movie_title,date))
    return jsonify({'status':200, 'message':'Movie created with success.'})

@app.route('/movies/<int:movie_id>/watch', methods=['POST'])
def add_to_watch_list(movie_id):
    data = request.get_json()
    user_username = data['user_name']
    update_watched_movies(movie_id, user_username)

    return jsonify({'status': 200, 'message':'Movie Updated with success.'})

@app.route('/movies/<id:movie_id>/unwatch', methods=['DELETE'])
def unwatch_movie(movie_id):
    data = request.get_json()
    user_username = data['user_name']
    delete_watched(movie_id, user_username)

    return jsonify({'status': 200, 'message':'Movie Updated with success.'})

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete(movie_id):
    delete_movie(movie_id)
    return jsonify({'status': 200, 'message':'Movie Deleted with success.'})

# Starting the service
print("Starting Server...")
if __name__ == '__main__':
    create_table()
    app.run(debug=True, host="0.0.0.0", port=PORT)
    print(f"Running on ${PORT}...")
