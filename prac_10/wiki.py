import wikipedia
user_input = input("Page title or search phrase: ")
while user_input != "":
    try:
        page = wikipedia.page(user_input)
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    user_input = input("Page title or search phrase: ")
