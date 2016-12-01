def main():
    print "Allowed Commands:\n\
    SIZE to set size of cache,\n\
    SET to set store a key value in the cache,\n\
    GET to get the value for a key in the cache,\n\
    EXIT to exit the program"
    cmd = raw_input().strip()
    if cmd == 'EXIT':
        return

    try:
        cmd, value = cmd.split(" ")
        assert cmd.strip() == 'SIZE'
        cache_size = int(value.strip())
    except:
        raise IOError("First command should be size of cache:e.g. SIZE 4")
    else:
        assert cache_size > 0, 'Invalid size for cache'
        cache = Cache(cache_size)

    while True:
        cmd = raw_input().strip()
        if cmd == 'EXIT':
            break
            
        try:
            cmd, keyvalue  = cmd.split(" ",1)
            assert cmd in ['GET','SET']
        except:
            print "ERROR"
        else:
            if cmd == 'GET':
                cache.loadKey(key=keyvalue)
            elif cmd == 'SET':
                try:
                    key,value = keyvalue.split(" ",1)
                    key,value = key.strip(),value.strip() # Remove whitespaces from left and right
                except ValueError:
                    print "ERROR"
                else:
                    cache.storeKey(key,value)
    return cache

if __name__ == '__main__':
    main()
