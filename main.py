from flask import Flask, jsonify, request
from storage import all_movies,liked_movies,disliked_movies,notwatch
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-art")
def getmovies():
    movie_data = {
        "title":all_art[0][19],
        "poster_link":all_art[0][27],
        "release_date":all_art[0][30] or "NA",
        "duration":all_art[0][15],
        "rating":all_art[0][20],
        "overview":all_art[0][9]
    }
    return jsonify({
        "data":movie_data,
        "status":"success"
    })

@app.route("/liked-art", methods = ["POST"])
def likedmovies():
    movie = all_art[0]
    liked_art.append(movie)
    all_art.pop(0)
    return jsonify({
        "status":"success"
    },400)

@app.route("/unliked-art", methods = ["POST"])
def dislikedmovies():
    movie = all_art[0]
    disliked_art.append(movie)
    all_art.pop(0)
    return jsonify({
        "status":"success"
    },400)

if __name__ == "__main__":
    app.run(debug = True)