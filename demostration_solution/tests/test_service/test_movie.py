from unittest.mock import MagicMock

import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    first_movie = Movie(
        id=1,
        title='First_movie',
        description='',
        trailer='None',
        year=2000,
        rating=0,
        genre_id=2,
        director_id=3
    )
    second_movie = Movie(
        id=2,
        title='Second_movie',
        description='',
        trailer='None',
        year=2002,
        rating=0,
        genre_id=3,
        director_id=4
    )
    third_movie = Movie(
        id=3,
        title='Third_movie',
        description='',
        trailer='None',
        year=2003,
        rating=0,
        genre_id=4,
        director_id=5
    )

    movie_dao.get_one = MagicMock(return_value=first_movie)
    movie_dao.get_all = MagicMock(return_value=[first_movie, second_movie, third_movie])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movie_service.get_all()

        assert len(movie) > 0

    def test_create(self):
        movie_d = {
            'title': 'title',
            'description': 'description',
            'trailer': 'trailer',
            'year': 2003,
            'rating': 0.5,
            'genre_id': 2,
            'director_id': 3
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            'id': 1,
            'title': 'title',
            'description': 'description',
            'trailer': 'trailer',
            'year': 2003,
            'rating': 0.5,
            'genre_id': 2,
            'director_id': 3
        }
        self.movie_service.update(movie_d)
