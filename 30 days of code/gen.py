def take(count, iterable):
    counter =0
    for item in iterable:
        if counter==count:
            return
        counter+=1
        yield item

def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3,items):
        print(item)

if __name__== '__main__':
    run_take()