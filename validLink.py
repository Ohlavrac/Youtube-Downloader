def validLinkfunc(link2):
    linkValid = 'https://www.youtube.com/watch?v='

    for c in range(len(linkValid)):
        if linkValid[c] != link2[c]:
            return False

    return True