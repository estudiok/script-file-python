
def templatePostData():
    template = """
     { 
        "image": "$image",
        "autor": "$autor", 
        "link1": "$link1",
        "link2": "link2",
        "link3": "link3"
    }
    """
    return template
    

def createFile(nameFile):
    fp = open(nameFile, 'x')
    fp.close()