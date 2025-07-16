import requests
from bs4 import BeautifulSoup
import re
import params

stringParam = params.stringParam
urls = params.urls
lines = []

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.text

    #Finds text based on string
    print(title, '\n')
    lines.append(title)
    lines.append("\n")
    found = soup.find_all(string=re.compile(stringParam))
    lines.append(str(found))
    lines.append("\n\n")
    print(found, '\n')

if __name__ == '__main__':
    print('\n')
    counter = 0
    while counter < len(urls):
        scrape(urls[counter])
        counter += 1
    
    writeChoice = input("Would you like to write to file? y/n: ")
    if writeChoice.lower() == "y":
        with open("output.txt", "w") as file:
            file.writelines(lines)
            print("\nWritten to file successfully\n")
    else:
        exit(1)