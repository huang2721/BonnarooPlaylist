import spotipy
import sys
#Michael's Comment
def main():
	file = open(sys.argv[1], "r")
	artists = [artist for artist in file]

if __name__ == '__main__':
	main()