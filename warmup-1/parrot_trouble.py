def parrot_trouble(talking, hour):
    if hour < 7:
        if talking == True:
            return True
        else:
            return False
    elif hour > 20:
        if talking == True:
            return True
        else:
            return False
    else:
        return False