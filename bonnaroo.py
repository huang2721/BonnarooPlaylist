import spotipy
import sys
import spotipy.util as util

def main():
	file = open("artists.txt", "r")
	# Get artist names in list from file
	artists = [artist for artist in file]
	playlist_name = "Bonnaroo Playlist 2019"
	# Set up token verification info
	username = sys.argv[1]
	scope = "playlist-modify-public"
	token = util.prompt_for_user_token(username,scope,client_id='52e761dfa7e542b69f9250cb7d243bca',client_secret='30de97fa9ae24103ac067dcf1683dce2',redirect_uri='http://startbackpacking.org')
	if token:
		# Create spotify object
		sp = spotipy.Spotify(auth=token)
		# Create playlist
		playlist = sp.user_playlist_create(username,playlist_name)
		# Get IDs of all artists in the text file
		artistIDs = get_artist_ids(sp, artists)
		# Grab top 5 songs and add them to playlist
		songIDs = [sp.artist_top_tracks(artistIDs[i])['tracks'][j]['id'] for i in range(len(artistIDs)) for j in range(5)]
		sp.user_playlist_add_tracks(username, playlist['id'], songIDs)
	else:
		print("Can't get token for", username)

def get_artist_ids(sp, artists):
	artistIDs = [sp.search(artist,1,0,"artist",)['artists']['items'][0]['id'] for artist in artists]
	return artistIDs

if __name__ == '__main__':
	main()
