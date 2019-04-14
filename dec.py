from timer import timer

@timer
def add(x, y=10):
    '''
    MAIN function with your main business logic
    If you want to keep it clean, readable and focus on the business behavior only, 
    but you want some additional (extended) behavior be executed when the function runs
    for example: measure elapsed latency of the function execution and print it
    '''
    return x + y


print 'add(2)', add(2)