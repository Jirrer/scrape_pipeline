import os, enum, csv, urllib.request, random
import operations

# To-Do: maybve keep order of procresses (a stack) for dispalying finished processes
# To-Do: make operation cut off and keep track of progress
# To-Do: add a 'stack overflow' error if an operation is repeated too many times <-- important

class Operation(enum.Enum):
    linearSearch = 'linearSearch'
    binarySearch = 'binarySearch'
    filter = 'filter'

class Thread:
    def __init__(self, url, *operations: Operation):
        self.url = url
        self.operations = [o for o in operations]
        self.content = None
        self.workingLine = 0
        self.numOperations = len(operations)

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
            url = getNewUrl()

        if not url: break

        seen_urls.add(url[0])

        content = scrapeContnet(url[0])

        if not content: 
            failed_urls.add(url[0])
        
        else:
            stack.append(Thread(url[0], *url[1]))
            stack[len(stack) - 1].content = content

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
    
def scrapeContnet(url: str) -> str | bool:
    try:
        with urllib.request.urlopen(url) as response:
            html_content_bytes = response.read()

            return html_content_bytes.decode('utf-8')

    except urllib.error.HTTPError as e: return False
    except urllib.error.URLError as e: return False
    except urllib.error.AttributeError as e: return False

# To-Do: clean method
# To-Do: change the name of url
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
    if not len(stack): return

    if len(stack[0].operations): doOperation()

    if stack[0].completion == 100.00:
        stack.pop(0) # big O(n)

def doOperation():
    # To-Do: add peek functionality
    match (stack[0].operations.pop()):
        case Operation.linearSearch.value: 
            outcome = operations.linearSearch(stack[0], random.choice(list(set(stack[0].content.split(' ')))))

        case Operation.binarySearch.value: 
            outcome = operations.binarySearch(stack[0], random.choice(list(set(stack[0].content.split(' ')))))

        case Operation.filter.value: 
            outcome = operations.filter(stack[0])

        case _: 
            outcome = False

    if outcome == False:
        failed_urls.add(stack[0].url)

    elif outcome == True:
        stack[0].completion += 100 * (1 / stack[0].numOperations)

        if not len(stack[0].operations): stack[0].completion = 100.00 

if __name__ == "__main__":
    urls = setUrls()
    main()