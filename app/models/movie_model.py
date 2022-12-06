class MovieModel(object):
    def __init__(self, id, name, date, hit):
        self.id = id
        self.name = name
        self.date = date
        self.hit = hit
        
    def __repr__(self) -> str:
        return "Movie(id={}, name={}, date={}, hit={})".format(self.id, self.name, self.date, self.hit)
