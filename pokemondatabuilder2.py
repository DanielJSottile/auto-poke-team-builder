import sys
import re

NICKNAME_GEN_AND_ITEM_RE = re.compile(r'^.*\((.*)\) \(([MF])\) @ (.*) $')
NICKNAME_AND_ITEM_RE = re.compile(r'^.*\((.*)\) @ (.*) $')
NICKNAME_GEN_NO_ITEM_RE = re.compile(r'^.*\((.*)\) \(([MF])\)$')
NICKNAME_NO_ITEM_RE = re.compile(r'^.*\((.*)\)$')
NO_NICKNAME_GEN_AND_ITEM_RE = re.compile(r'^(.*) \(([MF])\) @ (.*) $')
NO_NICKNAME_AND_ITEM_RE = re.compile(r'^(.*) @ (.*) $')


def main():
    print("Import a Pokemon Showdown Set. Press `Enter` & `^D` when done: \n ")
    pokemon_set = sys.stdin.read()  # this let's us ignore lines yay

    pokemon_setlist = pokemon_set.splitlines()  # this splits by line into list

    # need to search in [0] the species inside the () from end of list, return
    s = pokemon_setlist[0]

    item = 'none'
    gender = 'any'

    if NICKNAME_GEN_AND_ITEM_RE.match(s):
        species, gender, item = NICKNAME_GEN_AND_ITEM_RE.match(s).groups()
    elif NICKNAME_AND_ITEM_RE.match(s):
        species, item = NICKNAME_AND_ITEM_RE.match(s).groups()
    elif NICKNAME_GEN_NO_ITEM_RE.match(s):
        species, gender = NICKNAME_GEN_NO_ITEM_RE.match(s).groups()
    elif NO_NICKNAME_GEN_AND_ITEM_RE.match(s):
        species, gender, item = NO_NICKNAME_GEN_AND_ITEM_RE.match(s).groups()
    elif NO_NICKNAME_AND_ITEM_RE.match(s):
        species, item = NO_NICKNAME_AND_ITEM_RE.match(s).groups()
    else:
        species = s

    level = '100'
    happiness = '255'
    ev = 'None'
    iv = 'None'
    moves = []

    for line in pokemon_setlist[1:]:
        line = line.strip()
        if line.startswith('Ability:'):
            _, _, ability = line.partition(': ')
        elif line.startswith('Level:'):
            _, _, level = line.partition(': ')
        elif line.startswith('Shiny:'):
            _, _, shiny = line.partition(': ')
        elif line.startswith('Happiness:'):
            _, _, happiness = line.partition(': ')
        elif line.startswith('EVs:'):
            _, _, ev = line.partition(': ')
        elif line.endswith('Nature'):
            nature, _ = line.split()
        elif line.startswith('IVs:'):
            _, _, iv = line.partition(': ')
        elif line.startswith('- '):
            moves.append(line[2:])

    for _ in range(4 - len(moves)):
        moves.append('None')

    # print everything.  Later, return to a database
    print('\n')
    print(species)
    print(gender)
    print(item)
    print(ability)
    print(level)
    print(shiny)
    print(happiness)
    print(ev)
    print(nature)
    print(iv)
    print(moves)

    # in the future this will return those values and create a database


if __name__ == '__main__':
    exit(main())
