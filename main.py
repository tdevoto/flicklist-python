import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # list of movies to select from
        movies = ["The Big Lebowski", "Blue Velvet", "Toy Story", "Star Wars", "Amelie"]

        # randomly choose one of the movies
        randomIdx = random.randrange(len(movies))

        return movies[randomIdx]

    def get(self):
        movie = self.getRandomMovie()

        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
