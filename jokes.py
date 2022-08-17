import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("Welcome to Dad Jokes!")
header = colored(header, color ="magenta")
print(header)

url = "https://icanhazdadjoke.com/search"

#Ask for joke topic 
user_input = input("Let me tell you a joke! Give me a topic: ")

# Make get request to jokes website
response = requests.get(
    url, 
    headers={"Accept":"application/json"},
    params = {"term": user_input}
).json() #takes the json and turns it into python that we can use

# Number of jokes
num_jokes = response['total_jokes']
# Response Results
results = response['results']

# There's more than 1 joke on the topic
if num_jokes > 1:
    #Tell user how many jokes there are for that topic and pick one joke at random 
    print(f"I've got {num_jokes} jokes about {user_input}. Here's one:\n {choice(results)['joke']}")
# There's only 1 joke about that topic
elif num_jokes == 1:
    # print first joke item in that list
    print(f"I've got one joke about {user_input}. Here it is:\n {results[0]['joke']}")
# There's no jokes about that topic
else:
    print(f"Sorry, I don't have any jokes about {user_input}! Please try again.")

