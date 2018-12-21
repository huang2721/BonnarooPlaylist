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
	token = util.oauth2.SpotifyClientCredentials(client_id='52e761dfa7e542b69f9250cb7d243bca', client_secret='30de97fa9ae24103ac067dcf1683dce2')
	cache_token = token.get_access_token()
	scope = "playlist-modify-public"
	#token = util.prompt_for_user_token(username,scope,client_id='52e761dfa7e542b69f9250cb7d243bca',client_secret='30de97fa9ae24103ac067dcf1683dce2',redirect_uri='http://startbackpacking.org')
	if token:
		# Create spotify object
		sp = spotipy.Spotify(cache_token)
		# Get IDs of all artists in the text file
		artistIDs = get_artist_ids(sp, artists)
		# Grab list of top 5 songs for each artist (No remixes for certain genres)
		remixesAllowed = []
		songIDs = get_song_IDs(sp, artistIDs, remixesAllowed)

		"""
		# Check to see if Bonnaroo playlist already exists
		userPlaylists = get_user_playlist_names(sp)
		if playlist_name not in userPlaylists:
			# Create playlist
			playlist = sp.user_playlist_create(username,playlist_name)
			# Adds top 5 songs for each artist to playlist
			add_track(sp, username, playlist, songIDs)
		else:
			print("Bonnaroo Playlist 2019 has already been created :)")
			"""

		# Create playlist
		playlist = sp.user_playlist_create(username, playlist_name)
		# Adds top 5 songs for each artist to playlist
		add_track(sp, username, playlist, songIDs)

	else:
		print("Can't get token for", username)

def get_artist_ids(sp, artists):
	artistIDs = {}
	for artist in artists:
		artistID = sp.search(artist,1,0,"artist")['artists']['items'][0]['id']
		artistGenre = sp.search(artist,1,0,"artist")['artists']['items'][0]['genres']
		artistIDs[artistID] = artistGenre
	return artistIDs

"""
def get_user_playlist_names(sp):
	userPlaylists = sp.current_user_playlists()
	return [userPlaylists['items'][i]['name'] for i in range(len(userPlaylists['items']))]
	"""

def get_song_IDs(sp, artistIDs, remixesAllowed):
	songIDs = []
	for artistID in artistIDs:
		added = 0
		print(artistIDs[artistID])
		for j in range(10):
			songIDs.append(sp.artist_top_tracks(artistID)['tracks'][j]['id'])
	return songIDs

def add_track(sp, username, playlist, songIDs):
	sp.user_playlist_add_tracks(username, playlist['id'], songIDs)

if __name__ == '__main__':
	main()
