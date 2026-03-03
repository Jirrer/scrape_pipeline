import time, os

class Thread:
    def __init__(self, url):
        self.url = url

seen_urls = set()
stack: list[Thread] = []

urls = iter([
    'https://www.google.com',
    'https://www.youtube.com',
    'https://www.wikipedia.org',
    'https://www.amazon.com',
    'https://www.reddit.com',
    'https://www.twitter.com',
    'https://www.instagram.com',
    'https://www.linkedin.com',
    'https://www.netflix.com',
    'https://www.microsoft.com'
])


def main():
    while (True):
        url = getNewUrl()

        while url  in seen_urls:
            url = getNewUrl

        if not url: break

        stack.append(Thread(url))

        seen_urls.add(url)

        showStack()

        time.sleep(1)

    while (len(stack)):
        showStack()

        time.sleep(1)

def getNewUrl() -> str | bool:
    try:
        return next(urls)

    except StopIteration as e:
        return False

def showStack():
    os.system('cls')

    print("*** Running Procress *** ")
    if len(stack): print(stack[0].url)
    else: print("NULL")

    print("\n*** Waiting Processes ***")
    if len(stack) > 1: 
        for thread in stack[1:]: print(thread.url)

    else: print("NULL")

    print("\n*** Finished Processes")
    activeUrls = set([T.url for T in stack])

    finishedUrls = []

    for url in seen_urls:
        if url not in activeUrls: 
            finishedUrls.append(url)

    if len(finishedUrls): print([U for U in finishedUrls])
    else: print("NULL")

if __name__ == "__main__":
    main()