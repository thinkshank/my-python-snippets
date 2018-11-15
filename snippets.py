def prettytime(ms):
    import datetime
    temp = datetime.datetime.fromtimestamp(ms/1000).strftime('%H:%M:%S')
    return temp

def datetimetomillis_python3(dattimeobj):
    # todo convert dattimeobject to milliseconds
