class Album:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, title, release_year, artist_id) -> None:
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
    
    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__
    def __eq__(self, other):
        if isinstance(other, Album):
            return (self.id == other.id and
                    self.title == other.title and
                    self.release_year == other.release_year and
                    self.artist_id == other.artist_id)
        return False

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"

