import webapp2

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):
        # still just a hard-coded string for now
        return "The Big Lebowski"

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
