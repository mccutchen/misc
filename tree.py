def tree(data, indent=' '):
    """
    Prints complicated nested-dictionary structures
    in a reasonable fashion.
    
    TODO: Is this deprecated by pprint.pprint?
    """
    if isinstance(data, dict):
        keys = data.keys()
        keys.sort()
        for key in keys:
            print indent + str(key)
            tree(data[key], indent + '  ')
    elif isinstance(data, list) or isinstance(data, tuple):
        for item in data:
            print indent + str(item)
    else:
        print indent + str(data)