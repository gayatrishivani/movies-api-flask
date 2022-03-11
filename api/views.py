from flask import Blueprint, jsonify, request
from . import db 
from .models import Movie

main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST']) #creating movie
def add_moive():
    movie_data = request.get_json()

    new_movie = Movie(rating = movie_data['rating'], review = movie_data['review'])

    db.session.add(new_movie)
    db.session.commit()

    return 'done', 201

@main.route('/movies') #reading movie
def movies():
    movie_list = Movie.query.all()
    movies =[]
    for movie in movie_list:
        movies.append({'rating':movie.rating, 'review':movie.review})
    return jsonify({'movies': movies})

@main.route('/delete/<id>', methods=['DELETE']) #deleting the movie
def delete_movie(id):

    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()

    return 'done', 201

@main.route('/update', methods=['POST']) #updating movie
def update_movie():
    post_data = request.get_json()
    id = post_data['id']
    movie = Movie.query.get(id)
    movie.rating = post_data['rating']
    movie.review = post_data['review']
    db.session.commit()

    return 'Done',201

