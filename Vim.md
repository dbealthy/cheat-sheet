# Vim
## Modes
There are two mods in Vim:
- *Insert*
- *Command* (default)
- *Visual* 
---
`i` - To change mode from Command to insert 
`Esc` - To get back to command mode
`v` in command mode to enter *visual mode*

---
Command and visual mode are case sensative

**Insert mode** - this is where you insert all text. In this mode every character that you type is inserted in the current location

**Command mode** - default mode in Vim. Every characted that you type is interpreted as command

**Visual mode** - Allows to select text (cut, copy, delete)



## Save file, exit ...
*In command code*
`:w` - to save file (write)
`:w` + filename - save to file with specified name
`:q` - exit vim (quit)
`:wq` - save and exit
`:q!` - exit and discard changes

## Moving cursor
*Using arrows is possible*
`h`  - left
`j` - down
`k` - up
`l` - right
`0` - move to the beginning of the line
`$` - move tp the end of the line
## Insertion mode options
*Command mode*
`a` - moves cursor right and enters insertion mode
`A` - moves cursor in the end of line and ins mode
`o` - makes line below and enters insert mode
`O` - makes line above and enters insert mode

## Moving within file
*Command mode*
`gg` - move in the begging
`G` - move
`w` - move to next word
`B` - move to the privious word back
`b` - move to the begging of the word
`e` - move to the end of the next word
`:` + line number - move to specofied line
## Execute command multiple times
*Command mode*
To do so we add number before command
`2w` - moves two words 
`10b` - ten words back
## Searching
*Command mode*
`f` + symbol move to the symbol in current line 
`f222` - find 222 in current line
`/` + something - find up to document's bottom
`?` + something - find up to document's top
(Press `n` to find next search result)
(Press `N` to find previous search result)
## Bookmarks
*Command mode*
`m` + name - create mark with some name in specified line
`'` + name - return to named mark
## Copy, past, delete, replace
*Visual mode* (press v in command mode)
`x` / `d` - cut selected text
`y` - copy selected text
`yy` - copy current line
`dw` - delete word
`dd` - delete line
`D` - delete to the end of line
`p` - past in the right of cursor
`P` - past in the left of cursor


## Undo, Redo
`u` - undo
`Ctrl_R` - redo
## Change text
`cw` - change word
`C` - change text to the end of line
`CC` - Delete whole line and enter insert mode
`Alt` + `k`/`j` - move line up or down
## Selection
*visual mode*
`V` - select whole line
## Vim Macro
1. `q` + digit - create macro
2. Go insert mode
3. Change file the way we want
4. `q` - finish macros
5. `@` + digit - use macros
6. n + `@` + digit - execute macros n times