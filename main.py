import webapp2

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):
        # for now, just return a hard-coded string
        return "The Big Lebowski"

    def get(self):
        movie = self.getRandomMovie()

        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<p>" + movie + "</p>"

        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
