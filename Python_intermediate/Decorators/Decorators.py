import datetime

def allow_worktime_only(_from=7, _to=22):

    def inner_method(fun_reference):

        def wrapper():
            now = datetime.datetime.now()
            if _to > now.hour > _from:
                fun_reference()
            else:
                print('fuck yourself')
        return wrapper
    return inner_method

@allow_worktime_only(9, 18)
def execute_some_work():
    print('Some work result')


execute_some_work()