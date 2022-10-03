from flask import Flask, jsonify, request
from storage import all_movies,liked_movies,disliked_movies,did_not_watch
from demographicFiltering import output
from contentBasedFiltering import get_recommendations

app = Flask(__name__)

@app.route("/get-movies")
def get_movies():
    movie_data = {
        "title":all_movies[0][8],
        "poster_link":all_movies[0][27],
        "release_date":all_movies[0][13],
        "duration":all_movies[0][15],
        "rating":all_movies[0][20],
        "overview":all_movies[0][9]
    }
    return jsonify({
        "data":movie_data,
        "status":"success!!"
    })

@app.route("/liked-movies", methods=["POST"])
def liked_movies():
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies.pop(0)

    return jsonify({
        "status":"success!!"
    }),201

@app.route("/disliked-movies", methods=["POST"])
def disliked_movies():
    movie = all_movies[0]
    disliked_movies.append(movie)
    all_movies.pop(0)

    return jsonfiy({
        "status":"success!!"
    })

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    movie = all_movies[0]
    did_not_watch.append(movie)
    all_movies.pop(0)

    return jsonify({
        "status":"success!"
    })

if __name__=="__main__":
    app.run()