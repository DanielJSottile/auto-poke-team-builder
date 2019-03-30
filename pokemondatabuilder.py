import sys
import re


def main():
    print("Import a Pokemon Showdown Set. Press `Enter` & `^D` when done: \n ")
    pokemon_set = sys.stdin.read()  # this let's us ignore lines yay

    pokemon_setlist = pokemon_set.splitlines()  # this splits by line into list

    # sets level to 100 if not included
    if not any("Level:" in lines for lines in pokemon_setlist[1:]):
        pokemon_setlist.insert(2, "Level: 100")
    
    # this deletes that if it contains it, because we dont need it.
    if pokemon_setlist[3] == 'Shiny: Yes  ':
        del pokemon_setlist[3]

    # sets happiness to 255 if not included
    if not any("Happiness:" in lines for lines in pokemon_setlist[1:]):
        pokemon_setlist.insert(3, "Happiness: 255")

    # sets EV's to none if not included
    if not any("EVs:" in lines for lines in pokemon_setlist[1:]):
        pokemon_setlist.insert(4, "EVs: None")

    # sets IV's to none if not included
    if not any("IVs: " in lines for lines in pokemon_setlist[1:]):
        pokemon_setlist.insert(6, "IVs: None")

    # sets move 2 to none if not included
    try:
        gotmove2 = pokemon_setlist[8]
    except IndexError:
        gotmove2 = '- None'
        pokemon_setlist.append(gotmove2)

    # sets move 3 to none if not included
    try:
        gotmove3 = pokemon_setlist[9]
    except IndexError:
        gotmove3 = '- None'
        pokemon_setlist.append(gotmove3)

    # sets move 4 to none if not included
    try:
        gotmove4 = pokemon_setlist[10]
    except IndexError:
        gotmove4 = '- None'
        pokemon_setlist.append(gotmove4)

    # need to search in [0] the species inside the () from end of list, return
    s = pokemon_setlist[0]
    NICKNAME_AND_ITEM_RE = re.compile(r'^.*\((.*)\) @ (.*) $')
    NICKNAME_NO_ITEM_RE = re.compile(r'^.*\((.*)\)')
    NO_NICKNAME_AND_ITEM_RE = re.compile(r'^(.*) @ (.*)')

    item = 'none'

    if NICKNAME_AND_ITEM_RE.match(s):
        species, item = NICKNAME_AND_ITEM_RE.match(s).groups()
    elif NICKNAME_NO_ITEM_RE.match(s):
        species, = NICKNAME_NO_ITEM_RE.match(s).groups()
    elif NO_NICKNAME_AND_ITEM_RE.match(s):
        species, item = NO_NICKNAME_AND_ITEM_RE.match(s).groups()
    else:
        species = s

    # search for the ability after Ability:
    a = pokemon_setlist[1]
    ABILITY_NAME_RE = re.compile(r'^.*: (.*)')

    if ABILITY_NAME_RE.match(a):
        ability, = ABILITY_NAME_RE.match(a).groups()
    else:
        ability = 'None'

    # search for the level after Level:
    l = pokemon_setlist[2]
    LEVEL_NUM_RE = re.compile(r'Level: (.*)')

    if LEVEL_NUM_RE.match(l):
        level, = LEVEL_NUM_RE.match(l).groups()
    else:
        level = '100'    

    # search for the happiness after Happiness:
    h = pokemon_setlist[3]
    HAPPINESS_NUM_RE = re.compile(r'Happiness: (.*)')

    if HAPPINESS_NUM_RE.match(h):
        happiness, = HAPPINESS_NUM_RE.match(h).groups()
    else:
        happiness = '255'

    # search for the EV string after EVs:
    e = pokemon_setlist[4]
    EV_STRING_RE = re.compile(r'EVs: (.*)')

    if EV_STRING_RE.match(e):
        ev, = EV_STRING_RE.match(e).groups()
    else:
        ev = 'None'

    # search for the nature name before the word Nature
    n = pokemon_setlist[5]
    NATURE_NAME_RE = re.compile(r'^(.*) Nature')

    if NATURE_NAME_RE.match(n):
        nature, = NATURE_NAME_RE.match(n).groups()
    else:
        nature = 'none'

    # search for the IV string after IVs:
    i = pokemon_setlist[6]
    IV_STRING_RE = re.compile(r'^IVs: (.*)')

    if IV_STRING_RE.match(i):
        iv, = IV_STRING_RE.match(i).groups()
    else:
        iv = 'None'

    # separate the moves, find them after - , strip them, then put them
    # into a new list by itself
    m1 = pokemon_setlist[7]
    m2 = pokemon_setlist[8]
    m3 = pokemon_setlist[9]
    m4 = pokemon_setlist[10]
    
    print(m1)

    MOVE_NAME_RE = re.compile(r'^- (.*)')
    move1, = MOVE_NAME_RE.match(m1).groups()
    move2, = MOVE_NAME_RE.match(m2).groups()
    move3, = MOVE_NAME_RE.match(m3).groups()
    move4, = MOVE_NAME_RE.match(m4).groups()

    # strip everything of trailing and leading whitespaces first
    species = species.strip()
    item = item.strip()
    ability = ability.strip()
    level = level.strip()
    happiness = happiness.strip()
    ev = ev.strip()
    nature = nature.strip()
    iv = iv.strip()
    move1 = move1.strip()
    move2 = move2.strip()
    move3 = move3.strip()
    move4 = move4.strip()

    move_list = []
    move_list.append(move1)
    move_list.append(move2)
    move_list.append(move3)
    move_list.append(move4)

    # print everything.  Later, return to a database
    print('\n')
    print(species)
    print(item)
    print(ability)
    print(level)
    print(happiness)
    print(ev)
    print(nature)
    print(iv)
    print(move_list)
    print('\n')
    print(pokemon_setlist)

    # current errors:
    # if you select the pokemon as always being Male or Female,
    # it will use (M) or (F) in the list and break this program
    # need to check if the thing in parentheses is more than 1 character.
    # possible fixes:
    # lines 23-42 could be something like this:
    # moves = []
    # for line in lines[1:]:
        # if line.startswith('- '):
            # moves.append(line[2:])
    # for _ in range(4 - len(moves)):
    # moves.append('None')

    #in the future this will return those values and create a database

if __name__ == '__main__':
    exit(main())
