import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch words from the url
      Args:
          the url

    Return:
        the list of words

    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print the item in the list
          Args:
              the item list

        """
    for item in items:
        print(item)


def main(url):
    """PFetch word from th eurl and Print the item in the list
              Args:
                  the url

            """
    words = fetch_words(url)
    print_items(words)


# Execute as script
if __name__ == '__main__':
    #main(sys.argv[1])  # thr arg is the url
    main('http://sixty-north.com/c/t.txt')

# http://sixty-north.com/c/t.txt
