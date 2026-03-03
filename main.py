import time, os, enum, csv
import operations

# To-Do: maybve keep order of procresses (a stack) for dispalying finished processes

class Operation(enum.Enum):
    sort = "sort"
    filter = 'filter'

class Thread:
    def __init__(self, url, *operations: Operation):
        self.url = url
        self.operations = [o for o in operations]
        self.content = None
        self.workingLine = 0

        if len(self.operations): self.completion = 0.00
        else: self.completion = 100.00

seen_urls = set()
failed_urls = set()
stack: list[Thread] = []


def setUrls():
    with open('urls.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        return iter([(row[0], tuple(row[1:])) for row in reader])
    
def main():
    while (True):
        url = getNewUrl()

        while url in seen_urls:
            url = getNewUrl

        if not url: break

        stack.append(Thread(url[0], *url[1]))

        seen_urls.add(url[0])

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

# To-Do: clean method
def showStack():
    os.system('cls')

    print("*** Running Procress *** ")
    if len(stack): print(f'{stack[0].url} - {stack[0].completion}%')
    else: print("NULL")

    print("\n*** Waiting Processes ***")
    if len(stack) > 1: 
        for thread in stack[1:]: print(thread.url)

    else: print("NULL")

    print("\n*** Finished Processes ***")
    activeUrls = set([T.url for T in stack])

    finishedUrls = []

    for url in seen_urls:
        if url not in activeUrls: 
            finishedUrls.append(url)

    if len(finishedUrls): 
        for url in finishedUrls :
            if url not in failed_urls: print(url)

    else: print("NULL")

    print("\n*** Failed Processes ***") 
    if len(finishedUrls): 
        for url in finishedUrls:
            if url in failed_urls: print(url)

    else:
        print("NULL")


def workCurrentThread():
    startTime = time.perf_counter()

    while (time.perf_counter() < (startTime + 5)):
        if len(stack[0].operations): doOperation()
        else: break

    if stack[0].completion == 100.00:
        stack.pop(0) # big O(n)

def doOperation():
    match (stack[0].operations.pop()):
        case Operation.sort.value: outcome = operations.sort()
        case Operation.filter.value: outcome = operations.filter()
        case _: outcome = False

    if not (outcome):
        failed_urls.add(stack[0].url)

    # To-Do: update completion here

    if not len(stack[0].operations): stack[0].completion = 100.00 

if __name__ == "__main__":
    urls = setUrls()
    main()