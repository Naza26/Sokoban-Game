# Sokoban

Sokoban is a puzzle video game in which the player pushes crates or boxes around in a warehouse, trying to get them to storage locations. This game was developed on Python & Gamelib Library.

## Installation

Make sure to have installed Gamelib library: [Gamelib](https://github.com/dessaya/python-gamelib).


Just download `gamelib.py` and place it along your project.


## Usage


Use the keys to move the player around.
```
"w" = Up.
"a" = Left.
"d" = Right.
"s" = Down.
"r" = Reset.
"u" = Undo.
"c" = Clue.

```

## Levels

This game includes 155 levels to play.

This is the representation of the game and its stuff:


Element | Character
------------ | -------------
Wall | #
Player | @
Player on goal square | +
Box | $
Box on goal square | *
Goal Square | .
Floor | (Space)

A level looks like this:

```
` ####
` #  ####
` #.*$  #
` # .$# #
` ## @  #
 ` #   ##
 ` #####

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
