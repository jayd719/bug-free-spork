"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  Jashandeep Singh
ID:      169018282
Email:   sing8282@mylaurier.ca
Section: CP164 B
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
from Movie import Movie
from datetime import date

CURRENT_YEAR = int(date.today().year)


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    title = input('Title:')
    year_of_release = int(input('Year of release:'))
    director = input('Director:')
    rating = float(input('Rating:'))
    genres = read_genres()
    movie = Movie(title, year_of_release, director, rating, genres)
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """

    # Your code here
    line = line.split('|')
    genres = []
    l2 = line[4].split(',')
    for each in l2:
        genres.append(int(each))

    movie = Movie(line[0], int(line[1]), line[2], float(line[3]), genres)

    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """
    movies = []
    for line in fv:
        movies.append(read_movie(line.strip()))

    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    print(Movie.genres_menu())
    genres = []
    user = input('Enter a genre number (ENTER to quit):')
    while user != '' or len(genres) == 0:
        if user == '' and len(genres) == 0:
            print('Error: must have at least one genre')
        elif user.isdigit()is False:
            print('Error: not a positive number')
        else:
            if int(user) > len(Movie.GENRES) - 1:
                print(f'Error: input must be <= {len(Movie.GENRES)-1}')
            elif int(user) in genres:
                print('Error: genre already chosen')
            else:
                genres.append(int(user))
        user = input('Enter a genre number (ENTER to quit):')
    genres.sort()
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """

    if year >= Movie.FIRST_YEAR and year <= CURRENT_YEAR:
        # check if given year in valid
        ymovies = []
        for movie in movies:
            if movie.year == year:
                ymovies.append(movie.title)
    else:
        ymovies = f'Error: Invalid Year\nEnter Year between {Movie.FIRST_YEAR}-{CURRENT_YEAR}'

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    if rating <= Movie.MAX_RATING and rating >= Movie.MIN_RATING:
        # check if entered Rating is valid
        rmovies = []
        for movie in movies:
            if movie.rating >= rating:
                rmovies.append(movie.title)
    else:
        rmovies = f'Error: Invalid Rating\nEnter Rating Between {Movie.MIN_RATING}-{Movie.MAX_RATING}'

    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """
    i = 0
    index = None
    while i < len(Movie.GENRES):
        if genre == Movie.GENRES[i]:
            index = i
        i += 1
    if index is None:
        gmovies = f'Invalid Genre, Cannot Get List Of Movies\n\nSelect From Following:\n{Movie.genres_menu()}'
    else:
        gmovies = []
        for movie in movies:
            if index in movie.genres:
                gmovies.append(movie.title)
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    gmovies = []
    for movie in movies:
        if len(genres) == len(movie.genres):
            i = 0
            matchh = True
            while i < len(genres):
                if genres[i] not in movie.genres:
                    matchh = False
                i += 1
            if matchh:
                gmovies.append(movie.title)
    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    count_table = {}
    # using a dict/ Hash Table count frequency of each genre
    for movie in movies:
        for genre in movie.genres:
            if genre in count_table:
                count_table[genre] += 1
            else:
                count_table[genre] = 1
    # Convert Hash table into count list
    counts = []
    for gnr in range(0, len(Movie.GENRES)):
        if gnr in count_table:
            counts.append(count_table[gnr])
        else:
            counts.append(0)

    return counts
