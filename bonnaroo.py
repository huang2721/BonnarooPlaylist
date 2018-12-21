import spotipy
import sys
import spotipy.util as util
#Michael's Comment
def main():
	file = open(sys.argv[1], "r")
	artists = [artist for artist in file]
	playlist_name = "Bonnaroo Playlist 2019"
	token = util.prompt_for_user_token(username)
	print (token)
	if token:
		sp = spotipy.Spotify(auth=token)
		print (token)




if __name__ == '__main__':
	main()
