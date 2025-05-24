# -*- coding: utf-8 -*-
""" Playlist Generator """

print("Hey there. This is a playlist generator, where your mood choice makes a personal playlist for you.")

#Input data
import pandas as pd
data = pd.read_csv('Pop.csv').to_dict()

#Organize the data
songs = {}
for index in data['genre']:
  songs[index] = {}
  for attribute in data:
    songs[index][attribute] = data[attribute][index]

#Initialize different moods of songs
moods = {}
moods['Chill'] = {'danceability':[0.4,0.9],'energy':[0.5,0.8],'loudness':[-20,2],'valence':[0.35,0.9]}
moods['Focus'] = {'danceability':[0,0.6],'energy':[0.1,0.5],'loudness':[-33,0],'valence':[0.1, 0.8]}
moods['Party'] = {'danceability':[0.3,1],'energy':[0.4,1],'loudness':[-33, 3],'valence':[0.6, 1]}
moods['Deep-cuts'] = {'danceability':[0,0.45],'energy':[0,0.55],'loudness':[-27,0],'valence':[0,0.4]}
moods['Sadcore'] = {'danceability':[0.2,0.55],'energy':[0.3,0.6],'loudness':[-10,-1],'valence':[0.2,0.5]}

#Function to assign moods
def assign_mood(song, details, mood_name):
  if not (song['danceability'] >= details['danceability'][0] and song['danceability'] <= details['danceability'][1]):
    return None
  elif not (song['energy'] >= details['energy'][0] and song['energy'] <= details['energy'][1]):
    return None
  elif not (song['loudness'] >= details['loudness'][0] and song['loudness'] <= details['loudness'][1]):
    return None
  elif not (song['valence'] >= details['valence'][0] and  song['valence'] <= details['valence'][1]):
    return None
  return mood_name

#Assigning moods to each song
for song in songs:
  valid = []
  for mood in moods:
    check = assign_mood(songs[song], moods[mood], mood)
    if check:
      valid.append(check)
  songs[song]['Mood'] = valid

#Remove extra songs
final_data = {}
for song in songs:
  if songs[song]['Mood']:
    final_data[song] = songs[song]

#Selecting moods for the playlist
print("Choose mood:")
print("1. Chill\n2. Focus\n3. Party\n4. Deep-cuts\n5. Sadcore")
choices = eval(f'{input("Enter numbers of your choices (separated by commas): ")} ,')

reqd_moods = []
for choice in choices:
  reqd_moods.append(list(moods.keys())[choice-1])

#Selecting songs of required moods
playlist = []
for song in final_data:
  for mood in reqd_moods:
    if mood in final_data[song]["Mood"]:
      playlist.append(final_data[song]['song_name'])

#Randomizing the songs and selecting a number of songs
length = int(input('\nHow many songs do you want in your playlist? '))
from numpy import random
random.shuffle(playlist)
playlist = playlist[:length]
print('\n\nHere is your playlist of', length,'songs from the selected moods!!')
for num in range(length):
  print(num + 1, '-', playlist[num])
print('\nHope you enjoyed using the program!\nEnjoy listening to your playlist! :)')
