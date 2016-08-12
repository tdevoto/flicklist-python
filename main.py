import webapp2
import random

class Index(webapp2.RequestHandler):

    def get(self):
        response = "<h1>FlickList</h1>"
        response += "<h3>Add a new movie to your Watchlist:</h3>"

        # create a form for user to add a new movie
        response += """
        <form action="/addmovie" method="post">
            <input type="text" name="new-movie"/>
            <input type="submit" value="Add"/>
        </form>
        """

        # TODO 1
        # Add another form so the user can delete a movie from their list.


        # TODO 4
        # Once you have the basic version working, modify the form so that it uses
        # a dropdown <select> instead of a text box <input type="text">.


        self.response.write(response)


class AddMovie(webapp2.RequestHandler):

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new_movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"
        header = "<h1>Thanks!</h1>"
        response = header + "<p>" + sentence + "</p>"

        self.response.write(response)


# TODO 2
# Add a new handler class called DeleteMovie, to receive and handle the delete request.
# The user should see a message like "Thanks! ___ has been deleted from you watchlist".



# TODO 3
# Add your delete route to the app, by adding another tuple to the list below.
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/addmovie', AddMovie)
], debug=True)
