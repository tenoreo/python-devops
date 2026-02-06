import wikipedia


def wiki(name="War Godddess", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name)
    return my_wiki