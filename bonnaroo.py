import spotipy
import sys

def main():
	file = open(sys.argv[1], "r")
	artists = [artist for artist in file]

if __name__ == '__main__':
	main()