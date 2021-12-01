import cross
import subprocess
import platform
game = cross.cross()


import sys

print("""
set first horizont
and second vertical
example 12:
  1  2  3
1| || || |
2|+|| || |
3| || || |
New game enter n
for quit enter q
""")
for line in sys.stdin:
    print(line)
    if 'q' == line.rstrip():
        break
    if len(line) == 3:
        game.setItem(line)
        continue
    if  "n"  == line[0]:
        game.newGame()
        continue
    else:
        print("erroe move")
        game.showField()
print("Exit")
