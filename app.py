#TEMPLATE
from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!

    artist_repository = ArtistRepository(self._connection)
    artists = artist_repository.all()

    for artist in artists:
        print(f"{artist.id}: {artist.name} ({artist.genre})")

if __name__ == '__main__':
    app = Application()
    app.run()