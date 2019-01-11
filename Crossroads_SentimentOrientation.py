# -*- coding: utf-8 -*-
# Include the following: SO = log((n(excellent, US healthcare) / n(excellent)) / (n(poor, US healthcare) / n(excellent))
# , where n(x) is the number of pages containing x and n(x,y) is the number of pages containing x and y.
# https://www.linkedin.com/pulse/quick-easy-sentiment-analysis-using-google-search-result-pranab-ghosh/

# Resources:
# Reference of parameters: https://developers.google.com/custom-search/json-api/v1/reference/cse/list
# API explorer: https://developers.google.com/apis-explorer/#p/customsearch/v1/search.cse.list?q=pizza+great&cx=013987910149588354017%253Aui0xnrn9hiw&_h=1&

# Maybe also use Twitter: https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/




# This is a small app that helps make decisions (and allows me to teach myself Python)
# Beware of actually following this app's advice!

print("I heard you had a tough decision to make? Maybe I can help.")


####################
# Get Options      #
####################

# Get the number of options
num_options = int(input("Enter the number of options you have: "))

# Declare lists
options = []
SentimentOrientations = []

# Let's ask for the what the options are
# Remember to use range() to make an x that is iterable, and to use the append thing
for i in range(num_options):
    options.append(input("What is option number " + str(i + 1) + ": "))

# Define words that describe whether an option is good or bad
positive_attribute = "great"
negative_attribute = "bad"


####################
# Query Google     #
####################

# Importing the API client library and JSON
from googleapiclient.discovery import build

# We'll need to do some math later
import math

# import json
# import pprint


# We need to import this to put the API tokens in a local environmental variable to avoid it showing up on GitHub
import os

my_api_key = os.environ['GOOGLE_CSE_API_KEY']
my_cse_id = os.environ['GOOGLE_CSE_ID']


# Defining the search function
# Important here might be the return – the string in the brackets pre-selects JSON keys
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    response = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return response['searchInformation']


# Looping the searches for each option
for option in options:


	# Plain Positive
	# Perform the Google search
	current_search_term = positive_attribute
	response_google = google_search(current_search_term, my_api_key, my_cse_id)

	# Extract the number of results of the Google search
	num_results_google_plainpositive = int(response_google['totalResults'])
	print(num_results_google_plainpositive) # Just for testing


	# Option + Positive
	# Perform the Google search
	current_search_term = option + " " + positive_attribute
	response_google = google_search(current_search_term, my_api_key, my_cse_id)

	# Extract the number of results of the Google search
	num_results_google_positive = int(response_google['totalResults'])
	print(num_results_google_positive) # Just for testing


	# Option + Negative
	# Perform the Google search
	current_search_term = option + " " + negative_attribute
	response_google = google_search(current_search_term, my_api_key, my_cse_id)

	# Extract the number of results of the Google search
	num_results_google_negative = int(response_google['totalResults'])
	print(num_results_google_negative) # Just for testing


	# Calculate Sentiment Orientiation Score
	SentimentOrientation = math.log(num_results_google_positive / num_results_google_plainpositive / num_results_google_negative / num_results_google_plainpositive)

	# Append list with Orientations
	SentimentOrientations.append(SentimentOrientation)

	# Output the Score
	print("Sentiment Score for " + option + " is: " + str(SentimentOrientation))



####################
# Output		   #
####################

# 1) Find highest value for Sentiment orientation, then 2) determine its index, and then 3) call that same item in options list
winner = options[SentimentOrientations.index(max(SentimentOrientations))]

# Let's give some potentially really bad advice
print("We (irresponsibly) recommend going with " + winner + ", which the internet thinks is the best (or least worst).")