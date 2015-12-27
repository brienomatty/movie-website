import webbrowser


class Video():
    def __init__(self, title, duration_in_minutes):
        self.title = title
        self.duration_in_minutes = duration_in_minutes

class Movie(Video):
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Open movie trailer once clicked on
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


