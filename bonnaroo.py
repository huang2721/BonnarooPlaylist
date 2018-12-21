import spotipy
import sys
import spotipy.util as util
#Michael's Comment
def main():
	file = open(sys.argv[1], "r")
	artists = [artist for artist in file]
	playlist_name = "Bonnaroo Playlist 2019"
	username = sys.argv[2]
	token = util.prompt_for_user_token(username)
	print (token)
	if token:
		sp = spotipy.Spotify(auth=token)
		print (token)
	playlist_description = "Barns, beats, Bonnaroo. Get ready for 2019 with these tunes as hot as the Tennessee sun!"
	if token:
		sp = spotipy.Spotify(auth=token)
		sp.user_playlist_create(username, playlist_name,playlist_description)

if __name__ == '__main__':
	main()
