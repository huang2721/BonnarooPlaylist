import spotipy
import sys
import spotipy.util as util

def main():
	file = open("artists.txt", "r")
	# Get artist names in list from file
	artists = [artist for artist in file]
	playlist_name = "Bonnaroo's 2019 Lineup Top 5"
	# Set up token verification info
	username = sys.argv[1]
	scope = "playlist-modify-public"
	token = util.prompt_for_user_token(username,scope,client_id='52e761dfa7e542b69f9250cb7d243bca',client_secret='30de97fa9ae24103ac067dcf1683dce2',redirect_uri='http://startbackpacking.org')
	if token:
		# Create spotify object
		sp = spotipy.Spotify(auth=token)
		# Get IDs of all artists in the text file
		artistIDs = get_artist_ids(sp, artists)
		# Grab list of top 5 songs for each artist (No remixes for certain genres)
		remixesAllowed = ['house','dub','trance','breakbeat','bass','techno','edm']
		songIDs = get_song_IDs(sp, artistIDs, remixesAllowed)
		# Create playlist
		playlist = sp.user_playlist_create(username, playlist_name)
		# Adds top 5 songs for each artist to playlist
		add_tracks(sp, username, playlist, songIDs)
		print("Playlist was created successfully :) <3")
	else:
		print("Can't get token for ", username)

def get_artist_ids(sp, artists):
	artistIDs = {}
	for artist in artists:
		artistID = sp.search(artist,1,0,"artist")['artists']['items'][0]['id']
		artistGenre = sp.search(artist,1,0,"artist")['artists']['items'][0]['genres']
		artistIDs[artistID] = artistGenre
		print(artistIDs[artistID])
	return artistIDs

def get_song_IDs(sp, artistIDs, remixesAllowed):
	songIDs = []
	for artistID in artistIDs:
		if allow_remixes(artistIDs[artistID], remixesAllowed):
			currentSongs = get_all_songs(sp, artistID)
		else:
			currentSongs = get_songs_no_remixes(sp, artistID)
		for song in currentSongs:
			songIDs.append(song)
	return songIDs

def get_all_songs(sp, artistID):
	songs = []
	for i in range(5):
		songs.append(sp.artist_top_tracks(artistID)['tracks'][i]['id'])
	return songs

def get_songs_no_remixes(sp, artistID):
	allSongs = {}
	for i in range(10):
		allSongs[sp.artist_top_tracks(artistID)['tracks'][i]['id']] = [sp.artist_top_tracks(artistID)['tracks'][i]['name']]
	noRemixes = []
	added = 0
	for song in	allSongs:
		if added == 5:
			break 
		if 'remix' not in allSongs[song][0].lower() and 'edit' not in allSongs[song][0].lower():
			noRemixes.append(song)
			added += 1
	return noRemixes


def add_tracks(sp, username, playlist, songIDs):
	sp.user_playlist_add_tracks(username, playlist['id'], songIDs)

def allow_remixes(genres, remixesAllowed):
	for genre in genres:
		for remixGenre in remixesAllowed:
			if remixGenre in genre:
				return True
	return False

if __name__ == '__main__':
	main()