import json
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

# Define the path for the TMDB API request
TMDB_TRENDING_PATH = 'trending/movie/week'
TMDB_SEARCH_API_REQUEST = f'https://api.themoviedb.org/3/{TMDB_TRENDING_PATH}?'

################################################################################################################################
# functions
###########################################################################################
# Define the function to get the weekly trending movies
# from the TMDB API using the requests library
# returns a json object
def get_weekly_trending_movies():
    response = requests.get(
        TMDB_SEARCH_API_REQUEST,
        params={
            'api_key': os.getenv('TMDB_API_KEY')
        }
    )
    return response.json()

###########################################################################################
# Prints the title and vote average of each movie in the list of dictionaries.
# - movie_titles__votes: A list of dictionaries containing the title and vote average of a movie.
def print_movie_voter_avg_table(movie_titles__votes):
    # Define the format for the header and rows to ensure alignment
    header_format = "{:<50} | {:>10}"
    row_format = "{:50} | {:10}"

    # Print the header with proper alignment
    header = header_format.format("Title", "Vote Average")
    print(header)
    print("-" * len(header))  # Print a divider

    for movie in movie_titles__votes:
        # Format each line as a table row with fixed column widths
        row = row_format.format(
            movie['title'], 
            str(movie['vote_average'])
        )
        print(row)

###########################################################################################
# Prints the title, popularity, and vote count of
# each movie in the weekly trending movies JSON object.
# - weekly_trending_movies_json: A JSON object containing the weekly trending movies data.
def print_movie_details_table(weekly_trending_movies_json):
    # Define the format for the header and rows to ensure alignment
    header_format = "{:<50} | {:>10} | {:>10}"
    row_format = "{:50} | {:10} | {:10}"

    # Print the header with proper alignment
    header = header_format.format("Title", "Popularity", "Vote Count")
    print(header)
    print("-" * len(header))  # Print a divider

    for movie in weekly_trending_movies_json['results']:
        if movie['media_type'] == 'movie':
            # Format each line as a table row with fixed column widths
            row = row_format.format(
                movie['title'], 
                str(movie['popularity']), 
                str(movie['vote_count'])
            )
            print(row)

###########################################################################################
# Prints the title, popularity, and vote count of 
# each movie in the weekly trending movies JSON object.
# - weekly_trending_movies_json: A JSON object containing the weekly trending movies data.
def print_movie_details(weekly_trending_movies_json):

    for movie in weekly_trending_movies_json['results']:
        if movie['media_type'] == 'movie':
            print(f"Title: {movie['title']}")
            print(f"Popularity: {movie['popularity']}")
            print(f"Vote Count: {movie['vote_count']}")
            print("\n")

###########################################################################################
# Extracts titles and vote averages for movies from a JSON object.
# - movies_json: A JSON object containing movie data.
# - Returns: a list of dictionaries, each containing the title and vote average of a movie.
def extract_movie_titles_and_vote_average(movies_json):
    movie_details_list = []
    for movie in movies_json['results']:
        if movie['media_type'] == 'movie':
            movie_details = {
                'title': movie['title'],
                'vote_average': movie['vote_average']
            }
            movie_details_list.append(movie_details)
    
    return movie_details_list

###########################################################################################
################################################################################################################################
# main
################################################################################################################################
# Encodes response into a python json dictionary.
weekly_trending_movie_json_data = get_weekly_trending_movies()
#print(weekly_trending_movie_json_data)

# Convert json_data to a formatted pretty
# json string that is easy for humans to read.
# Mouse over function to get definition of indent and sort_keys
pretty_json_data = json.dumps(weekly_trending_movie_json_data, indent=4, sort_keys=True)
#print(pretty_json_data)

weekly_trending_movie_object = weekly_trending_movie_json_data
# Add Parsing Code Here



################################################################################################################################
'''part one'''
print('\n\n\n\nPart 1')
print('printout of movies\' titles, popularity, vote count \n\n\n\n')
# print out the following in formatted form:
# The titles, popularity and vote_count of the media type that are returned for movies
# - you choose the format
################################################################################################################################

print_movie_details_table(weekly_trending_movie_json_data)



################################################################################################################################
'''part two'''
print('\n\n\n\nPart 2')
print('printout of movies\' voter averages sorted\n\n\n\n')
# Sort and print out the following in formatted form:
# The titles and vote_average in order of their vote_average for movies.
# - consider using  sorted() or list.sort()
# - you choose the format
################################################################################################################################

movies_titles_and_votes = extract_movie_titles_and_vote_average(weekly_trending_movie_json_data)

# Sort the list of dictionaries by 'vote_average'. Use reverse=True for descending order.
movies_titles_and_votes.sort(key=lambda x: x['vote_average'], reverse=True)
print_movie_voter_avg_table(movies_titles_and_votes)