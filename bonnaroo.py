import spotipy
import sys
import spotipy.util as util

def main():
	file = open(sys.argv[1], "r")
	artists = [artist for artist in file]
	playlist_name = "Bonnaroo Playlist 2019"
	playlist_description = "Barns, beats, Bonnaroo. Get ready for 2019 with these tunes as hot as the Tennessee sun!"
	username = sys.argv[2]
	scope = "playlist-modify-public"
	token = util.prompt_for_user_token(username,scope,client_id='52e761dfa7e542b69f9250cb7d243bca',client_secret='30de97fa9ae24103ac067dcf1683dce2',redirect_uri='http://startbackpacking.org')
	if token:
		sp = spotipy.Spotify(auth=token)
		sp.trace=False
		public = True
		playlist = sp.user_playlist_create(username,playlist_name,public)
		id=playlist['id']
		artistID=[]
		for artist in artists:
			temp = sp.search(artist,1,0,"artist","US")
			artistID.append(temp['artists']['items'][0]['id'])
		print(artistID)


if __name__ == '__main__':
	main()
