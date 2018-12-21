import spotipy
import sys
import spotipy.util as util
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


def main():
	#server stuff
	HandlerClass = SimpleHTTPRequestHandler
	ServerClass  = BaseHTTPServer.HTTPServer
	Protocol     = "HTTP/1.0"
	port = 8888
	server_address = ('127.0.0.1', port)
	HandlerClass.protocol_version = Protocol
	httpd = ServerClass(server_address, HandlerClass)
	sa = httpd.socket.getsockname()
	httpd.serve_forever()

	file = open(sys.argv[1], "r")
	artists = [artist for artist in file]
	playlist_name = "Bonnaroo Playlist 2019"
	playlist_description = "Barns, beats, Bonnaroo. Get ready for 2019 with these tunes as hot as the Tennessee sun!"
	username = sys.argv[2]
	scope = "playlist-modify-public"
	token = util.prompt_for_user_token(username,scope,client_id='52e761dfa7e542b69f9250cb7d243bca',client_secret='30de97fa9ae24103ac067dcf1683dce2',redirect_uri='http://localhost:8888/callback')
	if token:
		sp = spotipy.Spotify(auth=token)
		playlists = sp.user_playlist_create(username, playlist_name,playlist_description)
		print(playlists)




if __name__ == '__main__':
	main()
