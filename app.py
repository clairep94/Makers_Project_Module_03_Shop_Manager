#TEMPLATE
from lib.database_connection import DatabaseConnection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository

class Application():
    def __init__(self) -> None:
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!\n")
        user_choice = input("What would you like to do?\n1 - List all albums\n2 - List all artists\n\nEnter your choice: ")
        if user_choice == "1":
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()

            for album in albums:
                print(f"{album.id} - {album.title} ({album.release_year})")
        
        elif user_choice == "2":
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()

            for artist in artists:
                print(f"{artist.id} - {artist.name}, {artist.genre}")

        else:
            raise Exception("Invalid choice. Please try again.")

if __name__ == '__main__':
    app = Application()
    app.run()