import os


def getSerieName():
    x = os.getcwd().split("\\")
    return x[len(x)-2]


def getStaffelNumber():
    x = os.getcwd().split("\\")
    x = x[len(x)-1]
    n = ""
    for f in x:
        if f.isdigit():
            n = n + str(f)
    return n


def getExecName():
    x = ""
    for f in os.listdir():
        if ".py" in f:
            x = f
    return x


def getFileNames():
    onlyfiles = [f for f in os.listdir(".") if (
        os.path.isfile(os.path.join(".", f)) and getExecName() not in f)]
    return onlyfiles


def getNewFileName(season, episode):

    if(len(str(episode)) < 2):
        episode = "0" + str(episode)

    return getSerieName() + " - S{}E{}.mp4".format(season, episode)


def getEpisodeNumber(filename):
    i = 0
    episodeString = ""
    while(i < len(filename)):
        if "e" in filename[i] or "E" in filename[i]:
            if(i+1 < len(filename)):
                if(filename[i+1].isdigit()):
                    episodeString = filename[i+1]
                    if(filename[i+2].isdigit()): episodeString = episodeString + filename[i+2]
                    if(filename[i+3].isdigit()): episodeString = episodeString + filename[i+3]
        i=i+1
    return episodeString
# getEpisodeNumber(getFileNames()[0])

def renameFiles():
    season = getStaffelNumber()
    for files in getFileNames():
        os.rename(files,getNewFileName(season,getEpisodeNumber(files)))


renameFiles()
