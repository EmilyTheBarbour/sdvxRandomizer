import xlrd
import random
import sys

class Level:

    def __init__(self, level, ratingArray):
        self.level = level
        self.ratings = ratingArray
        self.songs = []

    def getSongsAtRating(self, rating):
        for i, rate in enumerate(self.ratings):
            if rate == rating:
                return self.songs[i]
        return []

class LevelSet:

    def __init__(self, levels):
        self.levels = levels

    def getLevel(self, levelTarget):
        for lev in self.levels:
            if lev.level == levelTarget:
                return lev
        return Level(-1, [])

    def getSongsAtRatingFromLevel(self, levelTarget, rating):
        lev = self.getLevel(levelTarget)
        if lev.level == -1:
            return []
        return lev.getSongsAtRating(rating)

    def getRandomSongFromLevel(self, levelTarget):
        lev = self.getLevel(levelTarget)
        if lev.level == -1:
            return 'ERROR'
        songlist = []
        for songs in lev.songs:
            songlist += songs
        
        return random.choice(songlist)

    def getRandomSongAtRatingFromLevel(self, levelTarget, rating):
        songs = self.getSongsAtRatingFromLevel(levelTarget, rating)
        if songs == []:
            return 'ERROR'
        return random.choice(songs)
        
levels = []
ratingsSize = [7, 8, 8, 8, 5]

wb = xlrd.open_workbook('sdvx.xls')
add = 0

for shnum in range(1, 6):

    if shnum == 4:
        add = 1
        continue
    sh = wb.sheet_by_index(shnum)
    
    ratingsTemp = sh.row_values(1)
    ratings = []
    for i in range(ratingsSize[shnum-1]):
        ratings.append(ratingsTemp[i])

    levels.append(Level(19 - shnum + add, ratings))

    for col in range(ratingsSize[shnum - 1]):
        songsTemp = sh.col_values(col)
        songsTemp.pop(0)
        rating = songsTemp[0]
        
        songs = []
        for song in songsTemp:
            if song == '' or song == rating:
                continue
            songs.append(song)

        levels[shnum - 1 - add].songs.append(songs)

def getSongsWithRating(levelSet, levelTarget, rating, num):
    for i in range(num):
        print(levelSet.getRandomSongAtRatingFromLevel(levelTarget, rating))

def getSongs(levelSet, levelTarget, num):
    for i in range(num):
        print(levelSet.getRandomSongFromLevel(levelTarget))

def main():
        sdvx = LevelSet(levels)
        
        args = len(sys.argv[1:])
        
        if args >= 3:
            if sys.argv[1] == 'RandomSongFromRatingAtLevel':
                if args >= 4:
                    for i in range(int(sys.argv[4])):
                        print(sdvx.getRandomSongAtRatingFromLevel(int(sys.argv[2]), sys.argv[3]))     
                else:
                    print(sdvx.getRandomSongAtRatingFromLevel(int(sys.argv[2]), sys.argv[3]))                 

if __name__ == "__main__":
    main()
