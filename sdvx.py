import random
import re 
import sys

class Level:

    def __init__(self, level):
        self.level = level
        self.songs = []

class LevelSet:

    def __init__(self, levels):
        self.levels = levels

    def getLevel(self, levelTarget):
        for lev in self.levels:
            if lev.level == levelTarget:
                return lev
        return Level(-1)

    def getRandomSongFromLevel(self, levelTarget):
        lev = self.getLevel(levelTarget)
        if lev.level == -1:
            return 'ERROR'
        return random.choice(lev.songs)


levels = []

currentLevel = 0
index = -1
songName = 0

with open('sdvx.txt', encoding= 'utf8') as openfileobject:
    for line in openfileobject:
        line = re.sub('[\n\t]','', line)
        if line == '':
            songName = 0
            continue
        if line.isdigit() and songName == 0:
            songName = 1
            if int(line) > currentLevel:
                levels.append(Level(int(line)))
                index += 1
                currentLevel = int(line)
        elif songName == 1:
            levels[index].songs.append(line)
            songName = 0


def main():
    sdvx = LevelSet(levels)

    args = len(sys.argv[1:])
        
    if args >= 2:
         for i in range(sys.argv[3]):
             print(sdvx.getRandomSongFromLevel(sys.argv[2]))

if __name__ == "__main__":
    main()
        