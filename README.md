# sdvxRandomizer

#sdvx.py

has 2 arguments: level number
level: the level pool to pick songs from
number: the number of songs to pick from that pool

for example:

python sdvx.py 15 2 

would return the following information:
15
НУМЛ
New Game feat.Mayumi Morinaga

#sdvxRating.py

similar to sdvx.py, except it is built off of the community rating system for levels 15-18

has 4 arguments: type level rating number
type: which type of randomization you will use, currently only 'RandomSongFromRatingAtLevel' is supported
level: the level pool to pick songs from
rating: the rating pool to pick songs from
number: the number of songs to pick from that pool

for example:

python sdvxRating.py RandomSongFromRatingAtLevel 15 A 2

would return the following information:
Noisy Minority[EXH]
【超超光速スピードスターかなで[ADV]】

this version of the randomizer is sort of depricated but has its uses
