import time

# Never assume an operation can be done in one go under 5s

def linearSearch(thread, searchElement: str) -> bool | None:
    print('linear serch')
    startTime = time.perf_counter()

    parsedContent = thread.content.split(" ")

    index = thread.workingLine
    while (time.perf_counter() < startTime + 5):
        if parsedContent[index] == searchElement: return True

        if index == len(parsedContent) - 1: return False

        index += 1
        
    thread.workingLine = index
    
    return None

def binarySearch(thread, searchElement) -> bool | None:
    startTime = time.perf_counter()

    parsedContnet = thread.content.split(" ")

    sortedList = parsedContnet.sort() # move to loop

    l = thread.workingLine
    h = len(sortedList) - 1
    while (time.perf_counter() < startTime + 5 or l <= h):
        mid = (l + h) // 2

        if sortedList[mid] == searchElement: return True
        elif sortedList[mid] < searchElement: h = mid - 1
        else: l = mid + 1

        index += 1

    if l > h:
        return False

    thread.workingLine = index

    thread.content = ''.join(sortedList[l:h])

    return None

def filter(thead) -> bool:
    time.sleep(3)

    return True