from csv import DictReader
from django.core.management import BaseCommand

# Import the model
from reviews.models import Category, Genre, Review, Title, GenreTitle, Comment

MODELS = (
    Review,
    Title, GenreTitle, Comment
)

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from .csv"

    def handle(self, *args, **options):

        for model in MODELS:
            if model.objects.exists():
                print('data already loaded...exiting.')
                print(ALREDY_LOADED_ERROR_MESSAGE)
                return

        # Show this before loading the data into the database
        print("Data successfuly loading")

        # Code to load the data into database

#        for row in DictReader(open('./static/data/genre_title.csv')):
 #           genre_title = GenreTitle(
  #              id=row['id'], title=row['title_id'], genre=row['genre_id'],
   #         )
    #        genre_title.save()

        for row in DictReader(open('./static/data/titles.csv')):
            titles = Title(
                id=row['id'], name=row['name'], year=row['year'],
                description=row['description'], rating=row['rating'],
                category=row['category'], genre=row['genre'],
            )
            titles.save()

        for row in DictReader(open('./static/data/reviews.csv')):
            reviews = Review(
                id=row['id'], text=row['text'], author=row['author'],
                title=row['title'], score=row['score'],
                created=row['pub_date'],
            )
            reviews.save()

        for row in DictReader(open('./static/data/comments.csv')):
            comments = Comment(
                id=row['id'], review_id=row['review_id'], author=row['author'],
                text=row['text'], created=row['pub_date'],
            )
            comments.save()
