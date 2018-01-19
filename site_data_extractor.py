from bs4 import BeautifulSoup
import requests
import sys

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise ValueError("Need to pass in the site address as command line argument")
    url = sys.argv[1]
    last_occurence_of_slash = url.rfind("/")
    base_url = url[:last_occurence_of_slash]
    print(base_url)