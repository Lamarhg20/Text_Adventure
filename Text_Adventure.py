#game attempt

import random
import sys
import time

a = 1
b = 0.2
c = 0.05

#intro
def intro():
    s = 'You open your eyes. it\'s so dark'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(2)
    print('\nyou can\'t tell if your eyes are actually open. you feel around in the dark')
    time.sleep(b)
    print('stepping carefully, feeling for the edge of the room.')
    time.sleep(b)
    print('you touch a wall. It feels like cold weathered wood.')
    time.sleep(b)
    print('you move you hands around the wall as you sidestep to the right.')
    time.sleep(b)
    print('you find a switch and flip it')
    time.sleep(b)
    print('you can hear the crackling of florescent bulbs flickering as')
    time.sleep(b)
    print('they light the room.')
    print()
    time.sleep(b)
    print('you glance around as your eye adjust to the light')
    time.sleep(b)
    print('you don\'t remember how you got here or even where here is')
    time.sleep(b)
    print('you\'re in a large garage. The windows appear to be boarded up')
    time.sleep(b)
    print('and covered in plastic. sheets of plastic drape from ')
    time.sleep(b)
    print('the ceiling to the floor. There is a door next to the light switch')
    time.sleep(b)
    print('the door appears to have a window but the other side is covered')
    time.sleep(b)
    print('with paper. In the middle of the room there is a large metal table')
    time.sleep(b)
    print('the table appears to be the cleanest thing in the room. Hanging')
    time.sleep(b)
    print('above it are large power tools. they all look well used')
    print()
    time.sleep(a)
    e = 'What do you want to do next?:'
    for character in e:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print('a. continue examining the room')
    print('b. check the door')
    print('c. check the windows')
    firstBranch =input('choose wisely: (a/b/c)')
    if firstBranch.lower() == 'a':
            print()
            pathA1()
    elif firstBranch.lower() == 'b':
            print()
            pathB1()
    elif firstBranch.lower() == 'c':
            print()
            pathC1()

# game start
def start():
    startGame =''
    while startGame.lower() != 'n' and 'y':
        startGame = input('Do you want to play a game? (Y/N): ')
        if startGame.lower() == 'n':
            validateAnswer = input('Are you sure? (Y/N):')
        if validateAnswer.lower() == 'n':
                intro()
        elif startGame.lower() == 'y':
            intro()
        else:
            print('Well that\'s too bad')
# paths
def pathA1():
    print('ha ha you died va1')
def pathA2():
    print('ha ha you died va2')
def pathB1():
    print('ha ha you died vb1')
def pathB2():
    print('ha ha you died vb2')
def pathC1():
    print('ha ha you died vc1')
def pathC2():
    print('ha ha you died vc2')

def gameOver(player):
    if player.health < 1:
        print('you\'ve been knocked unconscious.')
        print('you wake up strapped to the large metal table')
        print('the butcher is standing over with his cleaver raised')
        print('you let out a muffled cry as the cleaver comes down.')
        print('******************** YOU DIED **********************')
        print('game over \nthanks for playing')
        exit()


# Protagonist
class player (object):
    health = 10
    strength = 5
    defense = 2

# enemy

class strangeMan (object):
    name = 'the tall skinny man'
    health = 20
    strength = 3
    defense = 10
    loot = random.randint(0,2)

class largeman (object):
    name = 'the heavy-set man'
    health = 30
    strength = 4
    defense = 10
    loot = random.randint(0,2)
# give him the key
class Boss (object):
    name = 'the butcher'
    health = 60
    strength = 5
    defense = 10
    loot = random.randint(0,2)

def enemyselect(largeman, strangeMan):
    enemyList = [largeman, strangeMan]
    chance = random.randint(0,1)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ['bandage', 'knife', 'screwdriver']
    lootChance = random.randint(0, 2)
    lootDrop = loot[lootChance]
    return lootDrop

def lootEffect(lootDrop, player):
    if lootDrop == 'bandage':
        player.health = player.health + 20
        print('you bandaged your wounds')
        return player
    elif lootDrop == 'knife':
        player.strength = player.strength + 5
        print('know you\'ve got a weapon')
        return player
    elif lootDrop == 'screwdriver':
        player.strength = player.strength + 2
        print('maybe you can use it as a weapon')
        return player