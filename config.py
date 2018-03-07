"""To maintain modifiability."""


"""Used in mail.py. If using the OAuth2 client, these can be the same."""

FROM_EMAIL = "b.lim@berkeley.edu"        #The address from which the email originates.
TO_EMAIL = "b.lim@berkeley.edu"          #The address to which the email is sent.


"""Used in crawler.py."""

SITE_URL = "https://www.urbanoutfitters.com/"           #The website's main URL.
SITE_NAME = "Urban Outfitters"                          #The domain name.
SEARCHBAR = "q"                                         #HTML name of the searchbar.
NOT_FOUND = "Your search returned zero results"         #Message upon a search with no results.
NO_EXIST = "Oops, sorry. That page can't be found."     #Message upon accessing a page that doesn't exist.
XPATH = "//li[contains(@class, 'is-disabled')]"         #XPath corresponding with unreachable size.
TIME_TO_SLEEP = 3600                                    #Time to check website again (in seconds).