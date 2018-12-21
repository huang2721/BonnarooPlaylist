import spotipy
import sys

def main():
	file = open(sys.argv[1], "r")
	print(file.read())

if __name__ == '__main__':
	main()