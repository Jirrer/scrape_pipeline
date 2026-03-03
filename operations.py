import time, random

def linearSearch(thread) -> bool | None:
    startTime = time.perf_counter()

    parsedContent = thread.content.split(" ")

    searchElement = random.choice(list(set(parsedContent)))

    index = thread.workingLine
    while (time.perf_counter() < startTime + 5):
        if parsedContent[index] == searchElement: return True

        if index == len(parsedContent) - 1: return False
        
        index += 1
        
    thread.workingLine = index
    
    return None

def filter(thead) -> bool:
    time.sleep(3)

    return True