import random
import webapp2

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):
        movies = ["The Big Lebowski", "Saving Pvt Ryan", "Snatch", "Big", "Walk Hard the Dewwy Cox's Story"]
        # TODO: make a list with at least 5 movie titles

        # TODO: randomly choose one of the movies, and return it

        return (random.choice(movies))

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>""Today's movie is " + movie + "</p>"

        tomorrow = self.getRandomMovie()
        tom = "<h1>Tomorrow's movie of the Day</h1>"
        tom += "<p>""Tomorrow's movie is " + tomorrow + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        self.response.write(content)
        self.response.write(tom)
app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
