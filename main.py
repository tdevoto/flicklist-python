import webapp2


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        # TODO 1
        strike_form = """
        <form action="/crossoff" method="post">
            <label>
                I want to cross off
                <input type="text" name="strike-movie"/>
                from my watchlist.
            </label>
            <input type="submit" value="Cross Off"/>
        </form>

        """# Include another form so the user can "cross off" a movie from their list.


        # TODO 4 (Extra Credit)
        # modify your form to use a dropdown (<select>) instead a
        # text box (<input type="text"/>)
        off_dropdown = """
        <form action="/select_off" method="post">
            <select name = "selectoffmovie">
                <option> Movie 1 </option>
                <option> Movie 2 </option>
                <option> Movie 3 </option>
                <option> Movie 4 </option>
            <input type="submit" value="Axe it"/>
        </form>

        """

        content = page_header + edit_header + add_form + strike_form + off_dropdown + page_footer
        self.response.write(content)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)


# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".
class CrossOffMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/crossoff'
        e.g. www.flicklist.com/crossoff
    """

    def post(self):
        # look inside the request to figure out what the user typed
        strike_movie = self.request.get("strike-movie")

        # build response content
        strike_movie_element = "<strike>" + strike_movie + "</strike>"
        sentence = strike_movie_element + " has been crossed off of your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)

class selectOff(webapp2.RequestHandler):
    """ Handles requests coming in to '/crossoff'
        e.g. www.flicklist.com/crossoff
    """

    def post(self):
        # look inside the request to figure out what the user typed
        dropdown = self.request.get("selectoffmovie")

        # build response content
        dropdownoff = "<strike>" + dropdown + "</strike>"
        sentence = dropdownoff + " has been crossed off of your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)

# TODO 3
# Include a route for your cross-off handler, by adding another tuple to the list below.
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/crossoff', CrossOffMovie),
    ('/select_off', selectOff)
], debug=True)
