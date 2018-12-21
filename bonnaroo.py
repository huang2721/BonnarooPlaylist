import spotipy
import sys
#Michael's Comment
def main():
	util.prompt_for_user_token(username,scope,client_id='52e761dfa7e542b69f9250cb7d243bca',client_secret='30de97fa9ae24103ac067dcf1683dce2',redirect_uri='http://localhost:8888/callback')
	file = open(sys.argv[1], "r")
	artists = [artist for artist in file]

if __name__ == '__main__':
	main()