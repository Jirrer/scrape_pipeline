import time, os, random

class Thread:
    def __init__(self, url):
        self.url = url
        self.completion = 0.00
        self.content = None
        self.workingLine = 0

seen_urls = set()
stack: list[Thread] = []

def setUrls():
    with open('urls.txt', 'r', newline='') as file:
        return iter([row.replace('\r', '').replace('\n', '') for row in file])

def main():
    while (True):
        url = getNewUrl()

        while url  in seen_urls:
            url = getNewUrl

        if not url: break

        stack.append(Thread(url))

        seen_urls.add(url)

        showStack()
        workCurrentThread()

    while (len(stack)):
        showStack()
        workCurrentThread()

    showStack()

def getNewUrl() -> str | bool:
    try:
        return next(urls)

    except StopIteration as e:
        return False

def showStack():
    os.system('cls')

    print("*** Running Procress *** ")
    if len(stack): print(f'{stack[0].url} - {stack[0].completion}%')
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

    if len(finishedUrls): 
        for url in finishedUrls:
            print(url)

    else: print("NULL\n")

def workCurrentThread():
    startTime = time.perf_counter()

    while (time.perf_counter() < (startTime + 3)):
        doOperation()

    if stack[0].completion == 100.00:
        stack.pop(0) # big O(n)

def doOperation():
    time.sleep(random.randint(0, 3))

    completionTimes = [10, 25, 50, 75, 100]

    stack[0].completion += completionTimes[random.randint(0, 4)]

    if stack[0].completion > 100.00:
        stack[0].completion = 100.00

    return


if __name__ == "__main__":
    urls = setUrls()
    main()